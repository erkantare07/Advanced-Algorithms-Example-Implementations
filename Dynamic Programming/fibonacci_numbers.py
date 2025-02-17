# Fibonacci Numbers: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...

# Iterative version
# Linear time & Linear space
def fib_nums_v1(n):
    fib_nums = [0, 1]
    for i in range(2, n+1):
        fib_nums.append(fib_nums[i-1] + fib_nums[i-2])
    return fib_nums[n]

# Iterative Optimized version
# Linear time & Constant space
def fib_nums_v2(n):
    second_last, last = 0, 1
    for i in range(2, n+1):
        second_last, last = last, second_last + last
    return last

# Recursive with memoization
# Linear time & Linear space
def fib_nums_v3(n):
    fib_nums = [float('-inf')] * (n+1) # +1 because we need to store the 0 and first element 1
    fib_nums[0], fib_nums[1] = 0, 1

    def _lookupfib(n):
        if fib_nums[n] > float('-inf'):
            return fib_nums[n]
        
        fib_nums[n] = _lookupfib(n-1) + _lookupfib(n-2)
        return fib_nums[n]
    
    return _lookupfib(n)


if __name__ == "__main__":
    print(fib_nums_v3(10)) # 55