file = open('log.txt')
date = open('date.txt', 'a')
time = open('time.txt', 'a')
user_name = open('user_name.txt', 'a')
status = open('status.txt', 'a')
for line in file:
    data = line.split()
    date.write(data[0]+'\n')
    time.write(data[1][:-1]+'\n')
    user_name.write(data[2][:-1] +'\n')
    for i in range(3):
        data.pop(0)
    status.write(" ".join(data)+'\n')
    