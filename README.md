# Pong Game 🎾

A classic Pong game implemented in **Python** (using **Pygame** or your framework of choice). This project lets you play a two-player (or AI) version of Pong, complete with paddle movement, collision, scoring, and basic game logic.

---

## Table of Contents

- [Features](#features)  
- [How to Run](#how-to-run)  
- [Controls](#controls)  
- [Project Structure](#project-structure)  
- [Dependencies](#dependencies)  
- [Possible Improvements](#possible-improvements)  
- [Contributing](#contributing)  
- [License](#license)

---

## Features

- Real-time paddle and ball movement  
- Scoring system  
- Collision detection (ball ↔ paddle, ball ↔ wall)  
- Simple AI opponent (optional / if implemented)  
- Restart or quit functionality  

---

## How to Run

```bash
git clone https://github.com/MattCollingwood/Pong.git  
cd Pong  
python main.py
```

## Controls
**Left Paddle**: W (up), S (down)
**Right Paddle**: Up Arrow (up), Down Arrow (down)
**Quit / Restart**: (describe how you implemented these, e.g., Esc to quit)


## Project Structure
```
Pong/
│
├── assets/                # (optional) images, sound files, etc.
├── pong.py                # main game loop / logic
├── paddle.py              # paddle class / logic
├── ball.py                # ball class / movement and collision
├── score.py               # (optional) scoring / scoreboard
└── README.md              # this file
```

##  Dependencies

Python 3.x
Pygame

```
pip install pygame
```

##License
This project is licensed under the MIT License — see the LICENSE
 file for details.
