#N*M크기의 얼음틀 구멍 : 0 칸막이가 존재하는 부분 : 1 
#상하좌우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다. 
#이때 얼음틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성
#<입력조건>
#첫째줄 : N,M
#둘째줄 ~M+1줄 : 얼음틀의 형태

N,M = map(int,input().split())
graoh = []
for i in range(n):
  graph.append(list(map(int,input().split()))
#특정한 녿를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):
      
  if x<=-1 or x>=n or y<=-1 or y>=m:
       return False
  if graph[x][y] == 0:
        graph[x][y]=1
               
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y+!)
        dfs(x,y-1)
        return True
   return False
result = 0
for i in range(n):
    for j in range(m):
           if dfs(i,j)==True:
               result+=1
print(result)
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
               
           
