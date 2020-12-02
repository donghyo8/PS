#include <iostream>
#include <queue>

using namespace std;

int main() {
    queue <int> test;

    test.push(1);
    test.push(3);
    test.push(2);
    test.push(6);

    cout << "size :" << test.size() << endl;
    cout << "front :" << test.front() << endl;
    cout << "back :" << test.back() << endl;

    while ( !test.empty()){
        cout << test.front() << " ";
        test.pop();
    }

    cout << endl;

}