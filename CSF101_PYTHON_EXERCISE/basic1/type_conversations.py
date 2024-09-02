#12
age = 18
age_str = str(age)
message = "i am" + age_str + "years old."
print(message)   #new variable plus strings and values

#13
num_str = "42"
num_int = int(num_str)
print(num_int)

#14
non_num_str = "Hello"
try:
    non_num_int = int(non_num_str)
    print(non_num_int)
except ValueError as e:
    print(f"Error: {e}") #using new function try and except .....something similar like if and else