#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

bool solution(vector<string> phone_book)
{
    bool answer = true;
    for (int i = 0; i < phone_book.size(); i++)
        for (int j = 0; j < phone_book.size(); j++)
            if (i != j && phone_book[i].find(phone_book[j]) == 0)
            {
                answer = false;
                return answer;
            }
    return answer;
}

int main()
{

    vector<string> phone_book1 = {"119", "97674223", "1195524421"};
    vector<string> phone_book2 = {"123", "456", "789"};
    vector<string> phone_book3 = {"12", "123", "1235", "567", "88"};

    solution(phone_book1);
    return 0;
}