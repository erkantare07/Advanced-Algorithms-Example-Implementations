# Find the maximum sum of a subarray in a list of numbers (incl. start and end indices of the subarray)

import random

A = [random.randint(-100, 100) for _ in range(10)]
print(A)

# Maximum Sum using Kadane's Algorithm => O(n)
def max_sum_kadane(A):
    running_sum = sum_max = A[0]
    start = end = start_max = end_max = 0
    for i in range(1, len(A)):
        if running_sum < 0:
            running_sum = 0
            start = i
    
        running_sum += A[i]
        end = i
        
        if running_sum > sum_max:
            sum_max = running_sum
            start_max = start
            end_max = end

    return sum_max, start_max, end_max

# O(nlogn)
def max_sum_dq_slow(A, l, r):
    if l == r:
        return A[l], l, r

    m = (l + r) // 2
    # divide
    left_sum, left_start, left_end = max_sum_dq_slow(A, l, m)
    right_sum, right_start, right_end = max_sum_dq_slow(A, m + 1, r)
    
    # merge
    cross_sum, cross_start, cross_end = max_cross_sum(A, l, m, r)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_start, left_end
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_start, right_end
    else:
        return cross_sum, cross_start, cross_end
    
def max_cross_sum(A, l, m, r):
    left_sum = float('-inf')
    sum_ = 0
    for i in range(m, l - 1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            left_max = i

    right_sum = float('-inf')
    sum_ = 0
    for i in range(m + 1, r + 1):
        sum_ += A[i]
        if sum_ > right_sum:
            right_sum = sum_
            right_max = i

    return left_sum + right_sum, left_max, right_max


print(max_sum_dq_slow(A, 0, len(A) - 1))
