class Solution:
    def searchMatrix(self, matrix: 'List[List[int]]', target: 'int') -> 'bool':
        if matrix is None:
            return False
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        row = len(matrix)
        col = len(matrix[0])
        left = col*0+0
        right = col*(row-1)+(col-1)
        while left<=right:
            mid = int((left+right)//2)
            x = int(mid % col)
            y = int(mid // col)
            if x < row and y < col:
                if(target == matrix[x][y]):
                    return True
                if target<mid:
                    right = mid
                if target>mid:
                    left = mid
        return False




solution = Solution()
print(solution.searchMatrix([[1,3,5,7], [10,11,16,20], [23, 30, 34, 50]], 3))


