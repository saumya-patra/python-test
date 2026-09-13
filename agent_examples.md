# Agent Examples in this Project

This folder contains three simple agent patterns you can use with Copilot Chat and VS Code.

## 1) CSV filter agent

File: `sample_agent.py`

Purpose:
- Reads a CSV file
- Keeps only approved rows
- Writes a filtered CSV file

Run:

```bash
python sample_agent.py sample_input.csv filtered_output.csv
```

## 2) Text file agent

File: `text_agent.py`

Purpose:
- Reads a text file
- Counts words, lines, and characters
- Prints summary information

Run:

```bash
python text_agent.py sample_notes.txt
```

## 3) CLI prompt agent

File: `cli_agent.py`

Purpose:
- Accepts a file path and keyword from the command line or prompt
- Counts keyword occurrences
- Prints a quick analysis

Run:

```bash
python cli_agent.py sample_notes.txt AI
```

## 4) Multi-command assistant agent

File: `multi_command_agent.py`

Purpose:
- Runs as a small command-based assistant
- Supports commands such as `help`, `count`, `search`, and `summary`
- Works like a lightweight local agent

Run:

```bash
python multi_command_agent.py --file sample_notes.txt --command count
python multi_command_agent.py --file sample_notes.txt --command search --keyword AI
```

## Best practice

Start with one focused job, test it, and then expand. This approach keeps the agent simple and easy to understand.
