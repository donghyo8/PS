#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(vector<string> seoul) {
    string answer = "";
    answer += "김서방은 ";

    for(int i=0; i<seoul.size(); i++){
        if(seoul.size() <=1000 && seoul[i].size() <=20 ){
            if(seoul[i] == "Kim"){
                answer += to_string(i);
            }

        }
    }
    answer += "에 있다";

    return answer;
}

int main(){
    vector<string> seoul = {"Kim", "Jane"};

    solution(seoul);

}