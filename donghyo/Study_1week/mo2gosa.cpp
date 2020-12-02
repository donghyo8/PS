#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

// 수포자가 찍는 패턴
int test1[5] = {1, 2, 3, 4, 5};
int test2[8] = {2, 1, 2, 3, 2, 4, 2, 5};
int test3[10] = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};

vector<int> solution(vector<int> answers)
{
    vector<int> answer;
    
    int score[3] = {
        0,
    };
    
    int max_score = 0;

    // 각 수포자마다 점수 카운트
    for (int i = 0; i < answers.size(); i++)
    {
        if (answers[i] == test1[i % 5])
            score[0] += 1;
        if (answers[i] == test2[i % 8])
            score[1] += 1;
        if (answers[i] == test3[i % 10])
            score[2] += 1;
    }

    max_score = max(max(score[0], score[1]), score[2]);

    for (int i = 0; i < 3; i++)
    {
        if (score[i] == max_score)
            answer.push_back(i + 1);
    }

    return answer;
}
int main()
{

    vector<int> answers = {1, 2, 3, 4, 2};
    solution(answers);

    return 0;
}