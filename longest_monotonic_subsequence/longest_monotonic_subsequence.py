from math import ceil

def longest_monotonic_subsequence(array):
    n = len(array)
    max_indices = [0] * (n + 1)
    predecessors = [0] * n
    max_length = 0
    
    for i in range(n):
        low = 1
        high = max_length

        # Use binary search because efficiency!
        #
        # Here, we are trying to find the latest-occurring
        # value from the input array that is less than a
        # value we have seen thus far as a terminator for
        # some sequence. 
        #
        # max_indices[j] will represent the maximum index 
        # of some element in array wherein it is the smallest
        # terminator of any monotonic subsequence of length j.
        while low <= high:
            mid = ceil((low + high) / 2)
            if array[max_indices[mid]] < array[i]:
                low = mid + 1
            else:
                high = mid - 1

        # low = length of longest prefix + 1 due to binary search.
        subseq_length = low

        # Update predecessor to represent the index of the preceding
        # term in the longest subsequence that ends at i.
        #
        # e.g. suppose i = 3; there is some subsequence of terms S
        # that ends at array[3]. predecessors[3] represents the
        # second-to-last term in S.
        #
        # This will allow us to reconstruct a final sequence later
        # after we have analyzed the entire array.
        predecessors[i] = max_indices[subseq_length - 1]
        max_indices[subseq_length] = i

        if subseq_length > max_length:
            max_length = subseq_length
    
    # Now we can rebuild the sequence, starting from the final
    # term of the longest sequence at max_indices[max_length]
    # and working backwards by using predecessors. This produces
    # one of potentially many correct sol'n.
    final_subseq = [0] * max_length
    k = max_indices[max_length]
    for i in range(max_length - 1, -1, -1):
        final_subseq[i] = array[k]
        k = predecessors[k]

    return final_subseq

mountains = list(map(int, input().split()))
trail = longest_monotonic_subsequence(mountains)
print(trail)

