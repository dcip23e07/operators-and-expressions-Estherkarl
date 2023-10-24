
#convert 4999 to base 2 
num1 = 4999
num1_bin = bin(num1)
print(num1_bin)

#result : 0b1001110000111

#convert 2111 to base 2
num2 = 2111
num2_bin = bin(num2)
print(num2_bin)

# result : 0b100000111111

#what will be the value of 4999 & 2111

num_value = (num1 & num2)

print(num_value)

#result is 7

#what will be the value of 4999 | 2111

num_value_2 = (num1 | num2)

print(num_value_2)

#result is 7103