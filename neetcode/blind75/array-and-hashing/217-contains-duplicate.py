class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


print(Solution().containsDuplicate([1, 2, 3, 1]))
print(Solution().containsDuplicate([1, 2, 3, 4]))
print(Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
