# Advent Of Code 2025 — Solutions

This repo contains solutions and small visualization tools for Advent Of Code 2025 puzzles the user worked on locally. The code is intentionally small and focused: each day's solution is a standalone Python script located in `Advent Of Code 2025/`.

## Contents

- `Advent Of Code 2025/Day_1.py` — Safe dial puzzle (Parts 1 & 2) with an interactive Pygame visualization.
- `Advent Of Code 2025/Day_2.py` — Product ID ranges puzzle (Parts 1 & 2).
- `Advent Of Code 2025/Day_3.py`, `Day_4.py`, `Day_5.py` — Other puzzle attempts / helper scripts included in the workspace.
- `day1.txt`, `day2.txt`, ... — Puzzle input files (placed at repository root next to the scripts).
- `requirements.txt` — Python dependencies required for the visualizer.

> Note: file paths and names in this README match the workspace layout used while developing. Adjust paths if you move files.

## Quick Results (from a local run)

- `Day_1.py` outputs:
  - Part 1: `1048`
  - Part 2: `6498`

- `Day_2.py` outputs:
  - Part 1: `28146997880`
  - Part 2: `40028128307`

These numbers were printed by the included scripts when run with the provided input files.

## Requirements

This project requires Python 3.8+ (Python 3.11/3.12/3.13 tested in the local environment). The visualization uses `pygame`.

Install dependencies with pip:

```powershell
python -m pip install -r requirements.txt
```

Or install only `pygame` if you don't need other packages:

```powershell
python -m pip install pygame
```

## How to run

All scripts are plain Python. From the repository root (where `day1.txt` and `day2.txt` live), run the desired script.

Examples (Windows PowerShell):

```powershell
# Run Day 1 (prints answers and launches the Pygame visualization)
cd "c:\VSCODE\Advent Of Code 2025"
python Day_1.py

# Run Day 2 (prints answers for both parts)
cd "c:\VSCODE"
python "Advent Of Code 2025\Day_2.py"
```

Notes:
- `Day_1.py` prints the two part answers to the console and then opens a Pygame window to visualize the dial rotations. Controls in the visualization:
  - `SPACE`: pause / resume animation
  - `Q` or window close: quit
- Each rotation animation uses an internal timing constant (0.05 seconds per rotation in the current code). If the animation is too fast for your system, edit the `rotation_progress` update in `Day_1.py` (the comment explains the constant).

## Visualization details (`Day_1.py`)

- The dial shows numbers `0`–`99` around a circle and a red pointer for the current position.
- The animation is driven by a `rotation_progress` variable that goes from `0.0` to `1.0` for each rotation. The current code advances `rotation_progress` using `1 / (0.05 * FPS)` to approximate `0.05` seconds per rotation with an `FPS` of 120.
- The visualization highlights passing/landing on `0` and shows live counts for:
  - Part 1: how many rotations ended with the dial at `0`.
  - Part 2: how many times the dial passed through `0` during rotations.

## Files of interest

- `Advent Of Code 2025/Day_1.py` — read the top of the file for input path assumptions (`../day1.txt` relative to the script path). The script expects `day1.txt` at the repository root.
- `Advent Of Code 2025/Day_2.py` — reads `../day2.txt` relative to the script path.

If you reorganize the files, update those relative paths accordingly.

## Development / Notes

- The visualization requires a working display (does not headlessly render). On headless systems, skip running `Day_1.py` or run on a machine with a GUI.
- If you plan to share the repository publicly, consider removing large input files or adding `.gitignore` entries for local-only files.

## License

This is a private Advent of Code workspace created for learning and solving puzzles. No license is attached; add one if you intend to publish.

---

If you want, I can also:
- Add a short `Makefile` or PowerShell script to run each day's script easily.
- Add a `requirements.txt` (I included one in this commit) and pin specific versions.
- Generate a short GIF of the Day 1 visualization for README embedding.
