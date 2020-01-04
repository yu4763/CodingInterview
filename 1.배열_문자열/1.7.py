import numpy as np
import math

if __name__ == '__main__':
    n = list(input().split())
    m = int (math.sqrt(len(n)))

    n = np.asarray(n).reshape(m, m)

    print(n)

    for i in range(int(math.ceil(m/2))):

        for k in range(i, m-1-i):
            t = n[i][k]
            n[m-1-k][i], n[i][k] = n[i][k], n[m-1-k][i]
            n[m-1-i][m-1-k], n[m-1-k][i] = n[m-1-k][i], n[m-1-i][m-1-k]
            n[k][m-1-i], n[m-1-i][m-1-k] =  n[m-1-i][m-1-k], n[k][m-1-i]
            n[k][m-1-i] = t


    print(n)
