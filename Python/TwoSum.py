# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i] + nums[j] == target):
#                     return [i,j]



# class Solution(object):
#     def twoSum(self, nums, target):
#         new_list = [] 
#         for i in range(len(nums)):
#             new_list.append(nums[i])
#             j = target - nums[i]
#             if j in new_list and new_list.index(j) != i:
#                 return [i, new_list.index(j)]
class Solution(object):
    def twoSum(self, nums, target):
        new_dict = {}
        for i in range(0,len(nums)):
            j = target - nums[i]
            if j in new_dict:
                return [i, new_dict[j]]
            new_dict[nums[i]] = i
