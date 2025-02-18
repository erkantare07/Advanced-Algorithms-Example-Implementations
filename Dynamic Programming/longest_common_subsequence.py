# Longest Common Subsequence
# Given two strings, find the length of the longest common subsequence but not necessarily in a contiguous fashion.

# Recursive - O(2^n) where n is the length of the longer string
# Recursive with memoization - O(n*m) where n and m are the lengths of the two strings
def longest_common_subseq(s1, s2, use_memoization=False): # s1 and s2 are the strings, i1 and i2 are the indices
    
    M = [[-1 for _ in range(len(s2))] for _ in range(len(s1))] # memoization table

    def _longest_common_subseq(s1, s2, i1, i2):
        if i1 < 0 or i2 < 0:
            return ""
        
        if use_memoization and M[i1][i2] != -1:
            return M[i1][i2]
    
        if s1[i1] == s2[i2]: # if the characters match, then it is part of the common subsequence
            return _longest_common_subseq(s1, s2, i1-1, i2-1) + s1[i1]
        
        # if the characters do not match, then we have two options:
        # 1. exclude the character from the first string
        first_excluded = _longest_common_subseq(s1, s2, i1-1, i2)
        # 2. exclude the character from the second string
        second_excluded = _longest_common_subseq(s1, s2, i1, i2-1)

        best = max(first_excluded, second_excluded, key=len)
        M[i1][i2] = best
        return best

    return _longest_common_subseq(s1, s2, len(s1)-1, len(s2)-1)

# iterative - O(n*m) where n and m are the lengths of the two strings
def longest_common_subseq_iterative(s1, s2):
    M = [["" for _ in range(len(s2)+1)] for _ in range(len(s1)+1)] # M[i][j] will store the length of the longest common subsequence of s1[:i] and s2[:j]

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            str_i, str_j = i-1, j-1
            if s1[str_i] == s2[str_j]:
                M[i][j] = M[i-1][j-1] + s1[str_i]
            else:
                M[i][j] = max(M[i-1][j], M[i][j-1], key=len)
    
    return M[len(s1)][len(s2)]

if __name__ == "__main__":
    s1 = "ANMN,NMNM,NMNM,NM,MAM,NM,NM,NM,N,MNNNM,NM,MN,MINMN,NMN,GM,N,N,MNO"
    s2 = "AKKLJKJLKJKLMKJLLKJKLJKLALKJJKLJKJLKNKJLKJKLJHJHKIJKHJKHJLHKLIKLJKJJKLJNKLJJLJKLJGKLJLKO"

    import time
    
    time_start = time.time()
    print("Longest common subsequence: ", longest_common_subseq(s1, s2, use_memoization=True))
    print("Time taken recursive with memoization: ", time.time() - time_start)

    time_start = time.time()
    print("Longest common subsequence: ", longest_common_subseq_iterative(s1, s2))
    print("Time taken with dp iterative: ", time.time() - time_start)
    
    # Takes too much time - don't run it
    # time_start = time.time()
    # print("Longest common subsequence: ", longest_common_subseq(s1, s2))
    # print("Time taken recursive without memoization: ", time.time() - time_start)