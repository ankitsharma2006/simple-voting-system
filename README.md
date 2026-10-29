# Simple Voting System

A complete implementation of the **Simple Voting System** matching the three core functional specifications:
1. **Add Candidates** – Enter candidate names
2. **Vote** – Cast a vote
3. **Result** – Show vote count & identify winners

---

## 📁 Included Implementations

This project contains 3 ready-to-run options depending on your preference:

| File | Type | Description |
| :--- | :--- | :--- |
| **[`index.html`](./index.html)** | **Interactive Web Application** | Open in any browser (Chrome, Edge, Firefox) with zero setup. Features live progress bars, candidate management, winner badges, and local persistence. |
| **[`gui_voting_system.py`](./gui_voting_system.py)** | **Desktop GUI (Tkinter)** | Native desktop window with 3 responsive panels matching the workflow. |
| **[`voting_system.py`](./voting_system.py)** | **Command-Line Interface (Python)** | Pure Python terminal program with clean interactive menu and tabular output. |

---

## 🚀 How to Run

### 1. Web Application (Recommended for instant visual demo)
- Simply double-click **`index.html`** in this folder, or right-click and choose **Open with > Google Chrome / Microsoft Edge**.

---

### 2. Desktop GUI Application (Tkinter)
Run via PowerShell or Command Prompt:
```bash
python gui_voting_system.py
```
- **Panel 1 (Add Candidates):** Type a candidate's name and click **Add** (or press Enter).
- **Panel 2 (Vote):** Select a candidate and click **Cast Vote**.
- **Panel 3 (Result):** View real-time vote totals, percentage share, and current leader / winner.

---

### 3. Command-Line Application (Python)
Run via PowerShell or Command Prompt:
```bash
python voting_system.py
```

**Interactive Menu:**
```text
===================================
       SIMPLE VOTING SYSTEM        
===================================
1. Add Candidates (Enter names)
2. Vote (Cast a vote)
3. Result (Show vote count)
4. View All Candidates
5. Reset All Votes
6. Exit
===================================
```

---

## ✨ Features
- **Duplicate Prevention:** Case-insensitive check to avoid duplicate candidates.
- **Vote Validation:** Ensures voters select existing candidates before voting.
- **Percentage Calculation:** Accurately computes voter share and handles ties.
- **Reset Support:** Ability to reset vote tallies without re-entering candidate names.
