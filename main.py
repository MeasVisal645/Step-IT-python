# my_tuple = (10, 20, 30 ,40)
#
# print(my_tuple[0])
# print(my_tuple[-2])
# print(my_tuple[1:3])
#
# a, b, c ,d = my_tuple
#
# first, *middle, last = my_tuple
#
# print(a)
# print(b)
# print(c)
# print(d)
#
# print(first)
# print(middle)
# print(last)
from netaddr.strategy.eui48 import mac_unix


# def get_user_name():
#     name = "Visal"
#     age = 22
#     city = "PP"
#     return name, age, city
#
# tuple_value = get_user_name()
# user_name, user_age, user_city = tuple_value
#
# print(tuple_value)
# print(user_name, user_age, user_city)

# locations = {
#     (40.7128, -74.0060): "New York",
#     (51.5074, -0.1278): "London",
#     (35.6762, 139.6503): "Tokyo"
# }
#
# print(locations)

def find_min(numbers):
    min_number = 0
    for i in range(0, len(numbers) - 1):
        if numbers[i] < numbers[i + 1]:
            min_number = numbers[i]
    return min_number

def find_max(numbers):
    max_number = 0
    for i in range(0, len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            max_number = numbers[i]
    return max_number

def analyze_numbers(numbers):
    min_number = find_min(numbers)
    max_number = find_max(numbers)
    average_number = sum(numbers) / len(numbers)

    return min_number, max_number, average_number

print(analyze_numbers([5, 2, 9, 1, 7]))
