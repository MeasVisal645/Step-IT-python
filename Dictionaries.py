# empty_dict = {}
# dict_constructor = dict(name="Bob", age=25)
# from_tuples = dict([("a", 1), ("b", 2)])

# # print(dict_constructor)
# # print(from_tuples)


# squares = {x: x**2 for x in range(5)}

# # print(squares)
# # print(squares[4])

# person = {"name": "Alice", "age": 30, "city": "NYC"}

# # Dictionary cannot be access by index
# # print(person[0]) 
# # print(person["name"])
# # print(person.get("age"))
# # print(person.get("city", "Unknown"))

# city = person.get("city")
# if city == None:
#     city = "Empty"
# # print(city)


# user = {}

# # add
# user["username"] = "dave"
# user.update({"password" : "12345", "username": "dave update"}) 
# user.setdefault("username", "default")
# user.setdefault("age", 10)

# # print(user)

# remove
# removed_value = user.pop("username")

# print(removed_value)
# print(user)

# removed_value = user.popitem()

# print(removed_value)
# print(user)


# # looping through key
# for key in user:
#     print(f'Key: {key} value: {user[key]}')

# # looping through item 
# print('-------------------------')
# for key, value in user.items():
#     print(f'Key: {key} Value: {value}')

# # looping through dict only value
# print('-------------------------')
# for value in user.values():
#     print(f'Value: {value}')



# Example
# Char count
# text = "hello world"
# char_count = {}

# for char in text:
#     char_count[char] = char_count.get(char, 0) + 1
# print(char_count)

# clean_text = text.replace(" ", "")
# print(clean_text)

# before_join = text.split(" ")
# print(before_join)
# clean_text1 = "".join(text.split(" "))
# print(clean_text1)
# print("".join(before_join))

def merge_dicts(dict1, dict2):
    result = dict1
    
    for key, value in dict2.items():
        if result.get(key) == None:
            result[key] = value
        else:
            result[key] += value    
        
    return result

d1 = { "a": 1, "b": 2, "c": 3}
d2 = { "b": 3, "c": 4, "d": 5}

# merge_dicts(d1, d2)
print(merge_dicts(d1, d2))
