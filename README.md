# Math Puzzle Game

This Python script (`math_puzzle.py`) is an interactive math-based puzzle game I created to challenge players' problem-solving skills. The game generates a sequence of mathematical puzzles based on a randomly selected formula, displays four solved examples, and asks the player to solve the fifth puzzle within a 30-second time limit. Points are awarded for correct answers, and difficulty increases every 10 points, advancing to a new level.

⚠️ **Note**: This game is designed for educational and entertainment purposes. Ensure you have Python installed to run it.

## Features
- Generates random math puzzles using operations like `n*n+n`, `n**3`, or `n**2+n**2`.
- Uses threading to enforce a 30-second time limit per puzzle.
- Tracks points and increases difficulty (level) as the player progresses.
- Displays a countdown timer for each puzzle.

## Prerequisites
- Python 3.x
- Required modules: `threading`, `time`, `random`, `sys` (all included in Python's standard library)

## Installation

1. **Clone or Download the Repository**:
   - Clone this repository or download the script:
     ```bash
     git clone https://github.com/shra1-tech/Games.git
     cd Games
     ```

2. **Save the Script**:
   - Ensure the script is saved as `math_puzzle.py`.

## Usage

1. **Run the Script**:
   - Execute the script in a terminal or command prompt:
     ```bash
     python3 math_puzzle.py
     ```

2. **How to Play**:
   - The game displays four solved math puzzles (e.g., `3 + 3 = 12`) and one unsolved puzzle (e.g., `7 + 7 = ?`).
   - Enter the value for `?` within 30 seconds.
   - Correct answers earn 1 point; incorrect answers or timeouts end the game.
   - Every 10 points, the game advances to a new level, increasing difficulty by adjusting the range of numbers used.
   - Example output:
     ```
     current level: 1
     3 + 3 = 12
     4 + 4 = 20
     5 + 5 = 30
     6 + 6 = 42
     7 + 7 = ?
     Time left: 30 seconds
     Enter value of '?': 56
     correct answer
     points: 1
     ```

3. **Stop the Game**:
   - The game ends if you answer incorrectly, run out of time, or manually stop the script (`Ctrl+C`).

## Notes
- **Environment**: Run in a local Python environment or a sandbox for testing.
- **Customization**: Modify the `operations` list in the script to add new mathematical formulas or adjust the `countdown` time (default: 30 seconds) for a different challenge.
- **Monitoring**: The game displays a countdown timer to track remaining time per puzzle.
- **Limitations**: The script uses basic console input/output. Future enhancements could include a GUI or additional puzzle types.
