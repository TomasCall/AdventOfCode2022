def move(count, start, finish, array):
    for i in range(0, count):
        array[finish].insert(0, array[start][0])
        array[start].pop(0)


def move_two(count, start, finish, array):
    array_tmp = []
    
    for i in range(0, count):
        array_tmp.append(array[start].pop(0))
    
    for cargo in array[finish]:
        array_tmp.append(cargo)
    array[finish] = array_tmp


def part_one():
    file = open("input.txt")
    lines = file.read().splitlines()

    line_with_numbers = ""
    
    for line in lines:
        if "1" in line:
            line_with_numbers = line
            break
    
    indexes = []

    for i in range(0, len(line_with_numbers)):
        if line_with_numbers[i] != " ":
            indexes.append(i)
    
    cargos = []

    for i in range(0, len(indexes)):
        cargos.append([])

    for line in lines:
        if "1" in line:
            break
        else:
            for i in indexes:
                if line[i] != " ":
                    cargos[indexes.index(i)].append(line[i])

    can_start_move = False
    index_of_line = 0
    for line in lines:
        print(f"Line:{index_of_line}")
        index_of_line += 1
        if can_start_move:
            count = int(line.split(" ")[1])
            start = int(line.split(" ")[3]) - 1
            finish = int(line.split(" ")[5]) - 1
            #move(count=count, start=start, finish=finish, array=cargos)
            move_two(count=count, start=start, finish=finish, array=cargos)
        elif line == "":
            can_start_move = True
    
    result = ""
    for cargo in cargos:
        result += cargo[0]
    
    return result



def main():
    print(f"Part one: {part_one()}")


if __name__ == "__main__":
    main()