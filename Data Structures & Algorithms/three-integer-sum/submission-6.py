class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left=i+1
            right=len(nums)-1
            while right > left:
                if nums[i]+nums[left]+nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while nums[left-1] == nums[left] and left<right:
                        left+=1
                elif nums[i]+nums[left]+nums[right] < 0:
                    left+=1
                else:
                    right-=1
        return res