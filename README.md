# JobFetch 🔍

A simple Python-based command-line tool to search and save job listings using the Reed.co.uk API.

## Features

- Search job listings by keyword, location, and salary.
- Save results to a local text file.
- Supports multiple keywords in a single command.
- Handles common API errors (timeout, connection, HTTP errors).
- Lightweight, fast, and customizable.

## Usage

```bash
python jobhawk.py Python Developer -l London -sal 30000 -r 50 -s jobs.txt
