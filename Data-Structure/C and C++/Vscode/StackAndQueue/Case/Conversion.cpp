// 利用栈实现进制的转换
#include<iostream>
using namespace std;

#define OK 1
#define ERROR 0

typedef int ElemType;
typedef int Status;


typedef struct StackNode
{
    ElemType data;
    struct StackNode *next;
}StackNode, *LinkStack;

Status InitStack(LinkStack &S)
{   
    S = NULL;
    return OK;
}

Status StackEmpty(LinkStack S)
{
    if(S == NULL)
        return OK;
    else
        return ERROR;
}

Status Push(LinkStack &S, ElemType e)
{
    LinkStack p;
    p = new StackNode;
    p->data = e;
    p->next = S;
    S = p;
    return OK;
}

Status Pop(LinkStack &S, ElemType &e)
{
    if(S == NULL) return ERROR;
    LinkStack p;
    e = S->data;
    p = S;
    S = S->next;
    delete p;
    return OK;
}

void conversion(int N, int n)
{
    LinkStack S;
    InitStack(S);   // 初始化栈
    while(N)
    {
        Push(S, N%n);
        N = N/n;
    }
    while(!StackEmpty(S))
    {
        int e;
        Pop(S, e);
        cout << e;
    }
}

int main()
{
    int N = 200;
    int n = 8;
    conversion(N, n);
}