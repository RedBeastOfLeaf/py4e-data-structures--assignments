my_list = []
fhand = open('romeo.txt')
for line in fhand:
    words = line.split()
    for word in words:
        if word in my_list:
            continue
        my_list.append(word)
print(sorted(my_list))        
        
