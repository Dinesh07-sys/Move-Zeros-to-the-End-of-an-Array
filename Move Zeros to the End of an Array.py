class Solution:
    def move_zeroes(self, nums: list[int]) -> None:
        n = len(nums)
        temp = []

        
        for num in nums:
            if num != 0:
                temp.append(num)


        while len(temp) < n:
            temp.append(0)


        for index in range(n):
            nums[index] = temp[index]

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    solution = Solution()
    solution.move_zeroes(nums)

    print(*nums)