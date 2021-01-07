#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int m, int n, vector<string> board)
{
    int answer = 0;
    vector<vector<string>> map;
    // string lion = "R", moozi = "M", apeach = "A", frodo = "F",
    //        neo = "N", tube = "T", jazi = "J", corn = "C";

    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << map[i][j] << endl;
        }
    }
    return answer;
}

int main()
{
    int m = 6;  
    int n = 6;   
    vector<string> board = {"TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"}; 

    solution(m, n, board);

    return 0;
}

// 라이언(R), 무지(M), 어피치(A), 프로도(F), 네오(N), 튜브(T), 제이지(J), 콘(C)