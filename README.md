
<div align="center">
  <h1>🔝 Higher-Lower Follower Game</h1>
</div>

<p align="center">
  <em>A fun Python console game where you guess which celebrity or brand has more followers. Keep your streak alive and beat your high score!</em>
</p>

---

## 📌 Overview

This is a simple **Higher-Lower style game** written in Python.  
It picks two random accounts from a data source and asks you to guess which one has more followers.  
You keep playing until you make a wrong guess.

---

## 🧩 How It Works

- The game randomly selects two accounts from `project_data.py`.
- Each account has a name, description, country, and follower count.
- You see details for **A** and **B** and guess which has more followers.
- If you guess right, your score increases and the game continues.
- If you’re wrong, your final score is shown.

---

## 🚀 How to Run

1️⃣ **Clone the repository**

```bash
git clone https://github.com/yourusername/higher-lower-game.git
cd higher-lower-game
```

2️⃣ **Check you have the required files**

- `main.py` (or `higher_lower.py`) — Your main game script.
- `art.py` — Contains ASCII art `logo` and `vs`.
- `project_data.py` — Contains the `data` list with accounts.

Example `project_data.py`:
```python
data = [
  {
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
  },
  {
    'name': 'Cristiano Ronaldo',
    'follower_count': 215,
    'description': 'Footballer',
    'country': 'Portugal'
  },
  ...
]
```

3️⃣ **Run the game**

```bash
python main.py
```

---

## 📄 Example Session

```
Compare A: Instagram, a Social media platform, from United States
vs
Compare B: Cristiano Ronaldo, a Footballer, from Portugal
Who has more followers? Type 'A' or 'B': A
You're right! Current score: 1.
...
Sorry, that's wrong. Final score: 4
```

---

## ✅ Requirements

- Python 3.x
- No external libraries needed (uses only built-in modules)

---

## 💡 Ideas to Improve

- Add clear screen support for better UX.
- Make sure A and B are never the same account.
- Add a score history or leaderboard.
- Add more data to `project_data.py`.

---

## 📬 License

This project is free to use and modify.  
Feel free to fork it and make your own version!

---

**Good luck guessing! 🔝✨**
