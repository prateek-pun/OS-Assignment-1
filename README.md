# Linux Process Management Experiment

This project contains Python scripts to simulate Linux process creation and management using the `os` module.

## Project Overview

The experiment covers:
- Creating child processes
- Executing commands via `exec()`
- Simulating zombie and orphan processes
- Inspecting process details from `/proc`
- Demonstrating process prioritization using `nice()`

## Files

- `task1_process_creation.py` – Create and manage child processes
- `task2_exec_command.py` – Execute Linux commands in child processes
- `task3_zombie_orphan.py` – Simulate zombie and orphan processes
- `task4_inspect_proc.py` – Inspect process info from `/proc`
- `task5_priority.py` – Process priority and CPU scheduling demonstration

## Requirements

- Python 3
- Linux environment (Ubuntu, WSL, or similar)

## How to Run

Open your terminal and run each script individually, for example:

`python3 task1_process_creation.py`

Follow prompts on the screen.

## Notes

- For Task 3, use another terminal and run `ps -el | grep defunct` to monitor zombie processes.
- Scripts use Linux-specific system calls; they won't run on Windows command prompt natively.
- Use `Ctrl+C` to stop any long-running task.

