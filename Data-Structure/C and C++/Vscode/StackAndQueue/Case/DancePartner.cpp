#include<iostream>
using namespace std;

#define ERROR 0
#define OK 1
#define MAXSIZE 100


typedef int Status;

// 跳舞者的个人信息
typedef struct
{
    char name[20];
    char sex;
}Person;

// 队列的顺序存储结构
typedef struct 
{
    Person *base;
    int front;
    int rear;
}SqQueue;

SqQueue Mdancers, Fdancers;   // 分别存放男士和女士入队者队列

Status InitSqQueue(SqQueue &Q)
{
    Q.base = new Person[MAXSIZE];
    if(!Q.base) return ERROR;
    Q.front = Q.rear = 0;
    return OK;
}


int main()
{
    string dancers[][7] = {{"1", "man"}, {"2", "man"}, {"3", "woman"}, {"4", "woman"}};
    for(int i=0; i < sizeof(dancers[0])/sizeof(string); i++)
    {
        cout << dancers[i][1] << endl;
    }
}   