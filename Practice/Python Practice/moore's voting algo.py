class Solution:
    def majorityElement(self, nums):
        major_ele = 0
        count = 0
        # Phase1:
        for num in nums:
            if count == 0:
                major_ele = num
            count += (1 if major_ele == num else -1)

        # Phase 2
        if nums.count(major_ele) > len(nums) // 2:
            return major_ele
        else:
            return None


if __name__ == '__main__':
    # Input list
    print('Input:', [2, 2, 1, 1, 1, 2, 2])
    nums = [2, 2, 1, 1, 1, 2, 2]

    # Creating Object
    obj = Solution()

    # Output
    print('OutPut:', obj.majorityElement(nums))

