#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(int n)
{
    vector<int> answer;
    vector<vector<int>> map(n, vector<int>(n));

    int number = 1;
    int index = map.size() - 1;
    int x = 0, y = 0;

    for (int index = n - 1; index >= 0; index -= 3)
    {
        // index가 0 일시 마지막 좌표 채우기(testcase n = 4)
        if (index == 0)
        {
            map[x][y] = number;
            break;
        }

        // 왼쪽
        for (int i = 0; i < index; i++)
        {
            map[x][y] = number++;
            x++;
        }

        // 바닥
        for (int i = 0; i < index; i++)
        {
            map[x][y] = number++;
            y++;
        }

        // 오른쪽
        for (int i = 0; i < index; i++)
        {
            map[x][y] = number++;
            x--;
            y--;
        }
        // 좌표 이동
        x += 2;
        y += 1;
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (map[i][j] != 0)
            {
                answer.push_back(map[i][j]);
            }
        }
    }
    // 달팽이 출력
    for (int i = 0; i < n; i++)
    {

        for (int j = n - 1; j > i; j--)
        {
            cout << " ";
        }

        for (int j = 0; j < 1 * i + 1; j++)
        {
            cout << " ";

            cout << map[i][j];
        }
        cout << endl;
    }

    return answer;
}

int main()
{

    int n = 6;

    solution(n);

    return 0;
}