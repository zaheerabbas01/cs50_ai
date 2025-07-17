# 🎬 Degrees of Separation — CS50 AI Project

> “How many steps away is one actor from another?”
> Using **Breadth-First Search (BFS)**, this AI finds the shortest connection between two actors based on movies they’ve starred in together.

---

## 🧠 Project Goal

You’ll build a program that determines how many **degrees of separation** exist between two actors, similar to the [Six Degrees of Kevin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) game!

---

## 🛠️ How It Works

### 📁 Dataset Structure

The program uses three CSV files to model Hollywood:

| File         | Description                                               |
| ------------ | --------------------------------------------------------- |
| `people.csv` | Each row = a person (with their ID, name, and birth year) |
| `movies.csv` | Each row = a movie (with its ID, title, and year)         |
| `stars.csv`  | Each row = connection between a person and a movie        |

These files create a **graph** where:

* **Nodes** = actors 🎭
* **Edges** = shared movies 🎬

The AI then uses **Breadth-First Search** to find the **shortest path** between two actors.

---

### 2. 🏃 Run It

```bash
python degrees.py large
```

You’ll be prompted:

```text
Name: Emma Watson
Name: Jennifer Lawrence
```

Output:

```text
3 degrees of separation.
1: Emma Watson and Brendan Gleeson starred in Harry Potter and the Order of the Phoenix
2: Brendan Gleeson and Michael Fassbender starred in Trespass Against Us
3: Michael Fassbender and Jennifer Lawrence starred in X-Men: First Class
```

You can also test on a smaller dataset:

```bash
python degrees.py small
```

---
## 🤔 How It Plays Out

Behind the scenes:

* 🌐 The program builds a graph of actors and movies.
* 🔍 It runs **BFS** to explore the shortest sequence of movie connections.
* 🎯 It stops when it finds the target actor and returns the path.

---

## 📚 What You Learn

* ✅ Graph search algorithms (Breadth-First Search)
* ✅ Modeling real-world relationships using graphs
* ✅ Efficient path-finding and memory management
* ✅ Working with datasets and real-world actor/movie data

---

## 💡 Acknowledgements

> Information provided by IMDb and used with permission.
