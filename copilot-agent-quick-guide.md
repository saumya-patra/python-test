# Copilot Chat Agent: Quick Guide

## 1. Open the project

Open your VS Code workspace and select a folder like:
- a Python project
- a small script folder
- a learning folder such as this one

## 2. Open Copilot Chat

- Open the Copilot Chat panel in VS Code
- Switch to Agent mode if it is available

## 3. Give a clear task

Keep the task narrow and specific. Use prompts like:

> Create a Python script that reads a CSV file and keeps only rows where the status is Approved.

Or:

> Build a small agent that reads input.txt and prints a summary.

## 4. Add project context

Tell Copilot exactly how the agent should behave:

> Use only the Python standard library. Add a main() function. Keep the code simple and readable. Validate the input file before processing.

## 5. Let Copilot build the first version

Ask for the initial version, for example:

> Create the first working version of this agent in the project folder and include a sample input file.

## 6. Test it

Run the script from the terminal:

```bash
python sample_agent.py sample_input.csv output.csv
```

Check the output. If something fails, ask Copilot to fix it.

## 7. Refine with follow-up prompts

Good follow-ups:

> Add error handling.
> Add CLI arguments for input and output file paths.
> Make the script print a summary after writing the file.
> Add docstrings.

## 8. Keep the scope small

Good agents start with one job, such as:
- filter CSV rows
- parse text file
- rename files
- summarize logs
- fetch API data

## 9. Example prompt

> Act as a small Python coding agent. Build a script that reads a CSV file, keeps only approved rows, and writes them to a new CSV file. Use standard Python libraries only. Include a main() function and basic validation.

## 10. Best practice

The best small agent is:
- specific
- easy to test
- limited to one task
- simple to run
- easy to improve

This approach works well for learning and for real projects.
