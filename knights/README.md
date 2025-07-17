# 🏰 CS50 AI: Knights

Solve logic puzzles using **propositional logic** and **model checking** in Python.

## 📚 Overview

This project is inspired by Raymond Smullyan’s *Knights and Knaves* logic puzzles. In these puzzles, each character is either:

* **Knight** (always tells the truth), or
* **Knave** (always lies)

Your goal is to write an AI that can determine, using logical inference, who is a knight and who is a knave based on what the characters say.

---

## 🛠️ Files Included

```
knights/
├── logic.py      # Core logic engine (do not modify)
├── puzzle.py     # Where you build the knowledge bases
├── README.md     # This file
```

---

## 💡 Objective

Complete the knowledge bases `knowledge0`, `knowledge1`, `knowledge2`, and `knowledge3` in `puzzle.py`, so that your AI can automatically solve the given logical puzzles using **model checking**.

---

## 🧩 The Puzzles

### Puzzle 0

A says: “I am both a knight and a knave.”

### Puzzle 1

A says: “We are both knaves.”
B says nothing.

### Puzzle 2

A says: “We are the same kind.”
B says: “We are of different kinds.”

### Puzzle 3

A says either “I am a knight.” or “I am a knave.” (you don’t know which).
B says: “A said ‘I am a knave.’”
B also says: “C is a knave.”
C says: “A is a knight.”

---

## ⚙️ How to Run

Make sure you have **Python 3.12** installed.

```bash
python puzzle.py
```

You’ll see the AI’s deductions about each puzzle printed to the console.

---

## 🧠 Key Concepts Used

* **Propositional Logic**
* **Logical Connectives**: `And`, `Or`, `Not`, `Implication`, `Biconditional`
* **Model Checking**: Testing all possible truth assignments
* **Knowledge Bases**: Logical representation of facts and statements

---

## 🧪 Example Output

```bash
Puzzle 0
    A is a Knave

Puzzle 1
    B is a Knight

Puzzle 2
    A is a Knave
    B is a Knight

Puzzle 3
    A is a Knight
    C is a Knight
```

---


## 💭 Hints

* Remember: Knights always tell the truth, Knaves always lie.
* Use propositional symbols like `AKnight`, `AKnave`, etc.
* Use logical constructs (`And`, `Or`, `Implication`) to build the puzzle rules.
* Don’t manually hard-code answers — let the AI deduce them from logic.

---

## 🎓 What You Learn

* How to represent knowledge with logic
* How inference engines work
* Foundation for more advanced AI concepts (e.g. constraint satisfaction, logic programming)

---

## 📚 Resources

* [CS50 AI Course](https://cs50.harvard.edu/ai/)
* [Raymond Smullyan’s Puzzles](https://en.wikipedia.org/wiki/Knights_and_Knaves)
* [Propositional Logic (Wikipedia)](https://en.wikipedia.org/wiki/Propositional_calculus)
