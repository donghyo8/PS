#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int a, int b)
{
    string answer = "";
    vector<string> days = {"FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"};
    vector<int> month_end = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int days_total = 0;

    for (int i = 0; i < a - 1; i++)
    {
        days_total += month_end[i];
    }

    days_total += b-1;
    cout << days_total << endl;

    answer = days[days_total % 7];

    cout << answer << endl;

    return answer;
}

int main()
{

    int a = 5, b = 24;

    solution(a, b);

    return 0;
}