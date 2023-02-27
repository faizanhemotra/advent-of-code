from typing import Any, List, Union

with open('day03/input.txt', 'r') as input_text:
    input_list = [line.rstrip() for line in input_text]


def string_divider(string: str) -> Union[str, List[str]]:
    """Function to divide string from a mid-point

    Parameters
    ----------
    string : str
        Input string

    Returns
    -------
    List[str]
        Divided string in a list
        If the string cannot be divided equally, original string is returned
    """
    LEN_STRING = len(string)
    STRING_MID_POINT = LEN_STRING//2
    if LEN_STRING % 2 != 0:
        print(f'String {string!r} cannot be divided equally :(')
        return string

    else:
        return [string[:STRING_MID_POINT], string[STRING_MID_POINT:]]


def offset_string_ascii(string: str, offset: int) -> int:
    """Offset string's ASCII

    Parameters
    ----------
    string : str
        Input string value
    offset : int
        Amount to offset by

    Returns
    -------
    int
        ASCII value offset by amount
    """
    return ord(string) - offset


all_rucksacks = []
for rucksacks in input_list:
    all_rucksacks.append(string_divider(rucksacks))


def find_common_strings(list_of_strings: List[str]) -> List[str]:
    sets_of_strings = []
    for string in list_of_strings:
        sets_of_strings.append(set(string))
    common_strings = list(set.intersection(*sets_of_strings))
    return common_strings


def set_priorities(alphabet: str) -> int:
    """Set priorities according to the challenge

    Parameters
    ----------
    alphabet : str
        lowercase or uppercase alphabet

    Returns
    -------
    int
        Returns priority number

    Raises
    ------
    ValueError
        Exception is raised if not a lowercase or uppercase character
    """
    LOWERCASE_OFFSET = 96
    UPPERCASE_OFFSET = 38
    if alphabet.islower():
        return offset_string_ascii(alphabet, LOWERCASE_OFFSET)
    elif alphabet.isupper():
        return offset_string_ascii(alphabet, UPPERCASE_OFFSET)
    else:
        raise ValueError('Invalid common item')


priorities = []
for rucksack in all_rucksacks:
    compartment_zero = rucksack[0]
    compartment_one = rucksack[1]
    common_items = find_common_strings([compartment_zero, compartment_one])
    for common_item in common_items:
        priorities.append(set_priorities(common_item))

# part 1 answer
print(sum(priorities))


# start of part 2
def equally_divide_list(input_list: List[Any], size: int) -> List[List[Any]]:
    import more_itertools
    return list(more_itertools.batched(input_list, size))


elf_groups = equally_divide_list(input_list, 3)
priorities = []
for elf_group in elf_groups:
    common_items = find_common_strings(elf_group)
    for common_item in common_items:
        priorities.append(set_priorities(common_item))

# part 2 answer
print(sum(priorities))