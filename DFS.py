<DFS>
Depth-First Search, 깊이 우선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

-그래프 구현 방법-
1)인접행렬(Adgacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식

INF = 99999999 #무한의 비용 선언
#2차원 리스트를 이용해 인접행렬 표현
graph = [[0,7,5],[7,0,INF],[5,INF,0]]
print(graph)