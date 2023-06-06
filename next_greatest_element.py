def nge(array:list):
    for i, value1 in enumerate(array):
        for value2 in array[i:]:
            if value2 > value1:
                print(f"{value1} -> {value2}")
                break
        else:
            print(f"{value1} -> -1")
#you can use range i.e for i in range(len(array)):
