#include<iostream>
using namespace std;

long Fib(long n)
{
    if (n==1 || n==2) return 1;
    else return Fib(n-1) + Fib(n-2);
}

int main()
{
    long c = Fib(4);
    cout << c << endl;
}

