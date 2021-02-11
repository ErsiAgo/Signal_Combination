#
import numpy as np
from itertools import combinations

a = np.array([[2,4,6,8,10,12],[1,3,5,8,10,12],[0,1,2,8,10,12],[4,5,6,8,10,12]])

def rSubset(arr, r):
    return list(combinations(arr, r))

# Function
if __name__ == "__main__":
    arr = a
    r = 2

comb_matrix = (rSubset(arr, r))
#print(comb_matrix)

comb_matrix_2 = np.array(comb_matrix)
print(comb_matrix_2)
m = comb_matrix_2.shape
#print(m)
o = comb_matrix_2[0,0]
p = comb_matrix_2[0,1]
q = comb_matrix_2[1,0]
s = comb_matrix_2[1,1]
#print(m)
print('---------------------------')
#print(o)
#print(p)
#print(q)
#print(s)
def combination():
    for m in range(comb_matrix_2.shape[0]):
        #for n in range(comb_matrix_2.shape[1]):
            print(comb_matrix_2[m,0])
            print(comb_matrix_2[m,1])
            #print(m,0)
            #print(m)
combination()







