#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

stack<int> bascket;
int answer = 0;

int solution(vector<vector<int>> board, vector<int> moves)
{
    int temp = 0;

    for (int i = 0; i < moves.size(); i++)
    {
        temp = moves[i] - 1; // 크레인을 세로로 움직인다고 보며 1부터 시작

        for (int j = 0; j < board.size(); j++)
        {
            if (board[j][temp] != 0) // board에 인형이 있는지 확인하기 위해 바닥 확인
            {
                if (!bascket.empty() && bascket.top() == board[j][temp])
                { // 기존 bascket에 담긴 인형과 끄집어내려는 인형과 같으면 인형을 없애고 카운트 증가
                    bascket.pop();
                    answer += 2;
                }
                else
                {
                    // 스택에 인형 담기
                    bascket.push(board[j][temp]);
                }
                // 인형을 삭제하고 루프 빠져나감
                board[j][temp] = 0;
                break;
            }
        }
    }

    cout << "return : " << answer << endl;
    return answer;
}

int main()
{

    vector<vector<int>> board = {{0, 0, 0, 0, 0}, {0, 0, 1, 0, 3}, {0, 2, 5, 0, 1}, {4, 2, 4, 4, 2}, {3, 5, 1, 3, 1}};
    vector<int> moves = {1, 5, 3, 5, 1, 2, 1, 4};

    solution(board, moves);

    return 0;
}