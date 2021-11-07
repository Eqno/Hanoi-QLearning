import numpy
import random
import copy

def getValidOpt(state):
    operation = []
    for i, s in enumerate(state):
        if len(s):
            for j, t in enumerate(state):
                if i != j:
                    if not len(t) or state[i][0] < state[j][0]:
                        operation.append((i, j))
    return operation

def getTuple(state):
    return tuple(tuple(i) for i in state)

def move(state, opt):
    res = copy.deepcopy(state)
    res[opt[1]].insert(0, res[opt[0]][0])
    res[opt[0]].pop(0)
    return res

def epsilonGreedy(Q, state, epsilon):
    operation = getValidOpt(state)
    if numpy.random.uniform() < epsilon:
        return operation[random.randint(0, len(operation)-1)]
    else:
        Qs = numpy.array([Q.get((getTuple(state), i), 0) for i in operation])
        return operation[numpy.argmin(Qs)]

# repTime->重复次数, decayFactor->衰减系数, origin->初始状态, target->目标状态
def trainQ(repTime, learnRate, decayFactor, origin, target):
    epsilon = 1.0
    stepNum = []
    Q = {}
    for _ in range(repTime):
        epsilon *= decayFactor
        step = 0
        lastState = []
        lastOpt = ()
        state = copy.deepcopy(origin)
        while True:
            step += 1
            opt = epsilonGreedy(Q, state, epsilon)
            newState = move(state, opt)
            if (getTuple(state), opt) not in Q:
                Q[(getTuple(state), opt)] = 0
            if newState == target:
                Q[(getTuple(state), opt)] = 1
                stepNum.append(step)
                break
            else:
                if step > 1:
                    Q[(getTuple(lastState), lastOpt)] += learnRate \
                        * (1 + Q[(getTuple(state), opt)] - Q[(getTuple(lastState), lastOpt)])
                lastState = copy.deepcopy(state)
                lastOpt = copy.deepcopy(opt)
                state = copy.deepcopy(newState)
    return Q, stepNum

def testQ(Q, maxStep, origin, target):
    state = origin
    path = [[state, ()]]
    step = 0
    while True:
        step += 1
        Qs = []
        operation = getValidOpt(state)
        for i in operation:
            Qs.append(Q.get((getTuple(state), i), 0xffffff))
        opt = operation[numpy.argmin(Qs)]
        newState = move(state, opt)
        path.append([newState, opt])
        if newState == target:
            return path
        elif step >= maxStep:
            print("%d步内无法达到目标状态。" % maxStep)
            return []
        state = copy.deepcopy(newState)

def printState(state, N, M):
    for i in range(N-1, -1, -1):
        for j in state:
            index = len(j) - i - 1
            print("|%2d "%j[index] if index>=0 else "|   ", end='')
        print("|")
    for _ in range(M):
        print("|---", end='')
    print("|")
    for i in range(M):
        print("| %c " % chr(ord('A')+i), end='')
    print("|")

def printPath(path):
    if not len(path):
        return
    N = max(len(i) for i in path[0][0])
    M = len(path[0][0])
    map = {i : chr(ord('A')+i) for i in range(M)}
    print("\n初始状态：\n")
    for i, s in enumerate(path):
        if len(s[1]):
            print("\n第%d步操作：%c --> %c\n" % (i, map[s[1][0]], map[s[1][1]]))
        printState(s[0], N, M)
    print("\n已达到目标状态。")

origin = [[1, 2, 3, 4, 5], [], [], [], []]
target = [[], [], [], [], [1, 2, 3, 4, 5]]

Q, stepNum = trainQ(2000, 0.5, 0.7, origin, target)
path = testQ(Q, 100, origin, target)

print("共需要%d步。" % len(path))
printPath(path)