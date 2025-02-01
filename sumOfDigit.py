# print("Enter number")
# num = int(input())  #256 

# sum=0 
# last = num%10  #256%10 => 6
# sum = sum + last #6 

# num = num // 10  #256//10 => 25 
# last = num%10 # 25%10 => 5
# sum = sum + last #6+5 


# num = num // 10 #25//10 => 2
# last = num%10 # 2 % 10 => 2 
# sum = sum + last #6+5+2 

# num = num //10 # 2//10 => 0

# print(sum)



print("Enter number")
num = int(input())  #256 

sum=0 

while num > 0:
    last = num%10  #256%10 => 6
    sum = sum + last #6 
    num = num // 10  #256//10 => 25 
 
print(sum)