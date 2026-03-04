#include<iostream> 
using namespace std;

#define ERROR 0
#define OK 1

typedef char ElemType;
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
    e = S->data;
    LinkStack p;
    p = new StackNode;
    p = S;
    S = S->next;
    delete p;
    return OK;
}

Status StackEmpty(LinkStack S)
{
    if(S == NULL)
        return true;
    else
        return false;
}

Status GetTop(LinkStack S)
{
    if(S == NULL)
        return ERROR;
    return S->data;
}

bool Matching()
{
    int flag = 1;
    LinkStack S;
    InitStack(S);
    char ch;
    cin >> ch;
    while(ch != '#' && flag)
    {
        switch(ch)
        {
            case '{':
                Push(S, ch);
                break;
            case '[':
                Push(S, ch);
                break;
            case '(':
                Push(S, ch);
                break;
            case '}':
                if(!StackEmpty(S) && GetTop(S)=='{')
                {
                    char c;
                    Pop(S, c);
                    cout << c << "*" <<  endl;
                }
                else
                    flag = 0;
                break;
            case ']':
                if(!StackEmpty(S) && GetTop(S)=='[')
                {
                    char c;
                    Pop(S, c);
                }
                else
                    flag = 0;
                break;
            case ')':
                if(!StackEmpty(S) && GetTop(S)=='(')
                {
                    char c;
                    Pop(S, c);
                }
                else
                    flag = 0;
                break;
        }
        cin >> ch;
    }
    if(StackEmpty(S) && flag) 
    {
        cout << "正确" << endl;
        return true;
    }
    else 
    {
        cout << "错误" << endl;
        return false;
    }
}

int main()
{
    Matching();
}