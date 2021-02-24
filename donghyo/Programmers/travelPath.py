from collections import deque

def solution(tickets):
    answer, visited = list(), list()
    stack = deque()
    dic = dict()

    tickets.sort(reverse=True)

    for key, value in tickets:
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]

    stack.append("ICN")

    while stack:
        node = stack[-1]
        print(node)

        if node not in dic or len(dic[node]) == 0:
            visited.append(stack.pop())
        else:
            stack.append(dic[node].pop())
    
    visited.reverse()
    answer = visited
    print(answer)

    return answer

tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets2)