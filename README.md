# Fizzbuzz Kata
The fizzbuzz application accepts a number and outputs either: fizz, buzz, fizzbuzz, or the number itself based on the requirements.

## Fizzbuzz Requirements
- Outputs "fizz" for numbers divisible by 3
- Outputs "buzz" for numbers divisible by 5
- Outputs "fizzbuzz" for numbers divisible by 3 and 5
- Outputs the input if it doesn't fit the previous requirements

## Prerequisites
- [python](https://docs.python-guide.org/starting/install3/osx/): ^3.7
- [pytest](https://docs.pytest.org/en/latest/): ^5.4

## Getting Started
1. `git clone git@github.com:QuinnManor/python-katas.git`
2. `cd python-katas`
3. `git checkout fizzbuzz`

## Running our Tests
To execute the test suite run:

```python
pytest
```

## Fizzbuzz Usage
To run the application:

```python
python app.py
```

## Project Organization
------------
    ├── README.md         <- The top-level README for developers using this project.
    |
    ├── app.py            <- The main application.
    |
    ├── fizzbuzz          <- Directory holding fizzbuzz 
    │   ├── fizzbuzz.py        <- The fizzbuzz application.
    │   ├── test_fizzbuzz.py   <- The unit test suite for the.
    |
    ├── .gitignore         <- Specifies which files to ignore within the repository.
--------