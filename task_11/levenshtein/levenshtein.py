
# Wagner-Fischer algorithm to compute Levenshtein distance

import numpy as np


def distance(s1:str, s2:str) -> int:
    m = len(s1)
    n = len(s2)
    d = np.zeros((m+1, n+1), dtype=int)
    for i in range(m):
        d[i+1][0] = d[i][0] + 1 
    for j in range(n):
        d[0][j+1] = d[0][j] + 1 
    for i in range(m): 
        for j in range(n):
            if s1[i] == s2[j]:
                d[i+1][j+1] = d[i][j]
            else:
                d[i+1][j+1] = min(d[i+1][j], d[i][j+1], d[i][j]) + 1
    return d[m][n]

if __name__ == '__main__':
    s1 = 'eqw'
    s2 = 'wqw'
    print(distance(s1, s2))