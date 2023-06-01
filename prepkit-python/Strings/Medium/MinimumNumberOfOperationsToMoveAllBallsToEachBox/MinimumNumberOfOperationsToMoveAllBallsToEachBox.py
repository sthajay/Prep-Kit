# 1769. Minimum Number of Operations to Move All Balls to Each Box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = [0]*n
        leftCount, leftCost, rightCount, rightCost = 0, 0, 0, 0
        for i in range(1, n):
            if boxes[i-1] == '1':
                leftCount += 1
            leftCost += leftCount
            ans[i] = leftCost
        for i in range(n-2, -1, -1):
            if boxes[i+1] == '1':
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans

        # Other Solution O(n^2)
        # ans = [0]*len(boxes)
        # for i in range(len(boxes)):
        #     temp = 0
        #     for j in range(len(boxes)):
        #         if i != j and boxes[j] == '1':
        #             temp += abs(j - i)
        #     ans[i] = temp
        # return ans
