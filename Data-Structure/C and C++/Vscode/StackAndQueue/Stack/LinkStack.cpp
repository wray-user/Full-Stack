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
typedef int ElemType; 


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



Status Push(LinkStack &S, SElemType e)
{
    LinkStack p;
    p = new StackNode;
    p->data = e;
    p->next = S;
    S = p;
    return OK;
}

Status Pop(LinkStack &S, SElemType &e)
{
    LinkStack p;
    if(S==NULL) return ERROR;
    e = S->data;
    p = S;
    S = S->next;
    delete p;
    return OK;
}

SElemType GetTop(LinkStack &S, SElemType &e)
{
    if(S==NULL) return ERROR;
    return S->data; 
}







int main()
{



}