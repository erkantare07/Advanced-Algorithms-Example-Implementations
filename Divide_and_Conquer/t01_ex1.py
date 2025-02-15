# Find the maximum and minimum of a list of numbers

import time
import random

# Iterative approach
def find_max_min(N):
    max = N[0]
    min = N[0]
    for i in range(1, len(N)):
        if N[i] > max:
            max = N[i]
        if N[i] < min:
            min = N[i]
    return max, min

# Divide and Conquer approach
def find_max_min_dc(N, l, r):
    if l == r:
        return N[l], N[l]
    else:
        mid = (l + r) // 2
        max1, min1 = find_max_min_dc(N, l, mid)
        max2, min2 = find_max_min_dc(N, mid + 1, r)
        
        return max(max1, max2), min(min1, min2)

# Divide and Conquer approach - for circularly shifted sorted array
def find_max_min_dc_shifted(N, s, e):
    if N[s] < N[e]:
        return N[e], N[s]
    return find_max_min_dc_shifted_helper(N, s, e)

def find_max_min_dc_shifted_helper(N, s, e):
    if e > s:
        mid = (s + e) // 2
        # if we divide max/min in the middle by chance
        if N[mid] > N[mid + 1]:
            return N[mid], N[mid + 1]
        
        # divide
        return find_max_min_dc_shifted(N, s, mid) if N[s] > N[mid] else find_max_min_dc_shifted(N, mid + 1, e)
    else:
        return N[s], N[s]

if __name__ == '__main__':

    N = [random.randint(1, 100) for i in range(2**4)]
    shift = 0#random.randint(1, len(N))
    print("N: ", N)
    N_sorted_k_shift = sorted(N)[shift:] + sorted(N)[:shift]
    print("N_sorted: ", sorted(N))
    print("Shift: ", len(N) - shift)
    print("N_sorted_shifted: ", N_sorted_k_shift)

    result_max, result_min = find_max_min_dc_shifted(N_sorted_k_shift, 0, len(N_sorted_k_shift) - 1)

    print("Max: ", result_max)
    print("Min: ", result_min)
