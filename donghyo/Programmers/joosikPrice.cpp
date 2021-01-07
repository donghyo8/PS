#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

vector<int> solution(vector<int> prices)
{
    vector<int> answer;
    int price = 0;
    for (int i = 0; i < prices.size(); i++)
    {
        int price = 0;
        for (int j = i + 1; j < prices.size(); j++)
        {
            if (prices[j] >= prices[i])
                price++;
            else
            {
                price++;
                break;
            }
        }
        answer.push_back(price);
    }
    return answer;
}

int main()
{

    vector<int> prices = {1, 2, 3, 2, 3};

    solution(prices);

    return 0;
}