#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
using namespace __gnu_cxx;

string solution(vector<string> participant, vector<string> completion) {
    sort(participant.begin(), participant.end());
    sort(completion.begin(), completion.end());
    
    for(int i=0; i<participant.size(); i++)
        if(participant[i] != completion[i])
            return participant[i];
    return participant[participant.size()-1];
    
}