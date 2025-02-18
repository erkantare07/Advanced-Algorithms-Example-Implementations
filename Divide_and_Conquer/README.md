# Personal Notes on Divide and Conquer

### Questions to be asked to decide whether it is worth using D&C
1. Can I split the problem into *isolated* subproblems? => feasibility (might not be a dealbreaker though...)
2. Can I merge the subproblem solutions in reasonable time? => possible bottleneck
3. Is the total number of smallest problems a reasonable amount? => possible bottlenect (assuming O(1) for base case)
    -> in general, can I solve all base case problems in reasonable time?
    Note: This number is determined by the num. of splits and problem reduction factor per split. Recall master theorem.

### How to determine split and problem reduction size?
* If the merging step is more expensive than the number of base case problems then the bottleneck is merge. Since we have control over split count (sc: #recursive calls at a time) and problem reduction factor (prf: reduced original size to new smaller size by dividing by what), we want to have merge as bottleneck. However, sc and prf are dependent on eachother. If prf is greater than sc than we don't look all elements and if other way around then we look some same elements multiple times. Furthermore these can also affect the merge speed since sc determines how many pieces should be merged at the same time. Merging less pieces are generally less work but merging more pieces at once reduces the depth of the recursion tree. However, recall from master theorem, sc only determines the base of the logarithm and in asymptotic representation it doesn't make a big difference in runtime calculation and can be ignored. So keeping merge cheaper is the first concern then if it doesn't make merge more expensive than we can increase sc (together with prf) to optimize even further (although slightly(?))

### Examples

**Merge Sort:** Subproplems won't need info from other subproblems (isolated). We don't need to include same number into different subproblems (n atomic problems are enough - which is the least amount if we need to look at every single data point to solve the problem). Merging can be done in O(n). Hence the runtime is merge x recursion tree depth (log_2(n) but base doesn't matter in asymptotic notation)

**max subset sum:** n many atomic cases. Merge can compare both sums O(1) and find cross by checking sum beginning from end of right and start of left in O(n). Merge O(n) and num of atomic problems is not a bottleneck.

**find_max_min:** Iterative is here O(n). Does D&C help us further? Let's see... Atomic problems are isolated and can be solved in O(1) and merge is actually also O(1) which is just 2 comparisons. However, here is the bottleneck the num. of atomic problems. We should have at least n atomic problems to get data from each number. Hence this dominates => O(n)

**count inversions:** Subproblems can be solved independently (isolated). n many atomic problems are enough. We should investigate merge. We can sum both #subproblem_inversions in O(1) and then check inversion inbetween. If both subproblems also return sorted lists (or sort in-place) then we can count cross inversions in O(n). Sorting can be done using merge sort which is also O(n) during merge. So our merge can be O(n), hence runtime is O(n) x depth of recursion tree => log base doesn't matter in asymptotic notation => O(n) x O(logn) = O(nlogn)

**closest point pair:** O(n) atomic and O(n) merge.

