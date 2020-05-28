import sys
import time
start_time = time.time()

size=10
halfsize = (size+1)//2

def distance(p1,p2):
    return((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# given a list of points, check to see if all the distances
# between any 2 points are unique.
def checkunique(points):
    ds = set()
    for j in range(0,len(points)-1):
        for i in range(j+1,len(points)):
            d = distance(points[i],points[j])
            if d in ds:
                return False
            else:
                ds.add(d)
    return True


def findunique(size,points=[]):
    #print(points)
    if checkunique(points):
        if len(points)==size:
            return points
    else:
        return False
    lastpoint = points[-1]
    for i in range(lastpoint[0]+1,size):
        res = findunique(size,points+[[i,lastpoint[1]]])
        if res:
            return res
    for j in range(lastpoint[1]+1,size):
        for i in range(0,size):
            res = findunique(size,points+[[i,j]])
            if res:
                return res
    return False

for j in range(0,halfsize):
    for i in range(j,halfsize):
        result = findunique(size,[[i,j]])
        print(i,j,result)

print("--- {0:.3f} seconds ---".format(time.time() - start_time))
