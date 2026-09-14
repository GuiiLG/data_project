# Project 1 — FIFA 21 Data Cleaning

## 1. Project Context

You are given a raw dataset containing information about FIFA 21 football players.

The dataset should be treated as if it were received from an external system with unknown data quality.

Your goal is **not simply to "clean a CSV"**.

The goal is to develop the ability to:

> Receive unknown raw data → investigate it → identify problems → make decisions → transform the data → validate the result → produce reliable structured data.

This project is intentionally designed to make you investigate the data yourself.

Do not assume beforehand that you know what is wrong with the dataset.

---

# 2. Main Learning Objectives

This project is primarily about strengthening your Python fundamentals and developing a Data Engineering mindset.

By the end of the project, you should have practiced:

* Reading and writing files
* Working with CSV files
* Working with lists and dictionaries
* String manipulation
* Type conversion
* Regular expressions when appropriate
* Exception handling
* Functions and modular code
* Data validation
* Data cleaning
* Data normalization
* Detecting inconsistencies
* Handling missing values
* Detecting duplicates
* Investigating unknown data
* Making data-quality decisions
* Generating reports
* Designing a small, reliable data-processing pipeline

The project should force you to understand the data instead of relying on a library to automatically do the work for you.

---

# 3. Main Restriction — Pure Python

For this project, **do not use Pandas, NumPy, Polars, or other DataFrame/data-processing libraries.**

You must implement the data processing using Python and its standard library.

You may use standard-library modules such as:

```text
csv
json
pathlib
datetime
re
collections
logging
statistics
math
```

You do not need to use all of them.

Use a library only when it actually makes sense for the problem.

The purpose of this restriction is to make you practice working directly with:

* lists
* dictionaries
* strings
* files
* loops
* conditions
* functions
* exceptions
* data structures

Do not try to recreate Pandas.

The objective is to understand what is happening underneath the abstractions.

---

# 4. Important Principle

Do not begin by writing a cleaning script.

First investigate the dataset.

Your workflow should be approximately:

```text
Raw Dataset
    ↓
Investigation
    ↓
Identify Problems
    ↓
Define Cleaning Rules
    ↓
Implement Transformations
    ↓
Validate Results
    ↓
Generate Processed Dataset
    ↓
Generate Data Quality Report
```

The important part is the reasoning between each step.

---

# 5. Phase 1 — Data Investigation

Before modifying anything, inspect the dataset.

You should discover what the data actually looks like.

Investigate things such as:

* Number of records
* Number of columns
* Column names
* Example records
* Missing values
* Empty strings
* Duplicate records
* Potential identifiers
* Apparent data types
* Inconsistent formats
* Unexpected characters
* Whitespace problems
* Newline characters
* Numeric values stored as strings
* Values containing multiple pieces of information
* Different units
* Different representations of the same concept
* Suspicious values
* Unexpected formats

Do not assume that a column is problematic just because it looks unusual.

Investigate it first.

For example, if a value looks strange, ask:

> Is this actually invalid, or is it simply represented differently?

---

# 6. Investigate Before Searching for Solutions

You are allowed and encouraged to research specific Python concepts when necessary.

For example:

```text
How do I use csv.DictReader?
How do I remove newline characters from a string?
How do I use regular expressions in Python?
How can I convert a string containing "M" into a number?
How does datetime.strptime work?
```

This is allowed.

However, avoid searching for complete solutions to the project.

Avoid searches such as:

```text
How to clean the FIFA 21 dataset
FIFA 21 dataset cleaning solution
FIFA 21 messy dataset Python solution
FIFA 21 Kaggle cleaning notebook
```

Do not copy an existing cleaning notebook or tutorial.

The objective is for **you to discover the problems and decide how to solve them.**

---

# 7. Phase 2 — Identify Data Quality Problems

After investigating the dataset, create a list of the problems you discovered.

For each problem, determine:

1. What is wrong?
2. Which column(s) are affected?
3. How many records are affected?
4. Is the problem actually invalid data?
5. What should the correct representation be?
6. What should happen when the value cannot be converted or corrected?
7. Why is your chosen solution appropriate?

Examples of possible problems include:

* Numeric values stored as strings
* Currency values containing symbols
* Values using `K`, `M`, or other suffixes
* Height represented using feet/inches
* Weight represented using different units
* Special characters
* Extra whitespace
* Embedded newline characters
* Inconsistent date formats
* Empty values
* Missing values
* Duplicate IDs
* Invalid numeric values
* Unexpected strings
* Fields containing multiple pieces of information

