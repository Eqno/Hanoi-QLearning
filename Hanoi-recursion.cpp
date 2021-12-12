#include <iostream>
#include <vector>
using namespace std;

int n, step = 0;
vector <int> a, b, c;

// 显示 v 当前层的盘子。
void judge(int i, const vector <int> &v) 
{
	if (i < v.size()) printf("%3d|", v[i]);
	else printf("   |");
}

void show()
{
	puts("------------");
	for (int i=n-1; i>=0; i--)
	{
		judge(i, a);
		judge(i, b);
		judge(i, c);
		putchar('\n');
	}
	puts("---|---|---|\n  A|  B|  C|\n------------");
}

// 记录每一步的操作。
int parse(const vector <int> &x)
{
	if (x == a) return 'A';
	if (x == b) return 'B';
	if (x == c) return 'C';
	return 'N';
}

// 把 1 个盘子，从 x 移动至 y。
void move(vector <int> &x, vector <int> &y)
{
    y.push_back(x.back());
	x.pop_back();
    printf("第%d步操作：%c柱移到%c柱上。\n", ++step, parse(x), parse(y));
    show();
}

// 把 n 个盘子，从 x 借助 y 移动至 z。
void hanoi(int t, vector <int> &x, vector <int> &y, vector <int> &z)
{
	if (t == 1) move(x, z);
	else
	{
		hanoi(t-1, x, z, y);
		move(x, z);
		hanoi(t-1, y, x, z);
	}
}

int main()
{
	printf("请输入初始柱子上盘子的个数：");
	scanf("%d", &n);
    if (n > 25)
    {
        puts("n 太大导致程序要跑太久！");
        return 0;
    }
	for (int i=n; i>=1; i--)
		a.push_back(i);
    puts("初始状态：");
	show();
	hanoi(n, a, b, c);
	puts("已达成目标状态。");
	return 0;
}
