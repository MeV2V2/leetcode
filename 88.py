class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, n1, n2 = len(nums1) - 1, m - 1, n - 1
        while (i >= 0) and (n2 >= 0) and (n1 >= 0):
            if nums2[n2] >= nums1[n1]:
                nums1[i] = nums2[n2]
                n2 -= 1 
            else:
                nums1[i] = nums1[n1]
                n1 -= 1

            i -= 1

        while n2 >= 0:
            nums1[n2] = nums2[n2]
            n2 -= 1

if __name__ == '__main__':
    a = Solution()
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1

    a.merge(nums1, m, nums2, n)