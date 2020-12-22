#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<vector<string>> clothes)
{
    int answer = 0;
    string temp = "";
    map<string, int> clothesMap;

    for (int i = 0; i < clothes.size(); i++)
    {
        temp = clothes[i][1];
        clothesMap[temp]++;
    }

    for (auto itr = clothesMap.begin(); itr != clothesMap.end(); itr++)
    {
        // cout << itr->first << " " << itr->second << endl;
        answer += (answer + 1) * itr->second;
    }
    cout << answer << endl;
    return answer;
}

int main()
{

    vector<vector<string>> clothes1 = {{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"}, {"green_turban", "headgear"}};
    vector<vector<string>> clothes2 = {{"crow_mask", "face"}, {"blue_sunglasses", "face"}, {"smoky_makeup", "face"}};

    solution(clothes1);
}