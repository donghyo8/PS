#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
    vector<int> answer;
    int index = 0;
    int workDay = 0;

    while (index != progresses.size())
    {
        int count = 0;
        workDay++;

        for (int i = index; i < progresses.size(); i++)
        {
            // 작업진도 + 작업속도 * 일수
            // ex.) 93 + 1 * workDay > = 100
            // 100%보다 클경우, 인덱스 및 카운트 값 증가

            if ((progresses[index] + (speeds[index] * workDay)) >= 100)
            {
                index++;
                count++;
            }
        }
        if (count != 0)
        {
            answer.push_back(count);
        }
    }

    for (int i = 0; i < answer.size(); i++)
    {
        cout << answer[i] << " ";
    }

    cout << endl;
    return answer;
}

int main()
{

    vector<int> progresses = {95, 90, 99, 99, 80, 99};
    vector<int> speeds = {1, 1, 1, 1, 1, 1};

    solution(progresses, speeds);

    return 0;
}