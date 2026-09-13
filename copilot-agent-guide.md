# Small Agent with Copilot Chat: Step-by-Step Guide

This guide explains how to create a small agent using Copilot Chat in VS Code.

## 1) Install the tools

Make sure you have:
- VS Code
- GitHub Copilot extension
- GitHub Copilot Chat
- A project folder open

If needed, sign in to GitHub and enable Copilot.

## 2) Open a project and define the task

Create a small folder for your idea, for example:
- a Python script
- a file organizer
- a weather helper
- a task manager
- a CSV-to-JSON converter

Choose one simple task so the agent stays focused.

## 3) Switch to Agent mode

In Copilot Chat:
- Open the chat panel
- Choose Agent mode, if available
- Do not use just Ask or Edit for this workflow

Agent mode lets Copilot act more like a helper that can:
- inspect files
- edit code
- run commands
- suggest next steps

## 4) Give the agent a clear job

Use a prompt like this:

> Create a small Python agent for this project. It should read a CSV file, filter rows where the status is “Approved,” and save the result to a new CSV file. Keep the code simple, add docstrings, and include a main function. Use only standard Python libraries.

The better the instructions, the better the output.

## 5) Add project context

Tell Copilot what the project should do and what files exist. For example:

> This project is a Python utility. Use the current folder as the working directory. Keep the script runnable with `python app.py`. Do not use external packages.

You can also paste:
- sample input data
- expected output
- error handling requirements
- coding style preferences

## 6) Let Copilot scaffold the agent

Ask it to create:
- the main script
- a config or settings file if needed
- README notes
- sample input/output

Example prompt:

> Create the initial version of the agent in this project, including the main script and a sample CSV file.

Then review the generated code carefully.

## 7) Review and refine

Once Copilot writes code, check:
- does it match your task?
- are the functions clear?
- are there bugs?
- does it use the right libraries?
- can it run?

Then refine with prompts like:

> Improve the error handling.  
> Add a CLI argument for the input file path.  
> Make the output file name optional.  
> Add unit tests for the filter function.

## 8) Run the agent and verify

Open the terminal and run it:

```bash
python app.py
```

or:

```bash
python app.py input.csv output.csv
```

Check whether it:
- reads the files correctly
- handles invalid input
- writes the expected output
- behaves consistently

## 9) Save reusable instructions

If you want this as a reusable “agent,” add a custom instruction file or keep a prompt template.

Example prompt template:

> You are a small Python coding agent. Work in this project folder. Keep code simple and readable. Prefer standard library solutions unless a dependency is required. Always add a `main()` function. Validate with a quick run after creating code.

This gives Copilot a consistent behavior every time.

## 10) Good beginner pattern

A strong simple agent recipe is:

1. Define the task
2. Give project context
3. Ask for a minimal working version
4. Run it
5. Improve with follow-up prompts
6. Keep it narrow and clear

## Example prompt you can copy

> Act as a small coding agent for this project. Build a Python script that reads a CSV file, keeps only rows where `status == "Approved"`, and writes the filtered rows to a new file. Include a `main()` function, basic validation, and clear comments. Use only the Python standard library. After creating the code, run it once to verify it works.

## Best practice

Keep the first version small:
- one job
- one script
- one input/output
- clear instructions

Once that works, expand it into a more advanced agent with:
- multiple commands
- better prompts
- project rules
- reusable templates

## Quick summary

The easiest way to create a small agent is:
- open Copilot Chat in Agent mode
- give it a focused task
- provide project context
- let it build the first version
- test it
- refine with follow-up prompts

This keeps things simple while still giving you a working AI assistant for your code project.
