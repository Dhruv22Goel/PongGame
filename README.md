# 🏓 Classic Pong Game (Turtle Graphics - Python)

A modern remake of the classic Pong game built using Python's built-in `turtle` graphics module. This version includes clean visuals, smooth paddle movement, score tracking, and a responsive game loop – all without external libraries.

---

## 🎮 Features

- 🟩 Two-player paddle control (`W/S` for Left, `↑/↓` for Right)
- 🟢 Ball collision with walls and paddles
- ✅ Scoreboard that updates in real-time
- ⚠️ Game resets ball position on miss
- 🧱 Improved UI with center line and smooth paddle motion
- 🛑 Prevents paddles from going off screen
- 🛠 Bug fix: Ball no longer gets stuck behind paddles

---

## 🧱 Project Structure

```bash
pong-game/
│
├── Main.py           # Main game loop
├── Paddle.py         # Paddle class with movement logic
├── Ball.py           # Ball class with bounce and reset behavior
├── ScoreBoard.py     # Score tracking and display
└── README.md         # You're reading it!
```

## 🚀 Getting Started
### ✅ Prerequisites
      Python 3.x installed
      (Tested on Python 3.10+)
### ▶️ Run the Game
      python Main.py

## ⌨️ Controls

| Player | Move Up   | Move Down |
|--------|-----------|-----------|
| LEFT   |  W        |  S        | 
|--------|-----------|-----------|
| RIGHT  |  ↑ Arrow	 |  ↓ Arrow	 |
|--------|-----------|-----------|
