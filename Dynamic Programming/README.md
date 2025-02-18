# DYNAMIC PROGRAMMING
* Dynamic programming is typically applied to <i>optimization problems.</i>
* An optimal solution to the original problem contains optimal solutions to smaller subproblems.

## Approach
1. Recursively define problem 
2. Determine a set T consisting of all subproblems that have to be solved during the computation of a solution to P.
3. Find an order T0, T1, T2, ... , Tk of the subproblems in T such that during the computation of a solution to Ti only subproblems Tj with j < i are needed.
4. Solve the subproblems in the order T0, T1, T2, ... , Tk and store the solutions in a table.

## Observations
* Due to function call latency, iterative approach was usually faster. However, in cases where we don't need to calculate the whole memo table to solve the problem at hand, such as in subset sum, then memoization was faster than iterative approach.
* For big numbers, such as len(p) = 1000 for matrix_chain_mult, the recursive approach was not usable due to `RecursionError: maximum recursion depth exceeded in comparison`.


## Personal Notes on runtime calculation
* Cost of calculating the memory table

## Examples
*=> if split location doesn't matter (just split in 2 halves) and subproblems can be merged to get the solution of the bigger problem without having the need of looking into other subproblem combinations then go with **divide and conquer***

**fibonacci:** there is no list that we can split into subproblems. We need to know the -1 and -2 cases. The recursion tree is not a balanced tree anymore (depth is not logn for all leaf nodes). D&C might be expensive. However, we solve the same subsubproblems for different subproblems. We can store them and use them as scalars after computing it once. For fibonacci numbers up to n, we need a lookup table of size n or running values of last 2 fib. numbrs. With that every fib num can be calculated in O(1). For n numbers we got the runtime of O(n).
*=> no exhaustive search is needed. Just remember constant number of prev. states*

**matrix chain:** we can split the problem in halves and solve the atomic problems but *where we split matters* and all splits should be considered therefore splitting only in halves won't solve this. For matrix chain multiplication, the optimal cost for multiplying matrices from A₁ to Aₙ depends on finding the best split point k, and that optimal split can occur anywhere between 1 and n−1—not necessarily in the middle. This means you must evaluate each potential k because the scalar multiplication cost p[i−1]·p[k]·p[j] ties the two subproblems together. A fixed split into two halves would ignore many possible k values and thus could miss the optimal arrangement. Which is why dynamic programming-with its exhaustive consideration of splits and memoization to avoid redundant calculations—is essential for this problem. O(n^3)
*=> exhaustive search where all items are needed and split location matters*

**subset sum / knapsack:** this also lacks a simple "merge" step. We need an exhaustive search for each element being present or not. Looking at splits won't work here because we don't have to include all items in the list as it was the case for matrix chain problem. There will be repeated subproblems, hence memoization. O(n * maxW)
*=> exhaustive search where a subset is needed*

**weighted interval scheduling:** if not weighted greedy based on deadline but weighted needs exhaustive search and can be solved exactly like knapsack problem.
