https://en.wikipedia.org/wiki/Longest_increasing_subsequence

Given: an array of unsorted integers X.
Output: The longest subsequence S of elements from X wherein the elements of S are in sorted ascending order.

Constraints:
  * The subsequence need not be continugous.
  * The subsequence need not be unique -- potentially more than one right answer.

Common pitfall: Quadratic naive solution. Dynamic programming using a greedy algorithm can tighten this to O(n logn).

Sample inputs and outputs:
  0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15 -> 0 2 6 9 11 15
  1 2 2 5 9 5 4 4 1 6 -> 1 2 4 6
  4 9 4 9 9 8 2 9 0 1 -> 4 8 9
  0 5 4 6 9 1 7 6 7 8 -> 0 1 6 7 8
  1 2 20 13 6 15 16 0 7 9 4 0 4 6 7 8 10 18 14 10 17 15 19 0 4 2 12 6 10 5 12 2 1 7 12 12 10 8 9 2 20 19 20 17 5 19 0 11 5 20 -> 1 2 4 6 7 8 10 14 15 17 19 20

