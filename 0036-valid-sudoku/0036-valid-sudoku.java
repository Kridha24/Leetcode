class Solution {
    static {
        for (int index = 0; index < 100; index++)
            isValidSudoku(new char[9][9]);
    }
    public static boolean isValidSudoku(char[][] board) {
        int[] rowMask = new int[9];
        int[] columnMask = new int[9];
        int[] boxMask = new int[9];

        for (int row = 0; row < 9; row++) {
            for (int column = 0; column < 9; column++) {
                if (board[row][column] == '.') continue;
                int bit = 1 << (board[row][column] - '1');
                int box = (row / 3) * 3 + column / 3;

                if ((rowMask[row] & bit) != 0 || (columnMask[column] & bit) != 0 || (boxMask[box] & bit) != 0) return false;
                
                rowMask[row] |= bit;
                columnMask[column] |= bit;
                boxMask[box] |= bit;
            }
        }

        return true;
    }
}