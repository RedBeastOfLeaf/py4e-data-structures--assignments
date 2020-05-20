fname = input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print('File cannot be opened: ',fname)
    exit()
count = 0
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        print(line[1])
        count = count + 1
print("There were",count,"lines in the file with From as the first word")      
