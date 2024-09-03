#6
def create_binary_file(filename):
    data = bytes([0, 1, 2, 3, 4, 5])
    with open(filename, 'wb') as file:
        file.write(data)

create_binary_file('binary_sample.bin')
print("Binary file created successfully")

#7
def read_binary_file(filename):
    with open(filename, 'rib') as file:
        content = file.read()
        print("Binary content:", content)
    
read_binary_file('binary_sample.bin')

#8
def append_to_binary_file(filename, data):
    with open(filename, 'ab') as file:
        file.write(data)

append_to_binary_file('binary_somple.bin', bytes([6, 7, 8, 9]))
print("bytes appended to binary file.")
read_binary_file('binary_sample.bin')
