#include <string>
#include <vector>
#include <iostream>

using namespace std;

int answer = 0;

void dfs(vector<int> numbers, int target, int sum, int depth)
{
    if (depth == numbers.size())
    {
        if (sum == target)
        {
            answer++;
        }
        return;
    }
    // 전체 number를 root로 두고 depth를 1씩 증가시켜 트리형식으로 내려감
    // 첫번째 depth 1, -1 
    // 두번째는 1에서 파생된 1+1, 1-1,   -1에서 파생된 -1+1, -1-1....로 노드들을 탐색 
    dfs(numbers, target, sum + numbers[depth], depth + 1);
    dfs(numbers, target, sum - numbers[depth], depth + 1);
}

int solution(vector<int> numbers, int target)
{
    dfs(numbers, target, 0, 0);
    return answer;
}

int main()
{

    vector<int> numbers = {1, 1, 1, 1, 1};

    solution(numbers, 3);

    cout << answer << endl;

    return 0;
}