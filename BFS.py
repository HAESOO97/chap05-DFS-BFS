<BFS>
:너비우서 탐색, 가까운 노드부터 탐색하는 알고리즘, 큐자료구조 이용
 
<동작원리>
1)탐색시작노드를 큐에 삽입하고 방문처리를 한다.
2)큐에서 노드를 꺼내 해당 노드이 인접 노드중에서 방문하지 않은 노드를 큐에 삽입하고 방문 처리를 한다.
3)2번 노드를 더이상 수행할 수 없을 때까지 반복한다.

<예제>
from collections import deque
def bfs(graph,start,visited):
  queue = deque(start)
  #현재 노드를 방문처리
  visited[start] = True
  #큐가 빌때까지 반복
  while queue:
    #큐에서 하나의 원소를 뽑아 출력
    v = queue.popleft()
    print(v,end='')
    #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited = True
        
graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

visited = [False]*9

bfs(graph,1,visited)
  
  
  
  
  
  
  
  
  
