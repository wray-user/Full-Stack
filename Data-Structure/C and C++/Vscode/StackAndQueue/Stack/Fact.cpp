#include<iostream>
using namespace std;

long Fact(long n)
{
    if(n == 0) return 1;
    else return Fact(n-1)*n;
}

int main()
{
    long n = 4;
    int c = Fact(n);
    cout << c << endl;
}