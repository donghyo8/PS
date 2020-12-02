#include <string>
#include <vector>
#include <iostream>
#include <stack>

using namespace std;

bool check(string str){
    int len = (int)str.length();
    stack<char> st;
    for(int i=0; i<len; i++){
        char c = str[i];

        if((c == '(') || (c== '[') || (c== '{') || (c== '<')){
            st.push(str[i]);

        }else{
            if(!st.empty()){
                st.pop();
            }
            else{
                return false;
            }
        }
    }
    return st.empty();
}

int solution(string inputString) {
    int answer = -1;
    int len = (int)inputString.length();

    for(int i=0; i<=len; i++){
        if(check(inputString)){
            answer += 1;
        }
}
    return answer;
}


int main(){

    string s = "line [plus]";

    cout << solution(s) << endl;

}