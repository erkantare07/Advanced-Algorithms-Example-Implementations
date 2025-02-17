# DYNAMIC PROGRAMMING
* Dynamic programming is typically applied to <i>optimization problems.</i>
* An optimal solution to the original problem contains optimal solutions to smaller subproblems.

## Approach
1. Recursively define problem 
2. Determine a set T consisting of all subproblems that have to be solved during the computation of a solution to P.
3. Find an order T0, T1, T2, ... , Tk of the subproblems in T such that during the computation of a solution to Ti only subproblems Tj with j < i are needed.
4. Solve the subproblems in the order T0, T1, T2, ... , Tk and store the solutions in a table.

## Observations
* Due to function call latency, iterative dynamic programming was always faster
* For big numbers, such as len(p) = 1000 for matrix_chain_mult, the recursive approach was not usable due to `RecursionError: maximum recursion depth exceeded in comparison`.