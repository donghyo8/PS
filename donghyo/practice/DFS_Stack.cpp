#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>


using namespace std;

void Dfs(int start, vector<int> graph[], bool check[]) {
    stack <int> sta;

    sta.push(start); // start : index
    check[start] = true;

    while(!sta.empty()){
        int current_Node = sta.top();
        sta.pop();

        for(int i=0; i<graph[current_Node].size(); i++){

            int next_Node = graph[current_Node][i];

            if(check[next_Node] == false){
                check[next_Node] = true;
                sta.push(current_Node);
				sta.push(next_Node);
				break;
            }


        }

    }

}

int main(){

}