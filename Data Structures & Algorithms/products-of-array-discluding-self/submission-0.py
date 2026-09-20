class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_mult =1
        right_mult =1 
        left=[1]*len(nums)
        right=[1]*len(nums)

        for i in range(len(nums)):
            left[i]= left_mult
            left_mult *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            right[i] = right_mult
            right_mult *= nums[i]
        
        return [left[i]*right[i] for i in range(len(nums))]