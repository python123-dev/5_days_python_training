# 5-Day Python Training

Hands-on Jupyter notebooks and scripts from a 5-day Python training course, covering
core language fundamentals, OOP, file/exception handling, web requests, databases, GUI
programming, a small Flask app, NumPy/Pandas/data visualization, and regex/concurrency.

## Prerequisites

- Python 3.13 (developed/tested against 3.13.14)
- pip
- (Optional, only for `Day-3/mysql.ipynb`) a local MySQL server

## Setup

```bash
# from the project root
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Then launch Jupyter to work through the notebooks:

```bash
jupyter lab
# or
jupyter notebook
```

## Project Structure

```
5_days_python_training/
├── Day-1/   Python fundamentals
├── Day-2/   OOP, exceptions, files, functional programming
├── Day-3/   HTTP requests, MySQL, serialization, GUIs (tkinter/PyQt5), Flask app
├── Day-4/   NumPy, Pandas, data visualization, EDA
├── Day-5/   Regex, threading, multiprocessing
├── requirements.txt
└── .gitignore
```

## Day-by-Day Contents

### Day-1 — Python Fundamentals
- `python_basics.ipynb` — core syntax and language basics
- `datatypes.ipynb` — built-in data types
- `if_for.ipynb` — conditionals and loops
- `task.ipynb` — practice exercises

### Day-2 — OOP & File Handling
- `class_obj.ipynb` — classes and objects
- `inheritance.ipynb` — inheritance
- `abstract_base_class.ipynb` — abstract base classes
- `exception_handling.ipynb` — exception handling
- `file_handling.ipynb`, `file_text_handle.ipynb` — reading/writing files
- `functional_programming.ipynb` — functional programming concepts
- `task.ipynb` — practice exercises
- `bank_module.py` / `use_bank_module.py` — a small bank account module and a script that
  imports and uses it. Run with:
  ```bash
  python Day-2/use_bank_module.py
  ```

### Day-3 — Requests, Databases, GUIs, Flask
- `http_requests.ipynb` — the `requests` library
- `mysql.ipynb` — connecting to MySQL with `mysql-connector-python`
  (requires a local MySQL server running; the notebook connects to
  `host='localhost', user='root'` with an empty password by default — update these to match
  your local MySQL setup)
- `serialization.ipynb` — JSON/pickle serialization
- `task.ipynb` — practice exercises
- `tkinter_widgets.py`, `tkinter_layout.py`, `tkinter_events.py` — Tkinter GUI examples. Run
  any of them directly, e.g.:
  ```bash
  python Day-3/tkinter_widgets.py
  ```
- `pyqt_basics.py` — PyQt5 GUI example:
  ```bash
  python Day-3/pyqt_basics.py
  ```
- `flask_app/` — a small Flask project (application factory pattern with blueprints and a
  SQLite database):
  ```bash
  cd Day-3/flask_app
  python app.py
  ```
  Then open http://127.0.0.1:5000 in a browser. `app.py` builds the app via `create_app()`,
  registers `blueprints/views.py` (HTML views) and `blueprints/api.py` (JSON API), and
  `models.py` initializes the SQLite database (`customers.db`).

### Day-4 — NumPy, Pandas & Data Visualization
- `numpy_basics.ipynb` — NumPy arrays and operations
- `pandas_basics.ipynb` — Pandas Series/DataFrames
- `data_vis.ipynb` — plotting with Matplotlib/Seaborn
- `eda_case_study.ipynb` — an exploratory data analysis case study

### Day-5 — Regex & Concurrency
- `regex.ipynb` — regular expressions
- `threads.ipynb` — multithreading
- `multi_t.ipynb` — more multithreading examples
- `task.ipynb` — practice exercises, using `mp_worker.py` (a `multiprocessing` worker module):
  ```bash
  python Day-5/mp_worker.py
  ```

## Notes

- Notebook checkpoint files (`.ipynb_checkpoints/`), `__pycache__/`, and the virtual
  environment (`.venv/`) are excluded from version control via `.gitignore`.
- `Day-3/mysql.ipynb` and `Day-3/task.ipynb` use local development MySQL credentials
  (`user='root'`, empty password) — these are for a local dev database only and should be
  updated to match your own environment before running.
