#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int solution(int n, vector<vector<int>> computers)
{
    queue<int> que;
    int answer = 0;
    int visit[200] = {
        0,
    };

    if (n >= 1 && n <= 200)
    {
        for (int i = 0; i < n; i++)
        {
            answer++;
            visit[i] = 1;
            que.push(i);
        }

        if (!que.empty())
        {
            int current = que.front();
            que.pop();

            for (int j = 0; j < n; j++)
            {
               
                if (current != j && computers[current][j] == 1 && visit[j] == 0)
                {
                    que.push(j);
                    visit[j] = answer;
                }
            }
        }
    }
    return answer;
}