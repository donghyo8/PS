#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<string> solution(int n, vector<int> arr1, vector<int> arr2)
{

    vector<string> answer(n);

    for (int i = 0; i < n; i++)
    {

        // ex. temp <- 0101 | 0110 
        int temp = arr1[i] | arr2[i];
        answer[i].assign(" ", n);
        cout << temp << " ";

        for (int j = n - 1; j >= 0; j--)
        {
            if (temp % 2 == 0)
                answer[i][j] = ' ';
            else
                answer[i][j] = '#';
            temp /= 2;
        }
    }
    cout << endl;

    for (int i = 0; i < answer.size(); i++)
    {
        cout << answer[i];
    }
    cout << endl;

    return answer;
}

int main()
{

    int n = 5;
    vector<int> arr1 = {9, 20, 28, 18, 11};
    vector<int> arr2 = {30, 1, 21, 17, 28};

    solution(n, arr1, arr2);

    return 0;
}
