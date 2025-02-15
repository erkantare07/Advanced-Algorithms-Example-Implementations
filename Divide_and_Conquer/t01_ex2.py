# Description: Count the number of inversions in a list of numbers
# Two array elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

import random

def count_inversions(N, s, e):
    if s < e:
        # swap - base case - 2 elements
        if e - s == 1:
            if N[s] > N[e]:
                print("Inversions: ", [N[s], N[e]])
                N[s], N[e] = N[e], N[s]
                return 1
            return 0
        
        # divide
        m = (s + e) // 2
        n_inv_left = count_inversions(N, s, m)
        n_inv_right = count_inversions(N, m + 1, e)

        # merge
        cross_inv = 0
        left = N[s:m+1]
        right = N[m+1:e+1]
        i = j = 0
        k = s

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                N[k] = left[i]
                i += 1
            else:
                N[k] = right[j]
                cross_inv += len(left) - i
                print("Inversions: ", [left[i:], right[j]])
                j += 1
            k += 1
        
        while i < len(left):
            N[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            N[k] = right[j]
            j += 1
            k += 1

        del left, right, i, j, k

        return n_inv_left + n_inv_right + cross_inv
    
    # single element
    return 0

if __name__ == '__main__':
    # inversions: (84,21), (84,44), (84,41), (84,36), (84,34), (85,21), (85,44), (85,41), (85,36), (85,34), (91,44), (91,41), (91,36), (91,34), (98,44), (98,41), (98,36), (98,34), (44,41), (44,36), (44,34), (41,36), (41,34), (36,34)
    # 24 inversions
    N = [19, 84, 85, 21, 91, 98, 44, 41, 36, 34, 100, 101, 102, 103, 104, 105]

    print("Inversions: ", count_inversions(N, 0, len(N) - 1))