#include<iostream>
using namespace std;

void move(char A, char C)
{
    cout << A << C << endl;
}
void Hanoi(int n, char A, char B, char C)
{
    if(n==1) move(A, C);
    else
    {
        Hanoi(n-1, A, C, B);
        move(A, C);
        Hanoi(n-1, B, A, C);
    }
}

int main()
{   
    int n = 4;
    char A = 65;
    char B = 66;
    char C = 67;
    Hanoi(n, A, B, C);

}