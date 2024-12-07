from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        
        for i, num in enumerate(nums):
            print(f"index: {i}, value: {num}")
            rest = target - num
            
            if rest in num_to_index:
                return [num_to_index[rest], i]
            
            num_to_index[num] = i
            print('x', num_to_index)




solution = Solution()

# # Example 1
# nums = [2, 7, 11, 15]
# target = 9
# result = solution.twoSum(nums, target)
# print(result)  # Output: [0, 1]

# Example 2
nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)  # Output: [1, 2]

# # Example 3
# nums = [3, 3]
# target = 6
# result = solution.twoSum(nums, target)
# print(result)  # Output: [0, 1]
