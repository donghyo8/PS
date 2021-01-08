#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit)
{
    int answer = 0;
    int index = 0;


    while (index < people.size())
    {
        if (people[index] + people.back() <= limit)
        {
            index++;
        }
        people.pop_back();
        answer++;
    }

    cout << answer << endl;
    return answer;
}

int main()
{

    vector<int> people = {70, 80, 50};
    int limit = 100;

    solution(people, limit);
    return 0;
}