# Advent of Code
These are my somewhat hacky Advent of Code solutions, starting from year 2024.

I try to vary between using `Python`, `Node.js`, `Java`, and `C#`, by using the `aoc.py` script which randomly selects a language for each day.

## How to use the aoc.py script
- Ensure VS Code is installed, and set the `VS_CODE_PATH` variable to the full path of the `.cmd` file.
- Create your Advent of Code directory and place the `aoc.py` file there.
- Run `python aoc.py` with the following arguments:
- - `-y --year` => year of the challenge (folder). If folder doesn't exist, it will be created
- - `-d --day` => day of the challenge (folder). If folder doesn't exist, it will be created
- - `-l --language` => language to use (`python|node.js|java|c#`). Creates the `solve` file with the boilerplate code for that language. If not included, will pick a random language.

- Example full command: `python aoc.py -y 2024 -d 1 -l python` 