dx =(1,-1,0,0)
dy = (0,0,-1,1)
def valido(x, y, n, m):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False
    return True

def dfs(x,y,g,c,d,n,m):
    if g[x][y]!='.':
        return x==c and y==d
    g[x][y]='X'
    for i in range(4):
        siguiente_x = x+dx[i]
        siguiente_y = y+dy[i]
        if valido(siguiente_x, siguiente_y, n, m):
            if dfs(x+dx[i],y+dy[i],g,c,d,n,m):
                return True
    return False


n, m = map(int,input().split())
g=[]
for i in range(n):
    g.append([char for char in input()])
a, b, = map(int,input().split())
a, b = a-1, b-1
c, d = map(int,input().split())
c, d = c-1, d-1

g[a][b]='.'
if dfs(a,b,g,c,d,n,m):
    print("YES")
else:
    print("NO")