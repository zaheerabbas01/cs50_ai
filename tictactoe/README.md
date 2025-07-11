# ❌⭕ Tic-Tac-Toe AI

*Powered by the Minimax Algorithm 🤖*

Welcome to the classic game of **Tic-Tac-Toe**, where you’ll face off against an unbeatable AI!
This project is part of [CS50’s Introduction to AI with Python](https://cs50.harvard.edu/ai/) course.

---

## 🎮 How to Play

👉 **Goal**: Get 3 of your symbols (❌ or ⭕) in a row — horizontally, vertically, or diagonally.

🧠 **You vs AI**:

* You’ll play as **O (circle)**.
* The AI will play as **X (cross)**.
* The AI uses the **Minimax algorithm** to play perfectly — it will never lose!

📋 **Controls**:

* Run the game, and click on any empty square to make your move.
* The AI will respond instantly with its move.

---

## 🖥️ How It Works

This game uses two main Python files:

| File           | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| `tictactoe.py` | Contains all the game logic and the AI implementation using Minimax |
| `runner.py`    | Graphical interface (GUI) built with Pygame                         |

---

## 🧠 AI Logic (Minimax Algorithm)

The AI makes its decisions based on the **Minimax algorithm**, which:

* Explores all possible future game states 🧩
* Assumes the opponent (you) plays optimally 👀
* Chooses the move that maximizes its chance to win and minimizes the risk of losing 🏆

In simple words:

> *If you make a mistake, the AI will win. If you play perfectly, it will tie.*

---

## 🚀 How to Run the Game

1. ✅ **Install Python 3.12** (recommended for this project)
2. ✅ **Install requirements**:

   ```bash
   pip install -r requirements.txt
   ```
3. ▶️ **Launch the game**:

   ```bash
   python runner.py
   ```

---

## 🧪 Sample Gameplay

```text
O goes first.
Click on an empty square to make your move.
AI (X) will respond with the best possible move.
Keep playing until someone wins or the board is full!
```

🧑‍💻 Example:

```
O |   |  
---------
  | X |  
---------
  |   |  
```

---

## 📦 Project Structure

```
tictactoe/
├── tictactoe.py     # Game logic and AI (edit this)
├── runner.py        # GUI game interface (provided)
├── requirements.txt # pygame dependency
├── README.md        # You’re reading it now :)
```

---

## ✨ Features

* ✅ Graphical user interface (via Pygame)
* ✅ Turn-based human vs AI gameplay
* ✅ AI never loses!
* ✅ Clear win/tie detection
* ✅ Fully functional Minimax algorithm

---

## 🎯 Learning Objectives

* Implement an unbeatable AI using **Minimax**
* Understand **adversarial search** in AI
* Use **Pygame** for building simple games
* Learn how to represent and manipulate **game states**

---

## 🧠 Remember:

> “The best move is the one that leaves your opponent with the worst moves.” — Minimax Philosophy
