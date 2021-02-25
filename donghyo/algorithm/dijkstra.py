import heapq

graph = {
    'A': {'B': 8, 'C':1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5},
}

def dijkstra(graph, start):
   # start로 부터의 거리 값을 저장하기 위함
  distances = {node: float('inf') for node in graph}  
  print(distances)
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
   # 시작 노드부터 탐색 시작 하기 위함
  heapq.heappush(queue, [distances[start], start]) 
  print([distances[start], start])

  while queue: # queue에 남아 있는 노드가 없으면 끝
     # 탐색 할 노드, 거리를 가져옴
    current_distance, current_destination = heapq.heappop(queue) 
    print(distances[current_destination], current_distance)
     # 기존에 있는 거리보다 길다면, 볼 필요도 없음
    if distances[current_destination] < current_distance: 
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
       # 해당 노드를 거쳐 갈 때 거리
      distance = current_distance + new_distance  
      print(new_destination,new_distance )
       # 알고 있는 거리 보다 작으면 갱신
      if distance < distances[new_destination]:  
        distances[new_destination] = distance
         # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        heapq.heappush(queue, [distance, new_destination])  
    
  print(distances)
  return distances

print(dijkstra(graph, 'A'))
