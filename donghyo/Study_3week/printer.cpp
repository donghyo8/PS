#include <string>
#include <vector>
#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location)
{
    int answer = 0;
    priority_queue<int> pq; //
    queue<pair<int, int>> que;

    for (int i = 0; i < priorities.size(); i++)
    { //           que
        //    ex.) 1, 0
        //         1, 1
        //         9, 2
        //         1, 3
        //         1, 4
        //         1, 5

        pq.push(priorities[i]);
        que.push(make_pair(priorities[i], i));
    }

    while (!que.empty())
    {
        int first = que.front().first;
        int second = que.front().second;

        que.pop();

        if (pq.top() == first)
        {
            answer++;
            pq.pop();

            if (second == location)
            {
                break;
            }
        }
        else
        {
            que.push(make_pair(first, second));
        }
    }

    cout << answer << endl;
    return answer;
}

int main()
{

    vector<int> priorities = {1, 1, 9, 1, 1, 1};
    int location = 0;

    solution(priorities, location);
}