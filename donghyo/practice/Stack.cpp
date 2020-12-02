#include <iostream>
#include <stack>

using namespace std;

int main(){
    stack<int> sta;

    sta.push(3);
    sta.push(2);
    sta.push(1);

    cout << "top element : " << sta.top() << "\n";

    sta.pop(); sta.pop();

    cout << "stack size : " << sta.size() << "\n";
    cout << "is it empty? : " << (sta.empty() ? "yes" : "no") << "\n"; 
}