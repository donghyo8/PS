#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(vector<int> numbers, string hand)
{
    string answer = "";
    int leftDistance = 0;
    int rightDistance = 0;
    int leftPosValue = 10;  // * 시작
    int rightPosValue = 12; // # 시작
    int temp1, temp2 = 0;
    
    
    // 1, 4, 7 / 3 ---> 나머지 1 
    // 2, 5, 8, 0 /3 ---> 나머지 2
    // 3, 6, 9, 12 /3 ---> 나머지 0 

    for (int i = 0; i < numbers.size(); i++)
    {

        // 왼쪽 키패드 1, 4, 7 체크
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7)
        {
            answer += "L";
            leftPosValue = numbers[i];
        }
        // 오른쪽 키패드 3, 6, 9 체크
        if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9)
        {
            answer += "R";
            rightPosValue = numbers[i];
        }

        else
        {
            if (numbers[i] == 2 | numbers[i] == 5 | numbers[i] == 8 | numbers[i] == 0)
            {
                if (numbers[i] == 0) 
                {
                    numbers[i] = 11;
                }

                // 가로길이 + 세로길이
                leftDistance = (abs(leftPosValue - numbers[i]) / 3) + (abs(leftPosValue - numbers[i]) % 3);
                rightDistance = (abs(rightPosValue - numbers[i]) / 3) + (abs(rightPosValue - numbers[i]) % 3);

                if (leftDistance < rightDistance)
                {
                    answer += "L";
                    leftPosValue = numbers[i];
                }
                if (leftDistance > rightDistance)
                {
                    answer += "R";
                    rightPosValue = numbers[i];
                }

                if (leftDistance == rightDistance)
                {
                    if (hand == "left")
                    {
                        answer += "L";
                        leftPosValue = numbers[i];
                    }
                    if (hand == "right")
                    {
                        answer += "R";
                        rightPosValue = numbers[i];
                    }
                }
            }
        }
    }

    cout << answer << endl;
    return answer;
}

int main()
{

    vector<int> numbers = {1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5};
    string hand = "right";

    solution(numbers, hand);

    return 0;
}