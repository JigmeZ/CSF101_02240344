#1 
def create_and_write_file(filename):
    with open(filename, 'w') as file: # it will help us create new file easily
        file.write("This is the first line. \n")
        file.write("This is the second line. \n")
        file.write("This is the third line. \n")

create_and_write_file('sample.txt')
print("file created and written successfully.")

#2
def rtead_and_print_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(content)

rtead_and_print_file('sample.txt')

#3
def append_to_file(filename, new_line):
    with open(filename, 'a') as file:
        file.write(new_line + "\n")
    
append_to_file('sample.txt', "This is an appended line.")
print("Line appended successfully.")
rtead_and_print_file('sample.txt')

#4
def print_line_with_numbers(filename):
    with open(filename, 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")
print_line_with_numbers('sample.txt')

#5
def count_words(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()

        
        