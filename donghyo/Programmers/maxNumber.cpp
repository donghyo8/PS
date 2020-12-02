#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

bool compare(const string &a, const string &b)
{
    return a + b > b + a;
}

string solution(vector<int> numbers)
{
    string answer = "";
    vector<string> temp;

    for (int i = 0; i < numbers.size(); i++)
    {

        temp.push_back(to_string(numbers[i]));
    }

    sort(temp.begin(), temp.end(), compare);

    for (int i = 0; i < temp.size(); i++)
    {
        answer += temp[i];
    }

    if (answer[0] == '0')
    {
        return "0";
    }
    return answer;
}

int main()
{
    vector<int> numbers1 = {6, 10, 2};
    vector<int> numbers2 = {3, 30, 34, 5, 9};

    solution(numbers1);

    return 0;
}