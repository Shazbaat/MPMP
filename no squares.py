import sys
import time
start_time = time.time()

# given a grid of boolean check to see if there are any squares 
# where all 4 corners are either all true or all false
def check4squares(grid):
    for x0 in range(len(grid)-1):
        for y0 in range(len(grid[0])-1):
            for x1 in range(x0+1,len(grid)):
                for y1 in range(y0,y0+x0+1): #this is wrong
                    dx=x1-x0
                    dy=y1-y0
                    if x0-dy < 0: continue  # this is a hack to ignore the wrong coordinates above.
                    if y0+dx+dy >= len(grid[0]): continue  # this is a hack to ignore the wrong coordinates above.
                    #print(x0,y0,x1,y1,dx,dy,len(grid),len(grid[0]))
                    if (grid[x0][y0]==grid[x0+dx][y0+dy]) and \
                       (grid[x0][y0]==grid[x0-dy][y0+dx]) and \
                       (grid[x0][y0]==grid[x0+dx-dy][y0+dy+dx]):
                        return True
    return False

def ppGrid(grid):
    for i in range(len(grid)):
        print(grid[i])
    print()

def findSquareFreeGrid(grid,numpoints,x=-1,y=0):
    #print(points)
    if numpoints == (len(grid)*len(grid[0]))//2:
        if check4squares(grid):
            return False
        else:
            return grid
    for i in range(x+1,len(grid)):
        grid[i][y] = True
        if numpoints==6: 
            ppGrid(grid)
            print("--- {0:.3f} seconds ---".format(time.time() - start_time))
        if findSquareFreeGrid(grid,numpoints+1,i,y):
            return grid
        grid[i][y] = False
    for j in range(y+1,len(grid[0])):
        for i in range(len(grid)):
            grid[i][j] = True
            if numpoints==6: 
                ppGrid(grid)
                print("--- {0:.3f} seconds ---".format(time.time() - start_time))
            if findSquareFreeGrid(grid,numpoints+1,i,j):
                return grid
            grid[i][j] = False
    return False

size=6
grid = [[False for i in range(size)] for j in range(size)]
answer=findSquareFreeGrid(grid,0)
for i in range(len(answer)):
    print(answer[i])

print("--- {0:.3f} seconds ---".format(time.time() - start_time))
