#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(string s) {
    int answer = 0;

    if(s.length() >= 1 & s.length() <= 5){
        if(s[0] != '0'){

            return stoi(s);

        }
        else{
            return 0;
        }
    }

    return answer;
}

int main(){

    string s =  {"1234"};

    solution(s);

    return 0;
}