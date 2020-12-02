#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int n)
{
    string answer = "";

    if (n <= 10000)
    {
        for (int i = 0; i <= n - 1; i++)
        {
            answer += (i % 2 == 0) ? "수" : "박";
        }
    }

    return answer;
}

int main()
{
    int n = 3;

    cout << solution(n) << endl;
}