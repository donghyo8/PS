#include <string>
#include <vector>
#include <iostream>
#include <math.h>

using namespace std;

vector<int> solution(int brown, int red)
{
    vector<int> answer;
    int sum = brown + red;
    int limit = (int)sqrt(sum);

    for (int i = 3; i <= limit; i++)
    {
        if (sum % i == 0)
        {
            int tmp = sum / i;
            //전체 카펫 위,아래 row 왼쪽,오른쪽 col을 제외하고 곱하면 red타일의 갯수가 나온다.
            if ((tmp - 2) * (i - 2) == red)
            {
                answer.push_back(tmp);
                answer.push_back(i);
                break;
            }
        }
    }
    return answer;
}

solution(10,2)