class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        Record = set()
        for i in nums:
            if i in Record:
                return True

            else:
                Record.add(i)

        return False


Sol = Solution()

# nums = [1,2,3,1]
# nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]

res = Sol.containsDuplicate(nums)
print(res)
