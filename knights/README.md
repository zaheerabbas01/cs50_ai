# 🏰 CS50 AI: Knights

This is my implementation of **Project 1: Knights** from [Harvard’s CS50 Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/). The project focuses on **logical inference** in a puzzle-like environment where a character deduces where knights are hidden on a grid.

## 🧠 Project Overview

In this logic puzzle, a character moves across a 2D grid where some cells contain hidden knights. The goal is to determine, using **propositional logic**, which cells contain knights and which are safe, based on a set of clues.

The project implements:

* **Modeling knowledge** in propositional logic
* **Constructing logical sentences** using symbols and operators
* **Applying inference** with a model-checking algorithm to solve the puzzle

## 🧩 Key Concepts

* **Knowledge Base (KB)**: A collection of logical sentences about the game state
* **Symbols**: Propositional variables (e.g., `Knight(A, B)`)
* **Inference**: Using the KB to determine if a symbol must be true/false
* **Model Checking**: An exhaustive approach to test logical entailment

---

## 🛠️ Features

* Build a logical model of the game grid
* Deduce the locations of knights using logical inference
* Identify safe moves and knight locations with certainty
* Visual terminal-based grid output for puzzle state

---

## 📂 File Structure

```
knights/
├── puzzle.py        # Logic for generating and displaying the puzzle
├── logic.py         # Logic for knowledge representation and model checking
├── runner.py        # Runs the puzzle and applies the AI logic
├── README.md        # This file
```

---

## 🚀 How to Run

1. **Install Python 3** if not already installed.

2. **Clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/knights-project.git
cd knights-project
```

3. **Run the game AI**:

```bash
python runner.py
```

You’ll see a grid where the AI deduces the safe and knight-containing cells.

---

## 🧪 Sample Output

```
Puzzle:
. 2 .
. . .
. . .

AI's knowledge:
Safe moves: (1, 2), (2, 0)
Knights: (0, 1)
```

---

## 📖 What I Learned

* How to represent real-world logic problems using propositional logic
* How model checking works in AI
* The importance of **knowledge representation** and **deductive reasoning**
* Foundations of logical inference systems used in modern AI applications

---

## 🧠 Related Topics

* Propositional Logic
* Knowledge-Based Agents
* Inference Engines
* Search vs Logic in AI

---

## 📚 Resources

* [CS50 AI Course](https://cs50.harvard.edu/ai/)
* [Python Docs](https://docs.python.org/3/)
* [Logic and Inference](https://en.wikipedia.org/wiki/Inference)
