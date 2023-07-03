import java.util.*;

public class ticTacToe {
    private char[][] board;
    private char currentPlayerMark;

    public ticTacToe() {
        board = new char[3][3];
        currentPlayerMark = 'X';
        initializeBoard();
    }

    // Initialize the board with empty spaces
    public void initializeBoard() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                board[i][j] = '-';
            }
        }
    }

    // Print the current board state
    public void printBoard() {
        System.out.println("-------------");
        for (int i = 0; i < 3; i++) {
            System.out.print("| ");
            for (int j = 0; j < 3; j++) {
                System.out.print(board[i][j] + " | ");
            }
            System.out.println();
            System.out.println("-------------");
        }
    }

    // Check if the board is full
    public boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i][j] == '-') {
                    return false;
                }
            }
        }
        return true;
    }

    // Check if there is a win
    public boolean checkForWin() {
        // Check rows
        for (int i = 0; i < 3; i++) {
            if (checkRowCol(board[i][0], board[i][1], board[i][2])) {
                return true;
            }
        }

        // Check columns
        for (int i = 0; i < 3; i++) {
            if (checkRowCol(board[0][i], board[1][i], board[2][i])) {
                return true;
            }
        }

        // Check diagonals
        if (checkRowCol(board[0][0], board[1][1], board[2][2]) ||
                checkRowCol(board[0][2], board[1][1], board[2][0])) {
            return true;
        }

        return false;
    }

    // Check if all the elements in a row or column are the same
    public boolean checkRowCol(char c1, char c2, char c3) {
        return (c1 != '-') && (c1 == c2) && (c2 == c3);
    }

    // Place a mark at the given row and column
    public boolean placeMark(int row, int col) {
        if ((row >= 0) && (row < 3) && (col >= 0) && (col < 3) && (board[row][col] == '-')) {
            board[row][col] = currentPlayerMark;
            return true;
        }
        return false;
    }

    // Change the player turn
    public void changePlayer() {
        currentPlayerMark = (currentPlayerMark == 'X') ? 'O' : 'X';
    }

    // Get the next move from the computer
    public void computerMove() {
        Random rand = new Random();
        int row, col;
        do {
            row = rand.nextInt(3);
            col = rand.nextInt(3);
        } while (!placeMark(row, col));
    }

    public static void main(String[] args) {
        ticTacToe game = new ticTacToe();
        Scanner scanner = new Scanner(System.in);
        boolean gameOver = false;

        System.out.println("Welcome to Tic-Tac-Toe!");

        while (!gameOver) {
            System.out.println("Current board:");
            game.printBoard();
            System.out.println("Player " + game.currentPlayerMark + ", enter your move (row [0-2] column [0-2]):");

            int row = scanner.nextInt();
            int col = scanner.nextInt();

            if (game.placeMark(row, col)) {
                if (game.checkForWin()) {
                    System.out.println("Player " + game.currentPlayerMark + " wins!");
                    gameOver = true;
                } else if (game.isBoardFull()) {
                    System.out.println("It's a tie!");
                    gameOver = true;
                } else {
                    game.changePlayer();
                    game.computerMove();

                    if (game.checkForWin()) {
                        System.out.println("Player " + game.currentPlayerMark + " wins!");
                        gameOver = true;
                    } else if (game.isBoardFull()) {
                        System.out.println("It's a tie!");
                        gameOver = true;
                    } else {
                        game.changePlayer();
                    }
                }
            } else {
                System.out.println("Invalid move. Please try again.");
            }
        }

        scanner.close();
    }
}
