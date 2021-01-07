#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve)
{
    int answer = 0;
    vector<int> temp(n, 1);

    sort(lost.begin(), lost.end());

    for (int i = 0; i < reserve.size(); i++)
    {
        temp[reserve[i - 1]]++;
    }
    for (int i = 0; i < lost.size(); i++) // 도둑 맞은 학생
    {
        temp[lost[i] - 1]--;
    }
    if (temp[0] == 0) // 첫번째 학생이 체육복 없을 경우
    {
        if (temp[1] == 2)
        {
            temp[0]++;
            temp[1]--;
        }
    }
    for (int i = 1; i < n - 1; i++) // 학생들 중 체육복 없는 학생
    {
        if (temp[i] == 0)
        {
            if (temp[i - 1] == 2) // 이전 인덱스 학생한테 받기
            {
                temp[i - 1]--;
                temp[i]++;
            }
            else if (temp[i + 1] == 2) // 이전 학생이 체육복이 없으면 다음 학생 인덱스 받기
            {
                temp[i + 1]--;
                temp[i]++;
            }
        }
    }
    if (temp[n - 1] == 0) // 마지막 학생이 체육복 없을 경우
    {
        if (temp[n - 2] == 2)
        {
            temp[n - 2]--;
            temp[n - 1]++;
        }
    }
    for (int i = 0; i < n; i++) // 루프 돌며 체육복 계산
    {
        if (temp[i] > 0)
        {
            answer++;
        }
    }

    cout << "return : " << answer << endl;
    return answer;
}

int main()
{
    int students = 5;
    vector<int> lost = {2, 4};
    vector<int> reserveList = {3};

    solution(students, lost, reserveList);
    return 0;
}