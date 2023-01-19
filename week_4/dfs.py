# 그래프 표현 (예시)
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

# 재귀를 활용한 dfs
# visited는 현재 방문한 적 있는 요소(노드)인지 판단하기 위한 변수
visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            dfs(visited, graph, neighbor)

dfs(visited, graph, 'A')


