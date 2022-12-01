def main():
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



if __name__ == '__main__':
    main()