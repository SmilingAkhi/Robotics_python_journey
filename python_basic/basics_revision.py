# EXERCISE 1
# def analyze_numbers(numbers):
#     """
#     Returns:
#     - count of even numbers
#     - count of odd numbers
#     - sum of numbers
#     - largest number
#     """

# Constraints:

# No built-in max()

# No sum()

# Handle empty list safely

# Return a dictionary


numbers = [4, 7, 1, 10, 3, 8, 16, 12]
 
def analyze_numbers(numbers):
    count_even = 0
    count_odd = 0
    sum = 0
    if numbers == []:
        return{"even_count": 0, "odd_count": 0, "sum": 0, "largest": None}
        
    else:
        for each_number in numbers:
            if each_number % 2 == 0:
                count_even += 1
            if each_number % 2 != 0:
                count_odd +=1
            else: continue
        # print(f"The count of even number is: {count_even}")
        # print(f"The count of odd number is: {count_odd}")
        for each_digit in  numbers:
            sum += each_digit
        # print(f"sum of all the numbers is {sum}")

        ##biggest number 
        biggest = numbers[0]
        for digit in numbers:
            if digit > biggest:
                biggest = digit
        # print(biggest)
        return  {"even_count": count_even, "odd_count": count_odd, "sum": sum, "largest": biggest}

print (analyze_numbers(numbers))

#EXERCISE 2
# 2A — Reverse a String
# 2B — Character Frequency Counter
# 2C — Remove Duplicates (Preserve Order)
# 2D — Sort List of Tuples by Second Value

# 2A
word = "robotics"
reversed_word = [ ]
index_count = len(word)
for each_letter in word:
    index_count -= 1 
    reversed_word.append(word[index_count])
print("".join(reversed_word))

# 2B

word = "robotics"
dic = {}

for each_letter in word:
    if each_letter in dic:
        dic[each_letter] += 1
    else:
        dic[each_letter] = 1

print(dic)

# 2C
digits = [1, 2, 2, 3, 1, 4]
new_list = []
for each_digit in digits:
    if each_digit not in new_list:
        new_list.append(each_digit)
    else: continue
print(new_list)

list = [("a", 3), ("b", 1), ("c", 2)]
sorted_list = sorted(list, key=lambda x:x[1])
print(sorted_list)

list.sort(key=lambda x:x[1], reverse=True)
print(list)
