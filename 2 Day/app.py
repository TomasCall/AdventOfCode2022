opponent_choices = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}

player_choices = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

loser_choices = {
    "A" : "Z",
    "B" : "X",
    "C" : "Y"
}

winner_choices = {
    "A" : "Y",
    "B" : "Z",
    "C" : "X"
}


def part_one():
    file = open("input.txt")
    lines = file.read().splitlines()
    count_of_won_games = 0
    for line in lines:
        player = line.split(" ")[1]
        opponent = line.split(" ")[0]
        if (player == "X" and opponent == "A") or (player == "Y" and opponent == "B") or (player == "Z" and opponent == "C"):
            count_of_won_games += 3 + player_choices[player]
        elif (player == "X" and opponent == "C") or (player == "Y" and opponent == "A") or (player == "Z" and opponent == "B"):
            count_of_won_games += 6 + player_choices[player]
        else:
            count_of_won_games += player_choices[player]
    return count_of_won_games


def part_two():
    file = open("input.txt")
    lines = file.read().splitlines()
    score = 0
    for line in lines:
        result = line.split(" ")[1]
        opponent = line.split(" ")[0]
        if result == "X":
            score += player_choices[loser_choices[opponent]]
        elif result == "Y":
            score += 3 + opponent_choices[opponent]
        else:
            score += 6 + player_choices[winner_choices[opponent]]
    return score


def main():
    print(f"Part one: { part_one() }")
    print(f"Part two: { part_two() }")


if __name__ == "__main__":
    main()