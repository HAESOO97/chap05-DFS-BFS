-그래프 구현 방법-
1)인접행렬(Adgacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식,2차원 배열에 각 노드가 연결된 형태를 기록하는 방식

INF = 99999999 #무한의 비용 선언
#2차원 리스트를 이용해 인접행렬 표현
graph = [[0,7,5],[7,0,INF],[5,INF,0]]
print(graph)

2)인접리스트(Adjacency List) : 리스트로 그래프의 연결관계를 표현 하는 방식, 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
  
 #행(ROW)이 3개인 2차원 리스트로 인접리스트로 표현
graph = [[] for _ in range(3)]
#노드 0에 연결된 노드 정보 저장(노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장((노드,거리))
graph[1].append((0,7))

#노드 2에 연결된 노드정보 저장((0,5))
graph[2].append((0,5))
print(graph)

<DFS>
Depth-First Search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘,스택 자료구조 이용
-DFS 예제

def dfs(graph,v,visited):
  #현재노드를 방문처리
  visited[v] = True
  print(v,end='')
  #현재노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)
      
graph = [[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7],
]
visited = [False]*9
dfs(graph,1,visited)





















