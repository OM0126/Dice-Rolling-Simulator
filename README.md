# Dice Rolling Simulator

A Python-based dice rolling simulator that tracks player scores, counts total attempts, and includes a session management feature that prompts the user to continue every three rolls.

---

# Features

* Roll a virtual dice (1–6)
* Score points when you roll a **6**
* Tracks total number of rolls
* Session control: prompts user after every 3 rolls
* Option to quit anytime

---

# Technologies Used

* Python 3
* `random` module

---

## How It Works

1. User presses **r** to roll the dice
2. A random number between 1 and 6 is generated
3. If the result is **6**, user earns a point
4. After every **3 rolls**, user is asked whether to continue
5. User can quit anytime by pressing **q**



## How to Run

1. Make sure Python is installed
2. Save the file as `dice.py`
3. Run the program:

```bash id="run321"
python dice.py
```

---

# Example Output

```id="ex555"
Welcome to Dice rolling simulator
press r to roll the dice and q to quit: r
u rolled a dice: 6
congrats you rolled and u got a 6
u scored 1 points
u have rolled the dice 1 times
```

---

## Notes

* Only rolling **6** increases your score
* Input is case-insensitive
* After 3 rolls, you must choose to continue or exit

---

## Future Improvements

* Add multiplayer mode
* Add leaderboard system
* GUI version using Tkinter
* Sound effects 
* Store scores in a file

---

# Author

OM
