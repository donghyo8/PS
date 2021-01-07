#include <string>
#include <vector>
#include <iostream>

using namespace std;

long long solution(int a, int b)
{
    long long answer = 0;
    int c = 0;

    if (a > b)
    {
        c = a;
        a = b;
        b = c;
    }

    for (int i = a; i <= b; i++)
    {
        answer += i;
    }

    cout << answer << endl;
    return answer;
}

int main()
{

    int a = 3, b = 5;

    solution(a, b);
    return 0;
}