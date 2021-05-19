#--- Factorial - While ( Option 1)
number = 6 
current = number
product =1

while current > 0:
    product*=current
    current-= 1
print(product)    

#--- Factorial - While ( Option 2)

# number to find the factorial of
number = 6
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1

while  current <= number:
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1

#--- Fatorial - For
number = 6 
current = number
product =1

for n in range(1,number+1):
    product*=n
print(product)    


#--- Count By
start_num = 5
end_num = 100
count_by = 2

break_num = start_num
while break_num < end_num:
    break_num += count_by

print(break_num)

#--- Count by - check
start_num = 5
end_num = 100
count_by = 2

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by

    result = break_num

print(result)

#---- Nested Square
limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)


#-----
## Please use this space to test and run your code
num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_count = 0
odd_list=[]

while odd_count <=5:
    for n in num_list:
        if n%2!=0:
            odd_list.append(n)
        odd_count = odd_count + 1
            
print(odd_list)




### ------- Using For


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

odd_count = 0
odd_sum = 0

for n in num_list:
    if odd_count <=5:
        if n%2!=0:
            odd_sum+=n
            odd_count+=1
print(odd_sum)


#Using While

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))