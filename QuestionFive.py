#Task 1 

value_one = 15 
value_two = 10
temp_value = 15 

print( "Value one is:" + str(value_one))
print( "Value two is:" + str(value_two))

value_one -= value_one 
value_one += value_two 


value_two -= value_two 
value_two += temp_value  

print( "Swapped value one is:" + str(value_one))
print( "Swapped value two is:" + str(value_two))

if(value_one < value_two):
    print("The numbers were correctly switched")
else :
    print("The numbers were not correctly switched")



