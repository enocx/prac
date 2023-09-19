

def TOH(numbers, start, aux, end):
    global count
    if numbers == 1:
        print(f"Move disk 1 from {start} to {end}")
        count += 1
        return
    TOH(numbers-1, start, end, aux)
    print(f"Move disk {numbers} from {start} to {end}")
    count += 1
    TOH(numbers-1, aux, start, end)


count = 0

disc = int(input("Enter the number of disks: "))

TOH(disc, "A", "B", "C")
print(f"Number of moves: {count}")
