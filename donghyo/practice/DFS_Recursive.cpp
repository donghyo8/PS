#include <iostream>
#include <vector>
using namespace std;
 
int n, m, v; // n: vertext(정점)의 개수, m: edge(간선)의 개수, v: 정점의 번호
vector<vector<int>> adj; //vector-vector를 선언
vector<bool> visited; // node의 방문 여부

int start, end; // start: 시작지점, end: 끝지점

void dfs_recursive(int node){
    visited[node] = true; // dfs 함수에 들어오면, node의 방문 여부를 체크
    cout << node << endl; // 방문한 노드 값 출력

    for(int i=0; i<adj[node].size(); i++){
        int next = adj[node][i]; // adj[node][i] : vector의 [node]번째 내의 i번째 인자

        if(visited[next] == false){
            dfs_recursive(next);
        }
    }
}

void dfs_stack(){
    
}


 
int main() {

}
