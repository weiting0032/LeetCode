'''
Title: 832. Flipping an Image (Easy) https://leetcode.com/problems/flipping-an-image/

Runtime: 40 ms, faster than 50.52% of Python online submissions for Flipping an Image.
Memory Usage: 11.5 MB, less than 5.51% of Python online submissions for Flipping an Image.

Description:
        Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

        To flip an image horizontally means that each row of the image is reversed.  
        For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

        To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
        For example, inverting [0, 1, 1] results in [1, 0, 0].

Example:
    Input: [[1,1,0],[1,0,1],[0,0,0]]
    Output: [[1,0,0],[0,1,0],[1,1,1]]
    Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
    Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]

    Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
    Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
    Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]

'''

class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        new = []
        for i in range(len(A)):
            tmp = []
            for j in range(len(A)-1,-1,-1):
                if A[i][j] == 0:
                    tmp.append(1)
                else:
                    tmp.append(0)
            new.append(tmp)
        return new
        