#include<iostream>
using namespace std;

# define MAXSIZE 100
# define TRUE 1
# define OK 1
# define ERROR 0
# define INFEASIBLE -1
# define OVERFLOW -2


typedef int QElemType; 
typedef int SElemType; 
typedef int Status; 
typedef int ElemType; 

// 队列的顺序存储结构
typedef struct
{
    QElemType *base;
    int front;
    int rear;
}SqQueue;

Status InitQueue(SqQueue &Q)
{
    Q.base = new QElemType[MAXSIZE];
    if(!Q.base) return ERROR;
    Q.front = Q.rear = 0;
    return OK;
}


int QueueLength(SqQueue Q)
{
    return (Q.rear-Q.front+MAXSIZE)%MAXSIZE;
}


Status EnQueue(SqQueue &Q, QElemType e)
{
    if((Q.rear+1)%MAXSIZE == Q.front) return ERROR;
    Q.base[Q.rear] = e;
    Q.rear = (Q.rear+1)%MAXSIZE;
    return OK;
}

Status DeQueue(SqQueue &Q, QElemType &e)
{
    if(Q.front = Q.rear) return ERROR;
    e = Q.base[Q.front];
    Q.front = (Q.front+1)%MAXSIZE;
    return OK;
}

SElemType GetHead(SqQueue &Q)
{
    if(Q.front == Q.rear) return ERROR;
    return Q.base[Q.front];
}


int main()
{
    SqQueue Q;
    InitQueue(Q);
    cout << Q.base << endl;


}