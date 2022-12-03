letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_container_one(rucksack):
    return rucksack[0:int(len(rucksack)/2)]


def get_container_two(rucksack):
    return rucksack[int(len(rucksack)/2):len(rucksack)]

def get_prioirity_of_letter(letter):
    return letters.index(letter) + 1


def part_one():
    file = open("input.txt")
    lines = file.read().splitlines()
    sum_of_prioirities = 0

    for line in lines:
        container_one = get_container_one(line)
        container_two = get_container_two(line)
        tmp = []
        for character in container_one:
            if character in container_two  and character not in tmp:
                tmp.append(character)
                sum_of_prioirities += get_prioirity_of_letter(character)
    return sum_of_prioirities


def part_two():
    file = open("input.txt")
    lines = file.read().splitlines()
    sum_of_prioirities = 0

    for i in range(0,len(lines), 3):
        line_a = lines[i]
        line_b = lines[i+1]
        line_c = lines[i+2] 
        for character in line_a:
            if character in line_b  and character in line_c:
                print(character)
                sum_of_prioirities += get_prioirity_of_letter(character)
                break
    return sum_of_prioirities


def main():
    print(f"Part one:{ part_one() }")
    print(f"Part two:{ part_two() }")


if __name__ == "__main__":
    main()