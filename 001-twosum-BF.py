class Solution(object):
    def twoSumBF(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i , j]
        return -1, -1

    def twoSumDic(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[target - nums[i]] = i
            else:
                return dic[nums[i]], i
        return -1, -1

solution = Solution()
print(solution.twoSumDic([2,7,11,15],22))
