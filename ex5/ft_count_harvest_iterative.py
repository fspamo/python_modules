def ft_count_harvest_iterative():
    i = 1
    num = input("Days until harvest: ")
    num = int(num)
    for i in range(1, num + 1):
        print(f"Day {i}")
    print("Harvest time!")
