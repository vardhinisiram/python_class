
"""
sample_file = open('sample.txt', 'a') 

print(dir(sample_file))
#for line in sample_file.readlines():
#    print(line)
sample_file.write('10\n')

#print(vals)
sample_file.close()
"""


with open('sample.txt', 'r') as sample_file:
    print(sample_file.tell())
    print(sample_file.readline())
    print(sample_file.tell())
    print(sample_file.readline())
    #sample_file.write("New lines here\n")
    print(sample_file.tell())

    sample_file.seek(0 # resetting the pointer...
    print("============================")
    for line in sample_file.readlines():
        print(line, sample_file.tell())