These are examples only.

You must discover the actual problems in the dataset yourself.

---

# 8. Phase 3 — Define Cleaning Rules

Before implementing the transformations, define what your program should do.

For every important problem, establish a rule.

For example:

```text
Problem:
Currency values contain "€", "K", and "M".

Decision:
Convert all monetary values into a single numeric representation.

Reason:
A numeric representation makes the values easier to process and compare.
```

Or:

```text
Problem:
Some records contain missing values.

Decision:
Do not automatically replace every missing value.

Reason:
The correct treatment depends on the meaning and importance of the column.
```

Your decisions should be based on the actual data.

Do not clean data simply because it "looks ugly."

The goal is to make the data **consistent, meaningful, and usable.**

---

# 9. Cleaning and Normalization

Implement the cleaning rules you defined.

The processed dataset should have consistent representations.

Possible transformations may include:

* Removing unnecessary whitespace
* Normalizing text
* Removing unwanted characters
* Converting numeric strings into numbers
* Converting monetary values into numeric values
* Converting dates into a consistent format
* Converting units into a common unit
* Splitting fields when appropriate
* Handling missing values
* Normalizing categorical values
* Removing or rejecting invalid records
* Preserving values that are unusual but valid

For example, a value such as:

```text
€110.5M
```

might need to become a numeric representation.

A value such as:

```text
5'11"
```

might need to be converted into a consistent measurement.

But these are examples of possible problems, not mandatory transformations.

The dataset itself should determine what you actually need to change.

---

# 10. Invalid vs. Unusual Data

One of the most important goals of this project is learning to distinguish between:

```text
Invalid data
```

and

```text
Unusual but valid data
```

Do not remove a value merely because it looks strange.

For example, consider a player's age.

A value such as:

```text
120
```

would probably be invalid.

But a player with an unusual position, nationality, salary, or rating is not necessarily invalid.

Your program should make decisions based on the meaning of the data.

Whenever possible, avoid arbitrary assumptions.

---

# 11. Data Validation

After cleaning the data, validate the result.

Do not assume that the transformation worked simply because the program finished without errors.

Check the processed dataset for problems.

Depending on the dataset, validation should include things such as:

* Number of records
* Number of rejected records
* Number of missing values
* Number of duplicate IDs
* Expected columns
* Expected data types
* Invalid numeric values
* Negative values where they make no sense
* Impossible measurements
* Invalid dates
* Unexpected formats
* Empty required fields
* Unexpected values after transformation

Examples:

```text
Age < 0
Weight <= 0
Height <= 0
Negative monetary values
Duplicate player IDs
Invalid dates
Missing required identifiers
```

Again, these are examples.

Define validation rules according to the meaning of the dataset.

---

# 12. Raw Data Must Never Be Modified

The original dataset must remain untouched.

Organize the project so that raw and processed data are separated.

Recommended structure:

```text
project/
│
├── data/
│   ├── raw/
│   │   └── players.csv
│   │
│   └── processed/
│       └── players_clean.csv
│
├── reports/
│   └── data_quality.txt
│
├── src/
│   ├── ...
│
└── README.md
```

The raw file should be treated as immutable input.

Your program reads the raw dataset and produces new outputs.

---

# 13. Data Quality Report

Your program must generate a data quality report.

The report should contain useful information about what happened during processing.

At minimum, include:

* Total number of records received
* Number of records successfully processed
* Number of rejected records
* Number of missing values
* Number of duplicate records or IDs
* Number of invalid values
* Important transformations performed
* Important problems discovered
* Any relevant warnings
* Any limitations or unresolved problems

The exact structure of the report is up to you.

The report should answer questions such as:

```text
How much data did I receive?

How much data did I successfully process?

How much data was rejected?

What problems did I find?

What transformations did I perform?

Why did I perform them?

What problems remain?
```

---

# 14. Error Handling

The program should handle expected errors gracefully.

Consider situations such as:

* File does not exist
* File is empty
* CSV is malformed
* A row has an unexpected number of fields
* A value cannot be converted
* A date has an unexpected format
* A numeric field contains invalid text
* Output file cannot be written
* Required column is missing

The program should not simply crash without useful information.

Use exceptions where appropriate.

However, do not use:

```python
try:
    ...
except:
    pass
```

simply to hide problems.

Errors should either be handled meaningfully or reported clearly.

---

# 15. Code Organization

Avoid putting the entire project inside one huge function or one giant script.

Separate responsibilities when appropriate.

For example:

