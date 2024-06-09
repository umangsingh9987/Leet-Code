class Solution:
    def rotate(self, nums, k):
        while k > 0:
            pop_element = nums.pop()
            nums.insert(0, pop_element)
            k = k - 1

        return nums


if __name__ == '__main__':
    # Input list
    print("Input:", [1, 2, 3, 4, 5, 6, 7, 8, 9])
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 3

    # Creating Object
    obj = Solution()

    # Output
    print('OutPut:', obj.rotate(nums, k))
