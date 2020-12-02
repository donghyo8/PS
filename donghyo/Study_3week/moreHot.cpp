#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int solution(vector<int> scoville, int K)
{
    int answer = 0;
    int maxUnhot_scov = 0, secondUnhot_scov = 0;
    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < scoville.size(); i++)
    {
        // 큰 순서대로 pq에 푸쉬
        pq.push(scoville[i]);
    }

    // pq의 맨앞에 있는 원소가 스코빌 지수 K 보다 클때 까지 루프 반복
    while (pq.top() < K && pq.size() != 1)
    {
        // pq의 top(first)과 second 값을 꺼내어 섞어서 pq에 넣고 섞은 횟수 증가
        // 섞은음식의 스코빌 지수
        // --> 가장 맵지않은 음식의 스코빌 지수 + (두번째로 맵지 않은 음식의 스코빌 지수 * 2)

        maxUnhot_scov = pq.top();
        pq.pop();
        secondUnhot_scov = pq.top();
        pq.pop();

        pq.push(maxUnhot_scov + (secondUnhot_scov * 2));
        answer++;
    }

    // 모든 음식의 스코빌 지수를 K 이상으로 만들수 없는 경우 -1 return
    if (pq.top() <= K)
    {
        return -1;
    }

    cout << answer << endl;
    return answer;
}

int main()
{

    vector<int> scoville = {1, 2, 3, 9, 10, 12};
    int K = 7;

    solution(scoville, K);
    return 0;
}