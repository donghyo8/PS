#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

vector<int> solution(int N, vector<int> stages)
{

    vector<int> answer;
    double arr[3][501] = {
        0,
    };

    // 분자 계산
    for (int i = 0; i < stages.size(); i++)
    {
        arr[0][stages[i]]++;
    }

    // 분모 계산
    arr[1][N] = arr[0][N] + arr[0][N + 1];
    
    for (int i = N - 1; i >= 1; i--)
    {
        arr[1][i] = arr[0][i] + arr[1][i + 1];
    }

    // 실패율 계산
    for (int i = 1; i <= N; i++)
    {
        if (arr[1][i] == 0)
        {
            arr[2][i] = 0;
        }
        else
        {
            // 스테이지에 도달했으나 아직 클리어 못한 플레이어 수 / 스테이지에 도달한 플레이어 수
            arr[2][i] = arr[0][i] / arr[1][i];
        }
    }

    // answer에 index 할당
    while (answer.size() < N)
    {
        int index = 1;
        for (int i = 1; i <= N; i++)
        {
            if (arr[2][index] < arr[2][i])
            {
                index = i;
            }
        }
        answer.push_back(index);
        arr[2][index] = -1;
    }

    return answer;
}

int main()
{
    int N = 5;
    vector<int> stages = {2, 1, 2, 6, 2, 4, 3, 3};

    solution(N, stages);

    return 0;
}