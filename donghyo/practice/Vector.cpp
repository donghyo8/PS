#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> v;

    v.push_back(10);
    v.push_back(20);
    v.push_back(30);
    v.push_back(40);

    for (vector<int>::size_type i = 0; i < v.size(); i++)
    {
        cout << "vec의" << i + 1 << "번째 원소 ::" << v[i] << endl;
    }
}