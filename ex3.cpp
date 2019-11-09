#include <iostream>
#include<stdio.h>
#include<stdlib.h>
using namespace std;

double random(double a, double b)
{
    return a + (b - a) * (rand() / double(RAND_MAX));
}

double f1(double x)
{
    return x * x ;
}

double f2(double x)
{
    return x * x * x ;
}

double s(double a, double b, double c, double d, int n, double (*f)(double))
{
    double s = (d - c ) * (b - a);
    double s1 = 0;
    int hit = 0;
    for(int i = 0; i < n; i++)
    {
        double x = random(a, b);
        double y = random(c, d);
        if(y >= 0 && y <= (*f)(x))
        {
            hit++;
        }
        else if(y < 0 && y >= (*f)(x)) //如果阴影在y轴下方记为负的面积
        {
            hit--;
        }
    }
    if(c > 0)
    {
        s1 = c * (b - a);
    }
    else if(d < 0)
    {
        s1 = d * (b - a);
    }
    return s1 + s * double(hit) / double(n); //矩形abcd中的阴影面积还要要加上坐标轴和abcd之间的矩形面积
}

int main()
{
    cout << s(1, 2, 1, 4, 1000000, f1) << endl; //2.33
    cout << s(-1, 2, 0, 4, 1000000, f1) << endl; //3
    cout << s(-1, 2, -1, 8, 1000000, f2) << endl; //3.75
    cout << s(-3, -2, -27, -8, 1000000, f2) << endl; //-16.25
}
