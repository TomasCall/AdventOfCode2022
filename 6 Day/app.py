

def part_one():
    file = open("input.txt")
    line = file.read()
    
    index = 0
    actual_four_characters = []
    for character in line:
        if len(actual_four_characters) == 4 and len(set(actual_four_characters)) == 4: 
            return index
        actual_four_characters.append(character)
        if len(actual_four_characters) == 5:
            actual_four_characters.pop(0)
        index += 1
    return index


def part_two():
    file = open("input.txt")
    line = file.read()
    
    index = 0
    actual_four_characters = []
    for character in line:
        if len(actual_four_characters) == 14 and len(set(actual_four_characters)) == 14: 
            return index
        actual_four_characters.append(character)
        if len(actual_four_characters) == 15:
            actual_four_characters.pop(0)
        index += 1
    return index


def main():
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")


if __name__ == "__main__":
    main()