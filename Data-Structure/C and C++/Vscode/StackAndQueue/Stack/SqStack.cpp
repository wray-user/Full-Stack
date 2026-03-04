#include<iostream>
using namespace std;

# define MAXSIZE 100
# define TRUE 1
# define OK 1
# define ERROR 0
# define INFEASIBLE -1
# define OVERFLOW -2


typedef int SElemType; 
typedef int Status; 



// 顺序栈存储结构
typedef struct 
{
    SElemType *base;
    SElemType *top;
    int stacksize;
}SqStack;


// 顺序栈初始化
Status InitStack(SqStack &S)
{
    S.base = new SElemType[MAXSIZE];   
    if(!S.base) exit(OVERFLOW);
    S.top = S.base;
    S.stacksize = MAXSIZE;
    return OK;
}

Status Push(SqStack &S, SElemType &e)
{
    if(S.top-S.base == S.stacksize)  return ERROR;
    *S.top++ = e;   // 先赋值，再自增
    return OK;
}

Status Pop(SqStack &S, SElemType &e)
{
    if(S.top == S.base) return ERROR;
    e = *--S.top;  // 先减再赋值
    return OK;
}

SElemType GetTop(SqStack S, SElemType &e)
{
    if(S.top != S.base)
        return *(S.top-1);    // 因为栈顶元素不是在S.top里面的。
}




int main()
{
    

}