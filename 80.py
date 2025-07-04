class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        k = 2

        for i in range(2, len(nums)):
            if nums[i] == nums[i - 2]:
                continue
            nums[k] = nums[i]
            k += 1
            
        return k
    
if __name__ == '__main__':
    a = Solution()
    print(a.removeDuplicates([0,0,1,1,1,1,2,3,3]))


