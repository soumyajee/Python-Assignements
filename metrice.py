import numpy as np
def rotate_zigzag(n):
    metrics=np.zeros((n,n),dtype=int)
    val=1
    for s in range(2*n-1):
        if s%2==0:
            x=min(s,n-1)
            y=s-x
            while x>=0 and y<n:
                metrics[x][y]=val
                val=val+1
                x=x-1
                y=y+1
        else:
            y=min(s,n-1)
            x=s-y
            while y>=0 and x<n:
                metrics[x][y]=val
                val=val+1
                x=x+1
                y=y-1
    return metrics
n=3
print(rotate_zigzag(3))                    
