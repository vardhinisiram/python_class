input_file = 'sample.txt'
# try and except


#with open(input_file, 'r') as file:
#    print(file.readlines())
try:  # exception...
    with open(input_file, 'a') as file: # a file cannot be opened if doesn't exist.
        print(file.readlines())
        # file.write("Hello")   # as we have opened that file with read, we cannot write.
        print(10/0)
except FileNotFoundError as e:
    print("There is no file called sample.txt")
except IOError as e:
    print("not writable exception", e)
    with open(input_file, 'r') as file:
        print(file.read ())
except Exception as e:
    print("Universal errors", e)


print("Hello world")

