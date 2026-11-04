class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<char>> cols, rows;
        map<pair<int, int>, unordered_set<char>> squares;

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.')
                    continue;

                char value = board[r][c];
                if (rows[r].count(value) || 
                    cols[c].count(value) || 
                    squares[{r / 3, c / 3}].count(value)) {
                    return false;
                }
                rows[r].insert(value);
                cols[c].insert(value);
                squares[{r / 3, c / 3}].insert(value);
            }
        }
        return true;
    }
};
