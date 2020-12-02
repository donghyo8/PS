#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

vector<int> answer;
vector<int> temp;

vector<int> solution(vector<int> array, vector<vector<int>> commands)
{

    for(int i=0; i< commands.size(); i++){

        temp.assign(array.begin() + commands[i][0] -1, array.begin() + commands[i][1]);

        sort(temp.begin(), temp.end());

        answer.push_back(temp[commands[i][2] -1]);
    }

    return answer;
}

int main()
{

    vector<int> arr = {1, 5, 2, 6, 3, 7, 4};
    vector<vector<int>> commands = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};

    solution(arr, commands);

    for(int i=0; i<answer.size(); i++) cout << answer[i] << endl;

    return 0;
}