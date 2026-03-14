def ft_plant_age():
    harvest_age = 60
    x_string = input("Enter plant age in days: ")
    x = int(x_string)
    if(x > harvest_age):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
