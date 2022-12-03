def get_the_elves_calories():
    file = open("input.txt")
    lines = file.read().splitlines()
    result = []
    tmp = 0
    for line in lines:
        if line != "":
            tmp += int(line)
        else:
            result.append(tmp)
            tmp = 0
    return result


def part_one():
    return (max(get_the_elves_calories()))


def part_two():
    result = get_the_elves_calories()
    result.sort(reverse=True)
    return result[0] + result[1] + result[2]


def main():
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
    


if __name__ == "__main__":
    main()