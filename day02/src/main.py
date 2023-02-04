from typing import List

with open('day02/input.txt', 'r') as input_text:
    input_list = [(
        line.rstrip()
        .replace('A', '1').replace('X', '1')
        .replace('B', '2').replace('Y', '2')
        .replace('C', '3').replace('Z', '3')) for line in input_text]


def rock_paper_scissors(plyr_zero: int, plyr_one: int, plyr_score: int = 1) -> int:
    """Rock Paper Scissors game function
    Takes Players moves as integers.
    1 for rock, 2 for paper, and 3 for scissors

    Parameters
    ----------
    plyr_zero : int
        Player zero's move
    plyr_one : int
        Player one's move
    plyr_score : int
        Return player zero or one's score

    Returns
    -------
    int
        _description_
    """
    LOSE_SCORE = 0
    WIN_SCORE = 6
    DRAW_SCORE = 3
    movediff = abs(plyr_zero - plyr_one)

    if movediff > 2:
        raise ValueError('Representation should be consecutive int numbers')

    if plyr_score == 0:
        plyrscore_to_return = plyr_zero

    elif plyr_score == 1:
        plyrscore_to_return = plyr_one
    else:
        raise ValueError('Invalid plyr_score value entered: Please enter 0 or 1')

    match movediff:
        case 0:
            return DRAW_SCORE + plyrscore_to_return

        case 1:
            return (WIN_SCORE if plyr_one > plyr_zero else LOSE_SCORE) + plyrscore_to_return

        case _:
            return (LOSE_SCORE if plyr_one > plyr_zero else WIN_SCORE) + plyrscore_to_return


def rps_outcomes(input_list: List[str] = input_list, sus: bool = True) -> List[int]:
    """Wrapper around rock_paper_scissors to get game results

    Parameters
    ----------
    input_list : List[str]
        Input list

    sus: bool
        Sussy Baka?
        part 2 of the day 2

    Returns
    -------
    List[int]
        Round results
    """
    outcomes = []
    for move in input_list:
        moves = move.split()
        plyr_one_move = int(moves[0])
        plyr_two_move = int(moves[1])
        if not sus:
            match plyr_two_move:
                case 1:
                    # if they choose paper we choose rock
                    # if it's scissors we choose paper
                    plyr_two_move = plyr_one_move - 1
                    # if it's rock we choose scissors
                    # this will fail for cases
                    # where the diff between each number > 0
                    if plyr_two_move == 0:
                        plyr_two_move = plyr_one_move + 2

                case 2:
                    plyr_two_move = plyr_one_move

                case 3:
                    plyr_two_move = plyr_one_move + 1
                    if plyr_two_move > 3:
                        plyr_two_move = 1
        outcomes.append(rock_paper_scissors(plyr_one_move, plyr_two_move))
    return outcomes


print(sum(rps_outcomes()))
# part 2
print(sum(rps_outcomes(sus=False)))
