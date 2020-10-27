#include <iostream>
#include <cmath>
#define f(x) ({x-cos(x);})
int main() {
    float a,b,m;
    for(std::cin>>a>>b;b-a>1e-6;(f(m)*f(a)>0?a:b)=m)m=(a+b)/2;
    std::cout<<m;
}

