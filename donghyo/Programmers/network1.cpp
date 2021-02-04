#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

// BFS

int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;
    queue<int> queue;
    bool visit[200] = {
        0,
    };

    if (n >= 1 && n <= 200)
    {
        for (int i = 0; i < n; i++)
        {
            // 방문한 노드가 1이 아닐 경우, 방문했다고 표시하고 큐에 삽입
            if (visit[i] != 1)
            {
                answer++;
                visit[i] = true;
                queue.push(i);
            }

            while (!queue.empty())
            {
                // 루프를 돌며 큐 맨앞에 있는 원소를 현재 노드의 값으로 보고 큐에서 제거
                int current = queue.front();
                queue.pop();

                for (int j = 0; j < n; j++)
                {
                    // 현재 노드의 값이 1이고, 방문하지 않은 노드라면 
                    if (computers[current][j] == true && visit[j] == false)
                    {
                        visit[j] = true;
                        queue.push(j);
                    }
                }
            }
        }

        cout << answer << endl;
        return answer;
    }
}

int main()
{

    int n = 3;
    vector<vector<int>> computers1 = {{1, 1, 0}, {1, 1, 0}, {0, 0, 1}};
    vector<vector<int>> computers2 = {{1, 1, 0}, {1, 1, 1}, {0, 1, 1}};

    solution(n, computers1);

    return 0;
}