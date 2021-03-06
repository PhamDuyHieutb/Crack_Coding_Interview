class Solution:
    """
    constraints: 0 <= nums[i] <= 100
    """
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101

        for num in nums:
            count[num] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        return [count[num - 1] if num > 0 else 0 for num in nums]

    def backup(self, nums):
        count = [0] * 101

        for num in nums:
            count[num] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        return [count[num - 1] if num != 0 else 0 for num in nums]
