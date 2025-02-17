# Given: Sequence (chain) of matrices' dimensions p0, p1, ..., pn where matrix Ai has dimensions p[i-1] x p[i]
# Goal: Compute the minimum number of scalar multiplications needed to compute the product of the matrices in the given order and where to put the parentheses

import random

# func(p, 1, n)
# T(1) >= 1 (at least one comparison)
# T(n) >= 1 + sum_{k=1}^{n-1}(T(k) + T(n-k) + 1) >= n + 2*sum_{k=1}^{n-1} T(k) 
# => T(n) >= 3^{n-1}
# Exponential time complexity
# With memoization, we can reduce the time complexity to O(n^3) because there are O(n^2) table entries that are computed once and each entry is looked up at most 2n times since mij is looked up by m_ab where a=i and b>j OR a<i and b=j.
def recursive_mat_chain(p, i, j, use_memoization=False):
    # m[i][j] will store the number of min scalar mult. for multiplying matrices from Ai to Aj (incl.)
    m = [[float('inf') for _ in range(len(p))] for _ in range(len(p))] # length is num of matrices + 1 although we dont have a matrix 0 but for compatbility with the dimensions array
    s = [[float('-inf') for _ in range(len(p))] for _ in range(len(p))] # s[i][j] will store the value of k at which the optimal split occurs for multiplying matrices from Ai to Aj (incl.)

    def recur(i,j):
        if i == j: # base case - one matrix no multiplication needed
            return 0
        if use_memoization and m[i][j] < float('inf'): # already computed
            return m[i][j]
        for k in range(i, j):
            q = m[i][j]
            m[i][j] = min(
                m[i][j], 
                recur(i, k) + recur(k+1, j) + p[i-1]*p[k]*p[j] # Ai's first dim X Ak's second dim X Aj's second dim - because _recur(i,k) will give the min scalar mult. for multiplying matrices from Ai to Ak (incl.) hence the resulting matrix will have dimensions p_{i-1} X p_k. Similarly, resulting matrix from mult. A_{k+1} to Aj will have dimensions p_k X p_j
                )
            if m[i][j] < q:
                s[i][j] = k
        return m[i][j]
    
    return recur(i,j), s


def iterative_mat_chain(p):
    n = len(p) - 1 # number of matrices
    m = [[float('inf') for _ in range(n+1)] for _ in range(n+1)] # +1 is again for compatibility with the dimensions array p
    for i in range(n+1):
        m[i][i] = 0
    s = [[float('-inf') for _ in range(n+1)] for _ in range(n+1)] # s[i][j] will store the value of k at which the optimal split occurs for multiplying matrices from Ai to Aj (incl.)

    # first start with smaller chains and build up to the larger chains. This is important because we need smaller chains to compute the larger chains.
    for l in range(2, n+1): # l is the chain length
        for i in range(1, n-l+2): # i is the starting matrix
            j = i+l-1 # j is the ending matrix
            for k in range(i, j):
                q = m[i][j] 
                m[i][j] = min(
                    m[i][j],
                    m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                )
                if m[i][j] < q:
                    s[i][j] = k
    return m[1][n], s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j]+1, j)
        print(")", end="")
    

if __name__ == '__main__':
    # p0, p1, ..., pn where matrix Ai has dimensions p[i-1] x p[i]

    dimensions = [10,100,5,50] #[random.randint(1, 100) for _ in range(10+1)]

    import time

    start = time.time()
    n_mult, splits = recursive_mat_chain(dimensions, 1, len(dimensions)-1, use_memoization=True)
    end = time.time()
    print("Time taken with recursive memoization: ", end-start)

    start = time.time()
    n_mult2, splits2 = iterative_mat_chain(dimensions)
    end = time.time()
    print("Time taken with iterative: ", end-start)

    # start = time.time()
    # print(recursive_mat_chain(dimensions, 1, len(dimensions)-1))
    # end = time.time()
    # print("Time taken with recursive without memoization: ", end-start)

    print(dimensions)
    print_optimal_parenthesization(splits, 1, len(dimensions)-1)
    print("\nNumber of scalar multiplications: ", n_mult)

    