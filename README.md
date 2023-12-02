# Advent of Code solutions by Luke's Bytes

## Setup execution environment

Create virtual environment

```bash
python3 -m venv .venv/
.venv/bin/activate
python3 -m pip install -r requirements.txt
````

To freeze modified environment at later stage

```bash
python3 -m pip freeze | tee requirements.txt
```

## Fill identity

TBD

## Run challange

Challenges are organized per year under `challenges` folder.  

To run the first challenge of 2023:

```bash
PYTHONPATH=. python3 challenges/2023/d01.py
```
