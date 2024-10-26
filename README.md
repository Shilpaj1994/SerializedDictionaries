# Sets and Serialized Dictionaries

This project contains implementations for merging dictionaries and validating nested dictionary structures.

## Project Structure

- `student_merge.py`: Contains functions for merging dictionaries using defaultdict and Counter.
- `student_code.py`: Contains a function for validating nested dictionary structures.
- `test_merge.py`: Contains test cases for the merge functions.
- `test_validate.py`: Contains test cases for the validate function.
- `main.py`: Main script to run the project (if applicable).

## Features

1. Merge multiple dictionaries using defaultdict
2. Merge multiple dictionaries using Counter
3. Validate nested dictionary structures against a template

## Requirements

- Python 3.12
- pytest (for running tests)
- pylint (for code quality checks)

## Installation

1. Clone this repository:   ```
   git clone <repository-url>
   cd SetsDictionaries   ```

2. Create a virtual environment (optional but recommended):   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`   ```

3. Install the required packages:   ```
   pip install pytest pylint   ```

## Run tests
```
pytest .
```

