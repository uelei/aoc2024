# aoc2024

https://adventofcode.com/2024

## Setup

Install the helper client aoc-cli [https://github.com/scarvalhojr/aoc-cli](https://github.com/scarvalhojr/aoc-cli)

Create the file `~/.adventofcode.session` with your session cookie.

To create and download a day:

```bash
cp -r day00 dayXX
aoc download --day X
```

## To Run Tests

```bash
uv run pytest partX.py
```

## To Run Parts

```bash
uv run python partX.py
```

## To Submit the Results

```bash
aoc submit --day=<DAY> <PART> <RESULT>
```
