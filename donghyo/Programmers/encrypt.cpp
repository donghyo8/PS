#include <string>
#include <vector>
#include <iostream>

using namespace std;


// 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

string solution(string s, int n){

    for(int i=0; i<=n; i++){
        if(s[i] != ' ' && s.length()){
            char start = ('A' <= s[i] && s[i] <= 'Z')? 'A':'a';
            s[i] = start + (s[i] + n - start ) % 26;
        }
    }
                return s;
}


int main(){

    string s = "a B z";
    int n = 4;

    cout << n << endl;

    cout << solution(s,n) << endl; 

}