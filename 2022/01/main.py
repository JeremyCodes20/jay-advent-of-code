def main():
    part1()
    part2()

def part1():
    with open('./input.txt', 'r') as input:
        lines = input.readlines()
        elf_sums = []
        curr_elf = 0
        for line in lines:
            if line == '\n':
                elf_sums.append(curr_elf)
                curr_elf = 0
            else:
                curr_elf += int(line)
        elf_sums.append(curr_elf)

        print(f'The most calories an elf is carrying is {max(elf_sums)}.')

def part2():
    with open('./input.txt', 'r') as input:
        lines = input.readlines()
        elf_sums = []
        curr_elf = 0
        for line in lines:
            if line == '\n':
                elf_sums.append(curr_elf)
                curr_elf = 0
            else:
                curr_elf += int(line)
        elf_sums.append(curr_elf)

        elf_sums.sort(reverse=True)

        calorie_sum = sum(elf_sums[:3])

        print(f'The three elves carrying the most calories total to {calorie_sum} calories.')

if __name__ == '__main__':
    main()