class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();

        // Validate rows
        for (int r = 0; r < n; r++) {
            unordered_set<char> nums;
            int numCount = 0;
            for (int c = 0; c < n; c++) {
                if (board[r][c] != '.') {
                    numCount++;
                    nums.insert(board[r][c]);
                }
            }
            if (numCount != nums.size()) {
                return false;
            }
        }

        // Valudate columns
        for (int c = 0; c < n; c++) {
            unordered_set<char> nums;
            int numCount = 0;
            for (int r = 0; r < n; r++) {
                if (board[r][c] != '.') {
                    numCount++;
                    nums.insert(board[r][c]);
                }
            }
            if (numCount != nums.size()) {
                return false;
            }
        }

        // Validate square
        for (int r = 0; r < n / 3; r++) {
            for (int c = 0; c < n / 3; c++) {
                unordered_set<char> nums;
                int numCount = 0;
                for (int i = 0; i < 3; i++) {
                    int row = r * 3 + i;
                    for (int j = 0; j < 3; j++) {
                        int col = c * 3 + j;
                        if (board[row][col] != '.') {
                            numCount++;
                            nums.insert(board[row][col]);
                        }
                    }
                }
                if (numCount != nums.size()) {
                    return false;
                }
            }
        }
        return true;
    }
};
