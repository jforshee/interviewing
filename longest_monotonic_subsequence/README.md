https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Given: an array of unsorted integers X.
Output: The longest subsequence S of elements from X wherein the elements of S are in sorted ascending order.

Constraints:
  * The subsequence need not be continugous.
  * The subsequence need not be unique -- potentially more than one right answer.

Common pitfall: Quadratic naive solution. Dynamic programming using a greedy algorithm can tighten this to O(n logn).

