class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return []
        if rowIndex == 1:
            return [[1]]
        
        result = [[1], [1, 1]]
        for i in range(2, rowIndex+1):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        
        return result[rowIndex]