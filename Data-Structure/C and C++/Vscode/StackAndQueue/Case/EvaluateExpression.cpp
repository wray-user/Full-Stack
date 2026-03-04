#include<iostream>
using namespace std;

#define OK 1
#define ERROR 0

typedef int ElemType;
typedef int Status;
typedef int SElemType;

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
    if(S==NULL) return ERROR;
    LinkStack p;
    p = new StackNode;
    p = S;
    e = S->data;
    S = S->next;
    delete p;
    return OK;
}

Status StackEmpty(LinkStack S)
{
    if(S==NULL) return ERROR;
    else return OK;
}

SElemType GetTop(LinkStack S)
{
    if(S==NULL) return ERROR;
    SElemType e;
    e = S->data;
    return e;
}

SElemType In(SElemType ch)
{
    ch = char(ch);
    if(ch=='+' || ch=='-' || ch=='*' || ch=='/' || ch=='(' || ch==')'|| ch=='#') return OK;
    else return ERROR;
}

SElemType Precede(char ch1, char ch2)
{
    if(ch1=='#') return '<';
    else if(ch2=='#') return '>';
    else if((ch1=='+' || ch1=='-') && (ch2=='*' ||ch2=='/')) return '<';
    else if((ch1=='*' || ch1=='/') && (ch2=='+' ||ch2=='-')) return '>';
    else if((ch1=='+' || ch1=='-') && (ch2=='+' ||ch2=='-')) return '>';
    else if((ch1=='*' || ch1=='/') && (ch2=='*' ||ch2=='/')) return '>';
    else if((ch1=='(') && (ch2==')')) return '='; 
    else if(ch1=='(' || ch2=='(') return '<';
    else if(ch2==')' && ch1!='(') return '>';
    else return '=';
}

SElemType Operate(SElemType a, char theta, SElemType b)
{
    if(theta == '-') return a-b;
    else if(theta == '+') return a+b;
    else if(theta == '*') return a*b;
    else if(theta == '/') return a/b;
    else return 0;
    
}

SElemType EvaluateExpression()
{
    LinkStack OPTR, OPND;
    InitStack(OPTR);
    InitStack(OPND);
    Push(OPTR, '#');   // 将'#'压入OPTR栈
    char ch;
    cin >> ch;
    while(ch!='#' || char(GetTop(OPTR))!='#')
    {
        if(!In(ch)) 
        {
            Push(OPND, ch);   // 不是运算符进 'OPND'栈，这里压入的是ASCII码
            cin >> ch;
        }
        else
            switch(Precede(GetTop(OPTR), ch))   // 比较输入的运算符与前一个运算符的优先级
            {
                case '<':
                    Push(OPTR, ch);   // 如果前优先级较，将当前运算符压入OPTR栈
                    cin >> ch;
                    break;
                case '>':
                    int theta;
                    Pop(OPTR, theta);  // 如果前优先级高，将前一个运算符取出来进行运算
                    int a, b;
                    Pop(OPND, b);Pop(OPND, a);  // 弹出栈顶两个运算数
                    Push(OPND, Operate(a-'0', theta, b-'0')+'0');  // 这里计算时需将a,b转为int
                    break;
                case '=':    // 如果是')'， 则弹出来
                    int k;
                    Pop(OPTR, k);
                    cin >> ch;
                    break;
            }
    }
    return (GetTop(OPND)-'0');
    
}

int main()
{
    SElemType a;
    a = EvaluateExpression();
    cout << a << endl;
}