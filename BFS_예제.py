#N*M크기의 직사각형 미로 
#초기 위치 : (1,1)
#미로의 출구 : (N,M)
#괴물이 있는 부분 : 0, 괴물이 없는 부분 : 1
#탈출하기 위해 움직여야 하는 칸의 최소 개수
#<입력조건>
#첫째줄 : N,M
#둘째줄~N+1 : 각각 M개의 정수(미로의 정보)
from collections import deque

n,m = map(int,input().split())
graph = []
for i in range(n):
  graph.append(list(map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  while queue:
     x,y = queue.popleft()
     for i in range(4):
         nx = x + dx[i]
         ny = y + dy[i]
         if nx<0 or nx>=n or ny<0 or ny>=m:
             continue
         if graph[nx][ny]==0:
             continue
         if graph[nx][ny]==1:
              graph[nx][ny] += graph[x][y]+1
              queue.append((nx,ny))
   return graph[n-1][m-1]
print(bfs(0,0))
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                 
                     
