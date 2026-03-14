def ft_harvest_total():
    x = 1
    ningen = 0
    total = 0
    while (x <= 3):
        print(f"Day ", x, " harvest: ")
        ningen = int(input())
        total = ningen + total
        x += 1
    print("Total harvest: ", total)
