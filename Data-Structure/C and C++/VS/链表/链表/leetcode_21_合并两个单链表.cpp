#define _CRT_SECURE_NO_WARNINGS 
#include<iostream>
using namespace std;


#define OK 1
#define ERROR 0
#define MAXSIZE 50


typedef int ElemType;
typedef int Status;

// 结点
typedef struct LNode {
    ElemType data;  
    struct ListNode* next;
}LNode, *LinkList;

// 初始化单链表
Status InitList(LinkList &L) {
    L = new LNode;
    L->next = NULL;
    return OK;
}

// 创建单链表_前插法
void CreatList_H(LinkList& L, int n, int arr[]) {
    LinkList p;
    L = new LNode;
    L->next = NULL;
    for (int i = 0; i < n; i++) {
        p = new LNode;

    }
}





int main(){
    int list1[MAXSIZE] = {};
    int list2[MAXSIZE] = {};

    ListNode L;   // 创建一个结点
    


    return 0;


}
