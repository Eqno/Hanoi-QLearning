import copy

def getTuple(mat):
    return tuple(tuple(i) for i in mat)

def getValidOpt(mat):
    res = []
    for i, s in enumerate(mat):
        if len(s):
            for j, t in enumerate(mat):
                if i != j:
                    if not len(t) or mat[i][0] < mat[j][0]:
                        res.append((i, j))
    return res

def moveState(state, opt):
    mat = state[0]
    pat = state[1]
    res = copy.deepcopy(mat)
    nxt = copy.deepcopy(pat)
    res[opt[1]].insert(0, res[opt[0]][0])
    res[opt[0]].pop(0)
    nxt.append(opt)
    return [res, nxt]

def search(origin, target):
    step = 0
    start = [origin, []]
    vis = set()
    st = []
    st.append(start)
    lastlen = 0
    while len(st):
        state = st[0]
        st.pop(0)
        mat = state[0]
        pat = state[1]
        if len(pat) > lastlen:
            step += 1
        lastlen = len(pat)
        if mat == target:
            return True, [pat, len(vis)]
        opt = getValidOpt(mat)
        for i in opt:
            newState = moveState(state, i)
            tmp = getTuple(newState[0])
            if tmp not in vis:
                st.append(newState)
                vis.add(getTuple(tmp))
    return False, [[], len(vis)]

def moveMat(mat, opt):
    res = copy.deepcopy(mat)
    res[opt[1]].insert(0, res[opt[0]][0])
    res[opt[0]].pop(0)
    return res

def printMat(mat, n):
    print('-', end='')
    for i in range(len(mat)):
        print("---", end='')
    print()
    i = n
    while i >= 0:
        print('|', end='')
        for j in mat:
            if i < len(j):
                print("%2d" % j[len(j)-i-1], end='')
            else:
                print('  ', end='')
            print('|', end='')
        print()
        i -= 1
    print('-', end='')
    for i in range(len(mat)):
        print("---", end='')
    print()
    print('|', end='')
    for i in range(len(mat)):
        print('%2d|' % (i+1), end='')
    print()
    print('-', end='')
    for i in range(len(mat)):
        print("---", end='')
    print()

origin = [[1, 2, 3, 4], [], [], [], []]
target = [[], [], [], [], [1, 2, 3, 4]]

reachable, ans = search(origin, target)
if reachable:
    n = max(len(i) for i in ans[0])
    print("达成目标状态最少需要%d步。" % len(ans[0]))
    print("初始状态：")
    printMat(origin, n)
    for i, opt in enumerate(ans[0]):
        print("第%d步操作，%d柱移到%d柱上。" % (i+1, opt[0]+1, opt[1]+1))
        origin = moveMat(origin, opt)
        printMat(origin, n)
    print("已达成目标状态。")
    print("搜过%d步可能的步数。\n" % ans[1])
else:
    print("无解！")
    print("搜过%d步可能的步数。\n" % ans[1])