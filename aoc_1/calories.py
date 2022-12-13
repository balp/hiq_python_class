import dataclasses
from pathlib import Path
from typing import List


def calculate(input_file: Path):
    nissar = make_nissar(input_file)
    print(f"Svaret är {max(nissar, key=lambda x: x.calories())}")

@dataclasses.dataclass
class Nisse:
    id: int
    snacks: List[int]

    def calories(self):
        return sum(self.snacks)



def make_nissar(input_file):
    with input_file.open("r") as f:
        lines = f.readlines()
    calories = 0
    count = 0
    snacks = []
    nissar = []
    nissar_objects = []
    for line in lines:
        line = line.strip()
        print(f" -- {len(line)}")
        if line == '':
            nissar.append(calories)
            nissar_objects.append(Nisse(count, snacks))
            snacks = []
            calories = 0
            count += 1
        else:
            snack = int(line)
            calories += snack
            snacks.append(snack)
            print(f" -- {calories}")
    nissar.append(calories)
    print(f" ::: {nissar_objects}")
    return nissar_objects


def top_three(input_file: Path):
    nissar = make_nissar(input_file)
    nissar.sort(reverse=True, key=lambda x: x.calories())
    top_calories = [x.calories() for x in nissar[:3]]
    print(f"<< {sum(top_calories)}")


if __name__ == '__main__':
    calculate(Path("input.txt"))
    top_three(Path("input.txt"))
