# 크루스칼 알고리즘: 최소신장트리(무방향 가중치 그래프에서 가중치의 합의 최소인것을 찾는) 알고리즘 --> Greedy 알고리즘이라 할수 있음

# 1. 간선들의 가중치가 증가하는 순서로 정렬
# 2. 가중치가 가장작은 간선이 사이클을 만들지 않으면 트리 간선으로 선택
# 3. 다음 가중치에서 사이클을 만들지 않으면 트리 간선으로 선택하고 이 과정을 반복하며 정점 -1개의 간선을 선택

def find(u, p):
    # 해당 정점의 최상위 정점을 찾음
    if u != p[u]:
        p[u] = find(p[u], p)

    return p[u]

def union(u, v, p):
    # 두 정점을 연결
    root1 = find(u, p)
    root2 = find(v, p)
    p[root2] = root1 

def Kruskal(n, costs):
    # 가중치로 간선 정렬(인덱스 2인 가중치를 기준으로 오름차순)
    costs.sort(key= lambda x:x[2])
    # 간선 개수 / 가중치 합
    tree_edges, mst_cost = 0, 0 
    # 상호배타적집합: 공통 원소가 없는 원소들에 대한 정보를 저장
    mst = list()
    p = [0]

    for i in range(1, n + 1):
        p.append(i)
    
    while True:
        if tree_edges == n - 1:
            break

        u, v, wt = costs.pop(0)
        print(u, v, wt)

        # u와 v가 서로 다른 집합에 속해 있으면
        if find(u, p) != find(v, p):
            union(u, v, p)
            mst.append([u,v])
            mst_cost += wt
            tree_edges += 1

    print(mst)
    print(mst_cost)
    return(mst_cost)

def solution(n, costs):
    answer = 0

    answer = Kruskal(n, costs)
    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])