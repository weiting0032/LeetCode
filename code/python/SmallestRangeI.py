'''
Title: 908. Smallest Range I (Easy) https://leetcode.com/problems/smallest-range-i/

Runtime: 120 ms, faster than 21.00% of Python online submissions for Smallest Range I.
Memory Usage: 12.7 MB, less than 6.15% of Python online submissions for Smallest Range I.

Description:
        Given an array A of integers, for each integer A[i] we may choose any x with -K <= x <= K, and add x to A[i].

        After this process, we have some array B.

        Return the smallest possible difference between the maximum value of B and the minimum value of B.

Example:
    Input: A = [1], K = 0
    Output: 0
    Explanation: B = [1]

    Input: A = [0,10], K = 2
    Output: 6
    Explanation: B = [2,8]

    Input: A = [1,3,6], K = 3
    Output: 0
    Explanation: B = [3,3,3] or B = [4,4,4]

'''

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)
        