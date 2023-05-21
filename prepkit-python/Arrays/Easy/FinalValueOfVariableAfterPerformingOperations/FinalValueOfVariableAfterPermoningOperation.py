# 2011. Final Value of Variable After Performing Operations
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for el in operations:
            if '+' in el:
                x += 1
            else:
                x -= 1
        return x

        # Other solution
        # add = operations.count('++X') + operations.count('X++')
        # sub = operations.count('--X') +  operations.count('X--')
        # return add - sub

        # add = operations.count('++X') + operations.count('X++')
        # return add - (len(operations) - add)
