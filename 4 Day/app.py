
def part_one():
    file = open("input.txt")
    lines = file.read().splitlines()
    count_of_overlap = 0
    for line in lines:
        firs_elf = line.split(",")[0]
        second_elf = line.split(",")[1]
        first_elf_first_task = int(firs_elf.split("-")[0])
        first_elf_second_task = int(firs_elf.split("-")[1])

        second_elf_first_task = int(second_elf.split("-")[0])
        second_elf_second_task = int(second_elf.split("-")[1])

        first_elf_tasks = list(range(first_elf_first_task, first_elf_second_task + 1))
        second_elf_tasks = list(range(second_elf_first_task, second_elf_second_task + 1))

        if first_elf_first_task in second_elf_tasks and first_elf_second_task in second_elf_tasks:
            count_of_overlap += 1
        elif second_elf_first_task in first_elf_tasks and second_elf_second_task in first_elf_tasks:
            count_of_overlap += 1
    return count_of_overlap


def part_two():
    file = open("input.txt")
    lines = file.read().splitlines()
    count_of_overlap = 0
    for line in lines:
        firs_elf = line.split(",")[0]
        second_elf = line.split(",")[1]
        first_elf_first_task = int(firs_elf.split("-")[0])
        first_elf_second_task = int(firs_elf.split("-")[1])

        second_elf_first_task = int(second_elf.split("-")[0])
        second_elf_second_task = int(second_elf.split("-")[1])

        first_elf_tasks = list(range(first_elf_first_task, first_elf_second_task + 1))
        second_elf_tasks = list(range(second_elf_first_task, second_elf_second_task + 1))

        if first_elf_first_task in second_elf_tasks or first_elf_second_task in second_elf_tasks:
            count_of_overlap += 1
        elif second_elf_first_task in first_elf_tasks or second_elf_second_task in first_elf_tasks:
            count_of_overlap += 1
    return count_of_overlap


def main():
    print(f"Part one: { part_one() }")
    print(f"Part two: { part_two() }")


if __name__ == "__main__":
    main()