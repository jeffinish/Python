# numbers = [2, 5, 6, 7, 8, 8,8,8,28, 10]
#
# for number in numbers:
#     while numbers.count(number) > 1:
#         numbers.remove(number)
# print(numbers)

numbers = [2, 5, 6, 7, 8, 8,8,8,28, 10]
unique = []

for number in numbers:
    if number not in unique:
        unique.append(number)

print(numbers)
print(unique)
