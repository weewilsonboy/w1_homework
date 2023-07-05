def add(num_1, num_2):
    return num_1 + num_2

print("------------------------------")
print("By adding 4 and 5, I'm expecting it to be 9, and the result is")
print(add(4, 5))

def subtract(num_1, num_2):
    return num_1-num_2

print("------------------------------")
print("By subtracting 3 from 10, I'm expecting it to be 7, and the result is")
# check by calling the function with the arguments 10 and 3:
print(subtract(10,3))

def multiply(num_1,num_2):
    return num_1 * num_2


print("------------------------------")
# replace _ with your own values and expectation:
print("By multiplying 2 and 4, I'm expecting it to be 8, and the result is")
# check by invoking the function with your own values:
print(multiply(2,4))

def divide(num_1,num_2):
    return num_1/num_2

print("------------------------------")
# replace _ with your own values and expectation:
print("By dividing 6 by 3, I'm expecting it to be 2, and the result is")
# check by calling the function with your own arguments:
print(divide(6,3))

def length(string):
    return len(string)

print("------------------------------")
print("By calculating the length of the string 'How now, brown cow?', I'm expecting it to be 19, and the result is")
print(length("How now, brown cow?"))

def concatenate(str1, str2):
    return str1+str2

print("------------------------------")
print("By joining the strings 'go do' and 'good', I'm expecting it to be 'go do good', and the result is")
print(concatenate("go do","good"))

def add_string_as_number(str1,str2):
    return int(str1) + int(str2)
print("------------------------------")
print("By adding the strings '58' and '42' as numbers, I'm expecting it to be 100, and the result is")
print(add_string_as_number("58","42"))

def number_to_full_name(month):
    month_list = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    answer = month_list[month -1] 
    return answer

print("------------------------------")
print("By converting 1 to the full month name, I'm expecting it to be 'January', and the result is")
print(number_to_full_name(1))

print("------------------------------")
print("By converting 3 to the full month name, I'm expecting it to be 'March', and the result is")
print(number_to_full_name(3))

print("------------------------------")
print("By converting 9 to the full month name, I'm expecting it to be 'September', and the result is")
print(number_to_full_name(9))

# HINT: Could you use `number_to_full_name` by calling it from within this function?
def number_to_short_month_name(month):
    long_mon = number_to_full_name(month)
    short_mon = long_mon[0:3]
    return short_mon


print("------------------------------")
print("By converting 2 to the short month name, I'm expecting it to be 'Feb', and the result is")
print(number_to_short_month_name(2))

print("------------------------------")
print("By converting 4 to the short month name, I'm expecting it to be 'Apr', and the result is")
print(number_to_short_month_name(4))

print("------------------------------")
print("By converting 10 to the short month name, I'm expecting it to be 'Oct', and the result is")
print(number_to_short_month_name(10))

#test