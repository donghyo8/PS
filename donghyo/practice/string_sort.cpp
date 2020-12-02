#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <string> 

using namespace std;

int num;

bool compare(string a, string b){

    if(a[num] == b[num]){
        return a < b;
    }
    else{
        return a[num] < b[num];
    }
}


vector<string> solution(vector<string> strings, int n) {
    num = n;

    sort(strings.begin(), strings.end(), compare);
    return strings;

}

// 3항연산자
// bool compare (string a, string b) {
//     return a[num] == b[num] ? a < b : a[num] < b[num];
// }

// vector<string> solution(vector<string> strings, int n) {
//     num = n;
//     sort (strings.begin(), strings.end(), compare);
//     return strings;
// }


int main() {

}