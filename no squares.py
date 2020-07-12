import sys
import time
import copy
start_time = time.time()

debug = -1
findAll = True
numsolutions = 0
allSolutions = []
anyRatio = True
# given a grid of boolean check to see if there are any squares 
# where all 4 corners are either all true or all false
def check4squares(grid,checkTrueOnly=False):
    for x0 in range(len(grid)-1):
        for y0 in range(len(grid[0])-1):
            for x1 in range(x0+1,len(grid)):
                for y1 in range(y0,y0+x0+1): #this is wrong
                    dx=x1-x0
                    dy=y1-y0
                    if x0-dy < 0: continue  # this is a hack to ignore the wrong coordinates above.
                    if y0+dx+dy >= len(grid[0]): continue  # this is a hack to ignore the wrong coordinates above.
                    #print(x0,y0,x1,y1,dx,dy,len(grid),len(grid[0]))
                    if checkTrueOnly:
                        if grid[x0][y0] and grid[x0+dx][y0+dy] and \
                           grid[x0-dy][y0+dx] and \
                           grid[x0+dx-dy][y0+dy+dx]:
                            return True
                    else:
                        if (grid[x0][y0]==grid[x0+dx][y0+dy]) and \
                           (grid[x0][y0]==grid[x0-dy][y0+dx]) and \
                           (grid[x0][y0]==grid[x0+dx-dy][y0+dy+dx]):
                            return True
    return False

# Pretty print the grid
def ppGrid(grid):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            print("{0:>5s} ".format(str(grid[j][i])), end='')
        print()
    print()

def findSquareFreeGrid(grid,numpoints,x=-1,y=0,findAll=False):
    global allSolutions
    global numsolutions
    #print(points)
    if numpoints == (len(grid)*len(grid[0]))//2 or anyRatio:
        if check4squares(grid):
            if not anyRatio:
                return False
        else:
            numsolutions += 1
            ppGrid(grid)
            allSolutions.append(copy.deepcopy(grid))
            if not findAll and not anyRatio:
                return grid
            elif not anyRatio:
                return False
    if numpoints>=4 and check4squares(grid,True):
        return False
    for i in range(x+1,len(grid)):
        grid[i][y] = True
        if numpoints==debug: 
            print(numsolutions)
            ppGrid(grid)
            print("--- {0:.3f} seconds ---".format(time.time() - start_time))
        if findSquareFreeGrid(grid,numpoints+1,i,y,findAll):
            return grid
        grid[i][y] = False
    for j in range(y+1,len(grid[0])):
        for i in range(len(grid)):
            grid[i][j] = True
            if numpoints==debug: 
                print(numsolutions)
                ppGrid(grid)
                print("--- {0:.3f} seconds ---".format(time.time() - start_time))
            if findSquareFreeGrid(grid,numpoints+1,i,j,findAll):
                return grid
            grid[i][j] = False
    return False

def stackSolutions(allSolutions, stackedSolutions):
    for i in range(len(allSolutions)):
        if i%100==0:
            print(i,"--- {0:.3f} seconds ---".format(time.time() - start_time),flush=True)
        for j in range(len(allSolutions)):
            grid = allSolutions[i] + allSolutions[j]
            #print(grid)
            if not check4squares(grid):
                stackedSolutions.append(grid)


M=6
N=3
grid = [[False for i in range(M)] for j in range(N)]
answer=findSquareFreeGrid(grid,0,-1,0,findAll)
#print(allSolutions)
print(numsolutions)
stackedSolutions=[]
stackSolutions(allSolutions,stackedSolutions)
for solution in stackedSolutions:
    ppGrid(solution)
print(len(stackedSolutions))
#for i in range(len(answer)):
#    print(answer[i])

print("--- {0:.3f} seconds ---".format(time.time() - start_time))
print(check4squares([[False,False,True],[False,True,True],[False,False,True]]))
