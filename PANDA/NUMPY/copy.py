import numpy as np
arr=np.array([1,2,3,4,5])
# x=arr.view()#copy()
x=arr.view()
y=arr.copy()

print(x.base)
print(y.base)