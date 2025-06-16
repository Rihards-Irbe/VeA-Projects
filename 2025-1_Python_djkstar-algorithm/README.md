# 2025-1_Python_djkstar-algorithm

## Overview
This Python script implements **Dijkstra’s** algorithm to find the shortest route between two Latvian cities based on given distances. It reads distance data from an Excel file (`distances.xlsx`) if available, otherwise, it uses default values. The output includes the shortest distance and the path taken.

## Features
- Load custom distance data from an Excel file `distances.xlsx`.
- Automatically fall back to default distance values if the Excel file is missing or unreadable.
- Demonstrates how modifying distances influences the chosen shortest path.

## How to Run
1. Make sure this dependency is installed:

```pip install pandas
   ```

2. **Optional** Place `distances.xlsx` in the same directory to use custom data.

3. Run the file using any Python compatible compiler or interpreter.
