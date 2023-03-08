def convert_add(list_to_add):
    sum = 0
    for i in list_to_add:
        sum = int(i) + sum
    return sum

convert_add([‘1’, ‘3’, ‘5’])