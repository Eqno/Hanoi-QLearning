#include <iostream>
#include <vector>
using namespace std;

int n, step = 0;
vector <int> a, b, c;

// ��ʾ v ��ǰ������ӡ�
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

// ��¼ÿһ���Ĳ�����
int parse(const vector <int> &x)
{
	if (x == a) return 'A';
	if (x == b) return 'B';
	if (x == c) return 'C';
	return 'N';
}

// �� 1 �����ӣ��� x �ƶ��� y��
void move(vector <int> &x, vector <int> &y)
{
    y.push_back(x.back());
	x.pop_back();
    printf("��%d��������%c���Ƶ�%c���ϡ�\n", ++step, parse(x), parse(y));
    show();
}

// �� n �����ӣ��� x ���� y �ƶ��� z��
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
	printf("�������ʼ���������ӵĸ�����");
	scanf("%d", &n);
    if (n > 25)
    {
        puts("n ̫���³���Ҫ��̫�ã�");
        return 0;
    }
	for (int i=n; i>=1; i--)
		a.push_back(i);
    puts("��ʼ״̬��");
	show();
	hanoi(n, a, b, c);
	puts("�Ѵ��Ŀ��״̬��");
	return 0;
}
