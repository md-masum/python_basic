# This script demonstrates how to read from a file in Python
# Open a file in read mode and print its content, it will read the entire file at once
my_file = open("test.txt", "r")
content = my_file.read()
print(content)
my_file.close() # The file is now closed, so we cannot read it again without reopening


my_file = open("test.txt", "r")
print(my_file.read())
print(my_file.read())  # This will read nothing as the file pointer is at the end
my_file.close()


# Open the file again to read it line by line
my_file = open("test.txt", "r")
print(my_file.readline()) # This reads the first line
print(my_file.readline()) # This reads the second line
print(my_file.readline()) # This reads the third line
my_file.close()


# Open the file again to read all lines at once into a list
my_file = open("test.txt", "r")
print(my_file.readlines()) # This reads all lines into a list
my_file.close()

# Using a context manager to handle file opening and closing automatically
with open("test.txt", "r") as my_file:
    print(my_file.read())

# Writing to a file
with open("newFile.txt", "w") as my_file: #mode "w" means write, it will overwrite the file if it exists, and create it if it does not
    my_file.write("This is a new line.\n")
    my_file.write("This is another new line.\n")


# Appending to a file
with open("test.txt", "a") as my_file: # mode "a" means append, it will add to the end of the file without overwriting
    my_file.write("This is an appended line.\n")


with open("test.txt", "r+") as my_file: # mode "r+" means read and write, it will not truncate the file
    print(my_file.read())
    my_file.write("This is a new line added to the file.\n")


#list of modes for file handling
# "r" - Read (default mode, file must exist)
# "w" - Write (overwrites the file if it exists, creates a new file if it does not)
# "a" - Append (adds to the end of the file, creates a new file if it does not exist)
# "r+" - Read and Write (file must exist, does not truncate the file)
# "w+" - Write and Read (overwrites the file if it exists, creates a new file if it does not)
# "a+" - Append and Read (adds to the end of the file, creates a new file if it does not exist)
# "b" - Binary mode (used for binary files, e.g., images, audio files)
# "t" - Text mode (default mode, used for text files)


# Reading a file in binary mode
with open("test.txt", "rb") as my_file:  # mode "rb" means read in binary mode
    content = my_file.read()
    print(content)  # This will print the binary content of the file

# Writing to a file in binary mode
with open("binaryFile.bin", "wb") as my_file:  # mode "wb" means write in binary mode
    my_file.write(b"This is a binary file.\n")



#read write file with try except
def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
        return None
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
        return None
def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
            print(f"Content written to {file_path} successfully.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")
# Example usage
file_path = "example.txt"
write_file(file_path, "Hello, World!\nThis is a test file.")
read_content = read_file(file_path)
