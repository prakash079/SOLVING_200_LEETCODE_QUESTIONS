#question2
#question link=https://leetcode.com/problems/shuffle-the-array/

---------------------------
#solution
""" the simplest solution for this problem we can think of :
is that we can take an empty array and merge/append
each element of the array from index 0 and index n as there are
n elements difference in the sorted arrays"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=[]
        for i in range(0,n):
            
            l.append(nums[i])
            l.append(nums[n+i])
        return l
