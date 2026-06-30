class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [[] for _ in range(9)]
        rows = board.copy()
        grids = [[] for _ in range(9)]
        row_counter = 1
        for row in board:
            col_counter = 1
            for element in row:
                cols[col_counter -1].append(element)
                if row_counter <=3 and col_counter <=3:
                    grids[0].append(element)
                if row_counter <=3 and col_counter <=6 and col_counter>3:
                    grids[1].append(element)
                if row_counter <=3 and col_counter <=9 and col_counter>6:
                    grids[2].append(element)
                if row_counter <=6 and row_counter >3 and col_counter <=3:
                    grids[3].append(element)
                if row_counter <=6 and row_counter >3  and col_counter <=6 and col_counter>3:
                    grids[4].append(element)
                if row_counter <=6 and row_counter >3  and col_counter <=9 and col_counter>6:
                    grids[5].append(element)
                if row_counter <=9 and row_counter >6 and col_counter <=3:
                    grids[6].append(element)
                if row_counter <=9 and row_counter >6  and col_counter <=6 and col_counter>3:
                    grids[7].append(element)
                if row_counter <=9 and row_counter >6  and col_counter <=9 and col_counter>6:
                    grids[8].append(element)
                col_counter = col_counter + 1
            row_counter = row_counter+1

        def isvalid_element(lis):
            res = [0]*9
            for element in lis:
                if element == ".":
                    continue
                res[int(element) - 1] += 1
                if res[int(element) - 1] > 1:
                    return False
            return True
            
        for pattern in cols+rows+grids:
            if isvalid_element(pattern) == False:
                return False
        return True