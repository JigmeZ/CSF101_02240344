#18
name = "Jigme"
age = 18
height = 176 #giving variables their values 
is_student = True #conditions

person_info = {
    "name" : name,
    "age" : age,
    "height" : height,
    "is_student" : is_student #inputs
}
print(person_info)

#19
person_info["favorite_color"] = "blue" #use of square brackets and info
print(person_info) # output

#20
try:
    print(person_info["weight"]) #using the try and except function
except KeyError as e:
    print(f"Error: {e}")



