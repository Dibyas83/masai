"""
# Project-Rollout (M2)

# **Module 2 Projects**

*Release Date: 7 **May 2025**  |  Final Submission: **17 May 2025 (23 : 59 IST)***

> Choose ONE of the four projects below and implement it completely in Python.
>
>
> This document breaks every project into **bite-sized steps** and explains exactly **what to build, what to store, how to test, and how to submit**.
>

---

---

# Project 1 – 🧬 *Conway’s Game of Life* Interactive Visualiser

### 1. Learning Goals

- Apply **2-D arrays / sets** for state storage
- Use an **update-all-at-once** algorithm (rules below)
- Practise **Tkinter / Pygame / Matplotlib** for simple graphics
- Persist patterns via **file I/O**

### 2. Rules Recap

For each generation every cell looks at its **eight neighbours**:

| **Condition** | **Next State** |
| --- | --- |
| < 2 live neighbours | Dies (under-population) |
| 2 or 3 live neighbours | Lives on |
| > 3 live neighbours | Dies (over-population) |
| Exactly 3 live neighbours & currently dead | Becomes alive |

### 3. Implementation Steps

| **Step** | **What to build** |
| --- | --- |
| **3.1 Bootstrap** | `life.py --width 60 --height 30 --fps 10` parses CLI args (use **argparse**). |
| **3.2 Model** | Start with `board = [[0]*W for _ in range(H)]` OR `live = set[(x,y)]`. |
| **3.3 Logic** | Write `next_gen(board)` that returns a **fresh board** (do NOT mutate in-place). Unit-test with the *Blinker* and *Glider* patterns in `tests/test_blinker.py`. |
| **3.4 View** | **Option A – Pygame**: draw each live cell as a filled square.   **Option B – Tkinter**: `Canvas.create_rectangle`. |
| **3.5 Controls** | *Space* = Play/Pause, *N* = single-step, *C* = clear, *R* = random fill, *S* = save pattern, *L* = load pattern. |
| **3.6 Persistence** | Save to `patterns.txt` one line per `(x,y)`, e.g. `10,15`.  Load by reading and re-populating the board. |
| **3.7 Polishing** | Add FPS label, live-cell counter, window resize, colour scheme (`colorama` or Pygame colours). |

### 4. File Formats

- **`patterns.txt`** – plain text list of live-cell coordinates

    ```
    # Pattern: Glider
    1,0
    2,1
    0,2
    1,2
    2,2

    ```


### 5. Sample Run

```
$ python life.py --width 40 --height 20 --fps 6
┌ Game of Life ──────────────────────────────┐
│ Space:▶/⏸  N:Step  R:Random  S:Save  L:Load│
│ Generation 42      Live cells: 117         │
└─────────────────────────────────────────────┘

```

[*The below image is just for your reference, not applicable for above sample run*]

![game-of-life-loop-cropped.gif](attachment:d632c394-a5ab-4636-a0de-ae5eeac3e5c2:game-of-life-loop-cropped.gif)

---

# Project 2 – 📚 *Library Management System*

### 1. Learning Goals

- Design a **mini-database** with CSV files
- Model **many-to-many** (members ↔ loans)
- Practise **login, roles, password hashing**
- Implement **CRUD** operations & due-date logic

### 2. System Roles

| **Role** | **Permissions** |
| --- | --- |
| **Librarian** | add / delete books, register members, issue/return, view overdue |
| **Member** | search catalogue, check availability, see own loan history |

### 3. File Schema

| File | Columns | Example Line |
| --- | --- | --- |
| `books.csv` | ISBN,Title,Author,CopiesTotal,CopiesAvailable | `9780132350884,Clean Code,Robert C. Martin,5,3` |
| `members.csv` | MemberID,Name,**PasswordHash**,Email,JoinDate | `1001,Ananya Singh,$2b$12$...Q3,ananya@mail.com,2025-05-10` |
| `loans.csv` | LoanID,MemberID,ISBN,IssueDate,DueDate,ReturnDate | `42,1001,9780132350884,2025-05-15,2025-05-29,` |

> 🔐 Hash passwords with bcrypt (pip install bcrypt).
>

### 4. Step-by-Step Build Plan

| **Phase** | **Tasks** |
| --- | --- |
| **4.1 Setup** | `models.py` (Book, Member, Loan dataclasses) & `storage.py` (CSV read/write helpers). |
| **4.2 Auth** | `auth.py` with `register_member()` & `login(role)`. Store logged-in user in `session` dict. |
| **4.3 Librarian Menu** | 1) Add book 2) Remove book 3) Issue book 4) Return book 5) View overdue list 6) Logout. |
| **4.4 Member Menu** | 1) Search catalogue (title / author keyword) 2) Borrow book (if available) 3) My loans 4) Logout. |
| **4.5 Business Rules** | *Issue*: decrement `CopiesAvailable`, create loan, due = `issue+14d`.  *Return*: fill `ReturnDate`, increment copies. |
| **4.6 Overdue Report** | Select loans where `ReturnDate=''` **and** `DueDate < today`; pretty-print table, e-mail reminder optional. |
| **4.7 Validation & Errors** | - Invalid ISBN - Duplicate member IDs - Negative copies - Password mismatch. |
| **4.8 Tests** | `pytest tests/test_issue_return.py` (issue then return restores availability). |
| **4.9 Argparse** | `--data-dir ./data` flag to load CSVs from custom folder. |

### 5. Console Snapshot

```
=== Librarian Dashboard ===
1. Add Book
2. Register Member
3. Issue Book
4. Return Book
5. Overdue List
6. Logout
> 3
ISBN to issue: 9780132350884
Member ID: 1001
✔ Book issued. Due on 29-May-2025.

```

---

# Project 3 – 🗺️ *Travelling Salesman City-Tour Optimizer*

### 1. Learning Goals

- Use **CSV parsing & geodesic maths**
- Implement classic **TSP heuristics**
- Write **re-usable modules** (`distance.py`, `tsp_solver.py`)
- Export results in **GeoJSON** for mapping

### 2. Input & Output

| **File** | **Columns** | **Sample** |
| --- | --- | --- |
| `places.csv` | Name,Lat,Lon | `Eiffel Tower,48.8584,2.2945` |
| `route.geojson` | GeoJSON `LineString` of the optimal path | *(auto-generated)* |

### 3. Implementation Road-Map

| **Step** | **Details** |
| --- | --- |
| **3.1 Read CSV** | Store as `Place` objects (`namedtuple`). |
| **3.2 Distance Matrix** | Haversine function → 2-D list `dist[i][j]`. |
| **3.3 Greedy Solver** | Start at chosen index, repeatedly pick nearest unvisited. |
| **3.4 Improve** | Implement **2-opt**: swap two edges if it shortens path; iterate until no gain. |
| **3.5 CLI** | `python tsp.py --csv places.csv --start "Eiffel Tower" --return` |
| **3.6 Output** | Print ordered list & total km; dump GeoJSON so user can drag-drop into Google Maps. |
| **3.7 Extra Points** | Matplotlib scatter-plot with arrows; time-window filtering; command-line flag `--algo simulated-annealing`. |

### 4. Example Session

```
Optimal tour (returns to start):
1) Eiffel Tower
2) Louvre Museum
3) Notre-Dame
4) Arc de Triomphe
5) Eiffel Tower
Total distance: 12.4 km
Route written to route.geojson

```

---

# Project 4 – 💼 *Portfolio Optimizer (0/1 Knapsack)*

### 1. Learning Goals

- Read **CSV market data**
- Apply **dynamic programming** to optimisation
- Visualise **efficient frontier** (risk vs return)
- Handle **multiple constraints** (capital, risk)

### 2. Data Files

| File | Purpose | Columns |
| --- | --- | --- |
| `assets.csv` | Input universe | `Ticker,ExpectedReturn(%),RiskScore(0-100),Price` |
| `prices.csv` *(optional)* | Raw daily data for computing μ & σ | date,ticker,close |

### 3. Build Steps

| Phase | Tasks |
| --- | --- |
| **3.1 Pre-processing** | Convert returns `% → float`; convert capital input to numeric. |
| **3.2 Single-Constraint DP** | Classic 0/1 knapsack on `Price`. Table size `(n+1) × (C+1)`. |
| **3.3 Risk Filter** | After DP pick, sum risk; if > tolerance, discard worst-return asset and retry (simplest). |
| **3.4 Multiple Runs** | Sweep risk tolerance 0→100 in steps of 5 to plot frontier. |
| **3.5 Plot** | Matplotlib scatter: x=risk, y=expected return. Save `frontier.png`. |
| **3.6 CLI** | `optimizer.py --capital 100000 --risk 40 --csv assets.csv --plot`. |
| **3.7 Unit Tests** | verify DP picks higher return for same cost, using a mini fixture of 5 assets. |

### 4. Console Demo

```
$ python optimizer.py --capital 75000 --risk 35
Selected 6 assets:
INFY  TCS  HDFCBANK  ITC  MARUTI  RELIANCE
Total Cost : ₹73 940
Exp Return : 16.8 %
Risk Score : 32
Frontier plot saved to frontier.png

```

---

## Submission – Step-by-Step Guide

1. **Finish Code**
    - All required features work, README updated, sample CSV / TXT files included.
2. **Run Tests**
    - `pytest -q` must be **green**.
3. **Record Demo Video**
    - Show : running the program, key features, data files on disk, error-handling example.
    - Talk : what algorithm / data-structure you used, biggest challenge, coolest extension.
    - Upload & copy the link (you can use G-drive or Youtube, make sure access is public)
4. **Push to GitHub**
    - Make sure the repository is public.
5. **Submit on LMS**
    - Paste GitHub URL + Video URL. Click **Submit**. Ensure both are public *(Submission assignment will get released on LMS soon)*

---

### Support & Resources

- **Project Query Sessions** – 8th, 9th and 10th May 7-8 PM on Zoom (link in LMS).
- Discussions – Raise queries, screenshots, or design doubts.
- **Cheat-sheets** –
    - `argparse`: [docs.python.org/argparse](https://docs.python.org/3/library/argparse.html)
    - `csv` module: [docs.python.org/csv](https://docs.python.org/3/library/csv.html)
    - Haversine formula: many references online

> Remember: these capstones are showcase pieces for your résumés and GitHub portfolios—write clean code, commit often, and most importantly, enjoy the build! 🎉
>

Good luck 🚀

"""