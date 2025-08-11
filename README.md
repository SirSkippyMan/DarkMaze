# Dark Maze
A simple but fun Pygame-based game with six progressively challenging levels.
Move your character using the WASD keys, avoid obstacles, and reach the goal in each stage.

## Installation
1. Clone the repository:
`git clone https://github.com/sirskippyman/DarkMaze.git`
2. Open the repository:
`cd DarkMaze`
3. Make the run script executable:
`chmod +x darkmaze.sh`
4. Run the game:
`./darkmaze.sh`

This script will:
1. Check for Python 3
2. Create a virtual environment (venv)
3. Install all dependencies from requirements.txt
4. Launch the game

NOTE: The virtual environment is active only while the game is running. You do not need to
manually deactiveate it.

## How to Play
Your character will move in four directions based on the keys pressed:
- W for up
- A for left
- S for down
- D for right

## Requirements
- Python 3.8+
- pip (comes with Python)
- Internet connection for first-time dependency install

## Troubleshooting
pygame not found
> Run the following commands:
`source venv/bin/activate`
`python -m pip install pygame`
> If you're not running on Windows, run with the following script:
`bash darkmaze.sh`

## Credits
All code, music, and art was created by Josh Nygaard
joshdn03@gmail.com
https://www.linkedin.com/in/josh-nygaard/



