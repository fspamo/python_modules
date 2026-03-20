def ft_harvest_total():
    x = 1
    total = 0
    while (x <= 3):
        ningen = input(f"Day {x} harvest: ")
        ningen = int(ningen)
        total = ningen + total
        x += 1

    print("Total harvest: ", total)

ft_harvest_total()
