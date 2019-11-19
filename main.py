import sys

max_number_of_cases = 100
# max_range = 200

number_of_cases = int(input())
if number_of_cases < 1 or number_of_cases > max_number_of_cases:
    sys.exit(0)
results = []
for i in range(0, number_of_cases):
    number_of_numbers = int(input())
    user_numbers = input()
    user_numbers_arr = user_numbers.split()
    result = 0
    if len(user_numbers_arr) != number_of_numbers:
        sys.exit(0)
    else:
        for n in range(0, number_of_numbers):
            result += int(user_numbers_arr[n])
        results.append(result)

for i in results:
    print(i)