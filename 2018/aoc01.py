global num_list
global curVal
global found
num_list = {0:1}
curVal = 0
found = False

def read_loop():
    global num_list
    global curVal
    global found
    with open("input01.txt", "r") as file:
        for line in file:
            num = int(line)
            curVal += num
            if curVal in num_list:
                print (curVal)
                found = True
                return
            num_list[curVal] = 1
    return


while(not found):
    read_loop()
