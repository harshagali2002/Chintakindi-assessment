def print_elements_less_than_5(elements):
    less_than_5 = []
    for element in elements:
        if element < 5:
            less_than_5.append(element)
    print("Elements less than 5 are:", less_than_5)


elements = [3, 6, 2, 7, 4, 8, 1, 9, 0, 5]

print_elements_less_than_5(elements)