# 1470. Shuffle the Array
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(0, n):
           ans.append(nums[i])
           ans.append(nums[int(str(len(nums)/2 + i).split('.')[0] , 10)])
        return ans
    
    # Other Solution
        # x = nums[:len(nums)//2]
        # y = nums[len(nums)//2:]
        # ans = []
        # for i in range(0, n):
        #    ans.append(x[i])
        #    ans.append(y[i])
        # return ans