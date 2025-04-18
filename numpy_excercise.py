import numpy as np
metrics=np.array([[1,2,3],
                  [4,5,6],
                  [8,9,10]])
print(metrics)
transpose=np.rot90(metrics,-1)
print(transpose)
reverse=np.transpose(metrics)[::-1]
print(reverse)
x=np.where(metrics%2==0,"even","odd")
print(x)

