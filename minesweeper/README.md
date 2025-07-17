# 💣 Minesweeper AI

> *"Can an AI solve Minesweeper without blowing up?"*

This project builds a **logical AI** that can play the classic puzzle game **Minesweeper** by reasoning with propositional logic and making inferences about the board — just like a human would! 🧠

---

## 🎯 Goal

Create an AI that:

* 🚩 Identifies all the mines
* 🛟 Safely uncovers non-mine cells
* 🤔 Infers safe and dangerous cells using logic
* 🧠 Learns from moves and updates its knowledge

---

## 🕹️ How to Play (via AI)

Run the game and watch your AI:

* Click a random cell to begin
* Use the revealed number to infer where mines might be
* Build logical sentences like:

  ```
  {A, B, C} = 1
  ```

  meaning one of A, B, or C is a mine
* Deduce new knowledge using subset logic
* Make safe moves where possible, otherwise guess smartly

---

## 🧠 How the AI Thinks

### 🧩 Knowledge Representation

Each piece of knowledge is a sentence like:

```
{A, B, C} = 2
```

Which means: "Two of these three cells contain mines."

The AI stores all such knowledge and updates it after each move.

### 🧮 Logical Inference Rules

* ✅ If `{A, B, C} = 0` → All are safe
* 💣 If `{X, Y} = 2` → Both are mines
* ➕ If `{A, B, C} = 1` and `{A, B, C, D} = 2` → `{D} = 1`

  > (Subset rule: Difference of sets = Difference of counts)

### 🌀 The Loop

After each move:

1. Add new sentence to knowledge base
2. Mark any known safe cells or mines
3. Infer new sentences
4. Repeat until the board is solved or only guesses remain

---

## 🗂️ Project Structure

```
minesweeper/
├── minesweeper.py    # Game engine (board + display)
├── sentence.py       # Represents logical sentences (e.g., {A, B, C} = 1)
├── minesweeperai.py  # The brain of the AI (your main work here)
├── runner.py         # Optional GUI to run the game
└── README.md         # You're reading it now!
```

---

## ▶️ Run It

```bash
python runner.py
```

Watch the AI make moves on the board, flag mines 🚩, and win (hopefully)!
Want to see logic only? You can test without the GUI too!

---

## 🔍 Features

✅ Automatically deduces safe/mine cells
✅ Tracks known safes and mines
✅ Uses subset inference logic
✅ Updates sentences after learning new facts
✅ Will guess **only if forced**

---

## 🔧 Requirements

* Python 3.12
* No external libraries needed (just standard Python)

---