```text
read data
    ↓
investigate data
    ↓
clean data
    ↓
validate data
    ↓
write processed data
    ↓
generate report
```

You may organize your code into modules such as:

```text
src/
├── reader.py
├── investigation.py
├── cleaning.py
├── validation.py
├── writer.py
└── report.py
```

This is only a suggestion.

Do not create unnecessary abstraction just for the sake of having many files.

The organization should make the program easier to understand and maintain.

---

# 16. Reproducibility

Your program should be able to process the dataset from start to finish without requiring manual modification of the raw file.

Ideally:

```text
raw dataset
      ↓
run program
      ↓
processed dataset
      +
data quality report
```

The goal is to create a repeatable process.

If the same raw dataset is processed again, the result should be consistent.

---

# 17. Final Challenge

After completing the first version of the project, ask yourself:

> "If I received this file again tomorrow, would I trust my program to process it automatically?"

If the answer is no, investigate why.

Possible reasons:

* The program depends on manual fixes
* Some unexpected values still cause crashes
* Validation is insufficient
* The cleaning rules are too specific
* The program silently loses information
* Some decisions were arbitrary
* The program does not report important problems
* The output cannot be trusted

Improve the program where necessary.

---

# 18. Final Deliverables

The project should produce at least:

### 1. Processed Dataset

A cleaned and normalized version of the raw dataset.

```text
data/processed/players_clean.csv
```

### 2. Data Quality Report

A report describing the processing and the problems discovered.

```text
reports/data_quality.txt
```

### 3. Source Code

Organized Python source code responsible for:

* Reading
* Investigation
* Cleaning
* Validation
* Writing
* Reporting

### 4. README

The README should explain:

* What the project does
* Where the dataset came from
* How to run the project
* What problems were discovered
* What transformations were performed
* What validation rules were implemented
* Important decisions made during cleaning
* Limitations of the final result

---

# 19. Success Criteria

The project is successful if you can demonstrate that you can take an unfamiliar dataset and independently go through the following process:

```text
UNKNOWN DATA
     ↓
INVESTIGATE
     ↓
UNDERSTAND
     ↓
IDENTIFY PROBLEMS
     ↓
MAKE DATA-QUALITY DECISIONS
     ↓
IMPLEMENT IN PYTHON
     ↓
VALIDATE
     ↓
PRODUCE RELIABLE DATA
     ↓
DOCUMENT THE PROCESS
```

The quality of the project is **not** measured by how many lines of code you write.

It is measured by whether you can explain:

* What was wrong with the raw data
* How you discovered it
* Why it was a problem
* What decision you made
* Why you made that decision
* How you implemented the transformation
* How you validated the result
* What information you removed or preserved
* What limitations remain

---

# 20. What You Should NOT Optimize For

Do not try to:

* Write the shortest possible code
* Use advanced Python just to look sophisticated
* Create unnecessary classes
* Create unnecessary abstractions
* Automatically fill every missing value
* Delete every unusual record
* Make the dataset "perfect"
* Copy a Kaggle notebook
* Use a library to solve the entire problem
* Finish as quickly as possible

The objective is learning.

Prefer code that you understand and can explain.

---

# 21. Research Rules

You may search for documentation and specific technical questions.

Good examples:

```text
Python csv DictReader documentation
Python regex documentation
Python datetime strptime
Python pathlib documentation
Python exception handling
Python string methods
Python write CSV
```

Bad examples:

```text
FIFA 21 dataset solution
FIFA 21 cleaning notebook
FIFA 21 data cleaning GitHub
complete FIFA 21 Python cleaning project
```

If you get stuck, first try to identify **exactly what concept you don't understand**.

Research that concept.

Then return to the project and implement the solution yourself.

---

# 22. The Core Rule

Do not ask:

> "How do I clean this dataset?"

Ask:

> "What is wrong with this dataset, and what evidence do I have that it is wrong?"

Then ask:

> "What should the correct representation be?"

Then:

> "How can I implement and validate that decision in Python?"

That is the main skill this project is designed to develop.

---

# 23. Project Philosophy

This project should feel more like receiving a real data file from another system than completing a tutorial.

You are the person responsible for figuring out what the data means.

There is no predefined list of cleaning operations.

There is no single "correct" cleaning script.

Different reasonable decisions may produce different outputs.

What matters is that your decisions are:

* Justified
* Consistent
* Reproducible
* Validated
* Documented

The ultimate goal is to develop the habit of looking at raw data and thinking:

> "Before I process this, I need to understand what I'm actually dealing with."
