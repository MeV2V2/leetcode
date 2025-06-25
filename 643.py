def findMaxAverage(nums: list[int], k: int) -> float:
    left, right = 0, k - 1
    cur_sum = sum(nums[:k])
    max_sum = cur_sum    
    
    while right < len(nums) - 1:
        right += 1
        max_sum = max(max_sum, cur_sum + nums[right] - nums[left])
        left += 1

    return max_sum / k


if __name__ == '__main__':
    nums = [0, 4, 0, 3, 2]

    result = findMaxAverage(nums, 1)
    print(result)