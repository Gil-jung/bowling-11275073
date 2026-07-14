# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository is currently empty of source code — it contains only a Python 3.13 virtualenv (`.venv`) with `pytest` installed. This is a TDD kata project: The Bowling Game Kata (미국식 텐핀 볼링 점수 계산). No source layout, package structure, or test files exist yet, so the structure below should be established as work begins rather than assumed to already exist.

## Environment

- Python 3.13, virtualenv at `.venv` (already created, has `pytest` installed).
- Activate on Windows: `.venv\Scripts\activate` (PowerShell: `.venv\Scripts\Activate.ps1`).
- Run tests: `.venv\Scripts\pytest` (or `pytest` once the venv is activated).
- Run a single test: `pytest path/to/test_file.py::test_name`.

## The kata

Implement a `Game` class for scoring a single game of American ten-pin bowling, given a valid sequence of rolls. Per the kata's scope, do NOT implement:
- Validation that individual rolls are legal (e.g. pin counts within bounds).
- Validation of the number of rolls/frames.
- Mid-game / per-frame score reporting (only the final total score is required).

### Required interface

- `roll(pins: int) -> None` — called once per ball thrown; `pins` is the number of pins knocked down.
- `score() -> int` — returns the total score for the completed game.

### Scoring rules

- A game has 10 frames; each frame is normally 2 rolls to knock down 10 pins.
- **Spare** (10 pins across 2 rolls in a frame): frame score = 10 + pins from the *next 1 roll*.
- **Strike** (10 pins on the first roll of a frame): frame ends immediately; frame score = 10 + pins from the *next 2 rolls*.
- **10th frame**: if it's a spare or strike, one or two bonus rolls are thrown within that same frame (max 3 rolls total in the 10th frame) — these bonus rolls are consumed as the frame's own rolls, not "next frame" lookahead.

This is the classic Kent Beck / Uncle Bob kata — expect the natural implementation to center on iterating frames and, for strikes/spares, looking ahead into the following roll(s) in the flat roll list.

## Development approach

The repo name (`bowling-tdd`) and kata framing indicate this should be built test-first with `pytest`: write a failing test for one scoring case (open frame, spare, strike, all-strikes/"perfect game", 10th-frame edge cases), implement the minimal code to pass, then proceed to the next case.
