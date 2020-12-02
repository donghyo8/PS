#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {

    map <string, int> m;

    m.insert(make_pair("a", 1));
    m.insert(make_pair("b", 2));
    m.insert(make_pair("c", 3));
    m.insert(make_pair("d", 4));
    m.insert(make_pair("e", 5));
    m.insert(make_pair("f", 6));

    m.erase("d");
    m.erase("e");
    m.erase(m.find("f"));

    if(!m.empty()){
        cout << "m size : " << m.size() << endl;
    }

    cout << "a : " << m.find("a")->second << endl;
    cout << "b : " << m.find("b")->second << endl;

    cout << "a count : " << m.count("a") << endl;
    cout << "b count : " << m.count("b") << endl;

    for(auto i = m.begin(); i != m.end(); i++){
        cout << "key : " << i->first << " " << "value : " << i->second << endl; 
    }

    return 0;
}