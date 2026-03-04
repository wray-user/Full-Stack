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


// 队列的链式存储结构
typedef struct QNode
{
    QElemType data;
    struct QNode *next;
}QNode, *QueuePtr;
typedef struct 
{
    QueuePtr front;
    QueuePtr rear;
}LinkQueue;


Status InitQueue(LinkQueue &Q)
{
    Q.front = Q.rear = new QNode;
    Q.front->next = NULL;
    return OK;
}

Status EnQueue(LinkQueue &Q, QElemType e)
{
    QueuePtr p;
    p = new QNode;
    p->data = e;
    p->next = NULL;
    Q.rear->next = p;
    Q.rear = p;
    return OK;
}

Status DeQueue(LinkQueue &Q, QElemType &e)
{
    if(Q.front == Q.rear) return ERROR;
    QueuePtr p;
    p = Q.front->next;
    e = p->data;
    Q.front->next = p->next;
    if(Q.rear==p) Q.rear == Q.front;
    delete p;
    return OK;
}

SElemType GetHead(LinkQueue Q)
{
    if(Q.front != Q.rear)
        return Q.front->next->data;
}

int main()
{



}

