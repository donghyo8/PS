#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
    int answer = 0;
    int index = 0;
    
    queue<int> queue;

    for (int i = 0; i < bridge_length; i++)
    {
        queue.push(0);
    }

    while (1)
    {
        // 큐의 맨앞에 원소를 weight에 append하고 큐에서 제거
        weight += queue.front(); 
        queue.pop();

        if (weight - truck_weights[index] >= 0)
        {
            if (truck_weights.size() == index + 1)
            {
                answer += bridge_length + 1;
                break;
            }

            weight -= truck_weights[index];
            queue.push(truck_weights[index]); 
            index++;
        }
        else // 트럭을 더 못올리면 0으로 트럭 밀기
        {
            queue.push(0);
        }
        // 전체 루프에서 한칸씩 움직인다고 볼때 1초씩 증가
        answer++; 
    }
    cout << answer << endl;
    return answer;
}

int main()
{

    int len = 2;
    int weight = 10;
    vector<int> truck_weight = {7, 4, 5, 6};

    solution(len, weight, truck_weight);
    return 0;
}

