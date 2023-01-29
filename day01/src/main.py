from collections import defaultdict

with open('day01/input.txt', 'r') as demo_input:
    demo_input_list = demo_input.readlines()


class ElfCalories:
    """Defaultdict class to append elf and corresponding list of calories"""
    def __init__(self):
        self.data = defaultdict(list)

    def add(self, elf, calorie):
        self.data[elf].append(calorie)


elfcalories = ElfCalories()

elf_num = 0
for calorie in demo_input_list:
    if calorie != '\n':
        elfcalories.add(f'elf{elf_num}', int(calorie.rstrip('\n')))
    else:
        elf_num += 1

sum_elfcalories = {}
for elf, calories in elfcalories.data.items():
    sum_elfcalories.update({elf: sum(calories)})

# Part One
print(max(sum_elfcalories.values()))

# Part Two
print(sum(sorted(sum_elfcalories.values(), reverse=True)[:3]))