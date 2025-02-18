# Subset Sum Problem
# Given a set of non-negative integers, and a value sum, find a subset of the given set with the closest sum to the given sum.

import random

# recursion => O(2^n)
# recursion with memoization => O(n*target) because there are n*target subproblems and each subproblem is solved once
def recursive_subset_sum(W, Wmax, n, use_memoization=False): # W is the set of non-negative integers, target is the sum to be achieved, n is the number of elements in the set
    M = [[[] for _ in range(Wmax+1)] for _ in range(n+1)] # memo[n][target] will store the subset with sum closest to target for the first n elements of W

    def recur(W, target, n):
        if target <= 0 or n == 0:
            return []

        if use_memoization and M[n][target]:
            return M[n][target]

        if W[n-1] > target:
            return recur(W, target, n-1) # exclude the current element

        exclude = recur(W, target, n-1) # exclude the current element
        include = [W[n-1]] + recur(W, target - W[n-1], n-1) # include the current element

        best = max(exclude, include, key=sum)
        M[n][target] = best
        return best

    return recur(W, Wmax, n)


# iterative => O(n*target)
# This computes the whole M table but recursive_subset_sum only computes the necessary subproblems.
# Therefore this is slower than recursive_subset_sum although recursive approach has the overhead of function calls.
def iterative_subset_sum(W, Wmax, n):
    M = [[[] for _ in range(Wmax+1)] for _ in range(n+1)] # M[n][target] will store the subset with sum closest to target for the first n elements of W

    for i in range(n+1):
        M[i][0] = [] # if Wmax is 0, then the subset is empty
    
    for i in range(1, n+1):
        for j in range(1, Wmax+1):
            if W[i-1] > j:
                M[i][j] = M[i-1][j]
            else:
                exclude = M[i-1][j]
                include = [W[i-1]] + M[i-1][j - W[i-1]]
                M[i][j] = max(exclude, include, key=sum)
    
    return M[n][Wmax]


def demo_subset_sum():
    W = [random.randint(1, 20) for _ in range(90)]
    target = 1033

    import time

    time_start = time.time()

    subset = iterative_subset_sum(W, target, len(W))
    print("Subset with sum closest to target: ", subset)
    print("Sum of subset: ", sum(subset))

    end = time.time()
    print("Time taken with iteration: ", end-time_start)

    time_start = time.time()

    subset = recursive_subset_sum(W, target, len(W), use_memoization=True)
    print("Subset with sum closest to target: ", subset)
    print("Sum of subset: ", sum(subset))

    end = time.time()
    print("Time taken with memoization: ", end-time_start)

    # time_start = time.time()

    # subset = recursive_subset_sum(W, target, len(W), use_memoization=False)
    # print("Subset with sum closest to target: ", subset)
    # print("Sum of subset: ", sum(subset))

    # end = time.time()
    # print("Time taken without memoization: ", end-time_start)

# O(n*Wmax) time complexity
def knapsack(W, V, Wmax, n):
    M = [[[] for _ in range(Wmax+1)] for _ in range(n+1)] # memo[n][target] will store the subset with sum closest to target for the first n elements of W

    def recur(W, target, n):
        if target <= 0 or n == 0:
            return []

        if M[n][target]: # memoization
            return M[n][target]

        if W[n-1] > target: # if not enough space for the current element
            return recur(W, target, n-1) # exclude the current element

        exclude = recur(W, target, n-1) # exclude the current element
        include = [(W[n-1], V[n-1])] + recur(W, target - W[n-1], n-1) # include the current element

        best = max(exclude, include, key=lambda x: sum([v for _, v in x]))
        M[n][target] = best
        return best

    return recur(W, Wmax, n)
    

if __name__ == "__main__":
    # demo_subset_sum()

    W = [random.randint(1, 20) for _ in range(10)]
    V = [random.randint(1, 20) for _ in range(10)]
    Wmax = 50
    print("Weights:", W)
    print("Values:", V)
    print("Max weight:", Wmax)
    result = knapsack(W, V, Wmax, len(W))
    total_value = sum(v for _, v in result)
    total_weight = sum(w for w, _ in result)
    print("Selected items (weight, value):", result)
    print("Total value:", total_value)
    print("Total weight:", total_weight)
