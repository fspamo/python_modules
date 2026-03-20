def ft_count_harvest_recursive(i, num):
    if i <= num:
        print(f"Day {i}")
        ft_count_harvest_recursive(i + 1, num)
    else:
        print("Harvest time!")

def harvester():
    i = 1
    num = input("Days until harvest: ")
    num = int(num)
    ft_count_harvest_recursive(i, num)
