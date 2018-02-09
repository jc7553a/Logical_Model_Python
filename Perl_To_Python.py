import re
import numpy as np


#Returns a List of Functions Stripped of Garbage
def get_functions(file):
    data = []
    # Read File
    for line in open(file).readlines():
        line = line.split(" ")
        data.append(line)

    #Strip out Garbage, and Covert ^ to ** in Functions
    regex = re.compile('x[1-9]+')
    for i in range(len(data)):
        data[i] = data[i][2].strip('\n')
        data[i] = data[i].replace("^", "**")
        #data[i] = list(data[i])
        #print(regex.findall(data[i]))    

    return data



def convertFunction(data):
    reg = re.compile('[0-9]')
    newData = []
    i =0
    while i <(len(data)):
        if data[i] == 'x':
            newData.append(data[i])
            newData.append('[')
            flag = True
            i+=1
            while (flag):
                if reg.match(data[i]) != None:
                    newData.append(str(int(data[i])-1))
                    i+=1
                else:
                    newData.append(']')
                    flag = False
        else:
            newData.append(data[i])
            i+=1
    return ''.join(newData)
            

def convert_Int_To_State(n):
    global num_nodes, num_states
    i = 1
    quotient = 1
    flag = True;
    states = []
    n -=1
    while(flag):
        quotient = int((n)/num_states)
        remainder = n%num_states
        states.append(remainder)
        n = quotient
        if quotient == 0:
            flag = False
            break
    dif = num_nodes - len(states)
    if dif > 0:
        for i in range(dif):
            states.append(0)
    states.reverse()
    return states

def convert_from_state_to_integer(state):
    int_rep = 1
    for i in range(num_nodes):
        int_rep += state[num_nodes-i-1]*(num_states**i)
    return int_rep

def get_nextstate(state):
    global num_states
    x = convert_Int_To_State(state)
    temp = functions
    evaluations = []
    for i in range(len(temp)):
        evaluations.append(eval(temp[i])%num_states)
    nextState = convert_from_state_to_integer(evaluations)
    return nextState

#Globals
functions = get_functions("func_example.txt")
num_nodes = len(functions)
num_states = 3
stateSpace_size = num_states**num_nodes
length = 5
mySet = set()
attractor_table = {}


def starting():
    global functions, stateSpace_size, length
    print("State space " + str(stateSpace_size))
    i = 1
    while i < (stateSpace_size):
        if i in mySet:
            pass
            i+=1
        else:
            #if i ==9:
            #    exit()
            arr = [i]
            print("Start Array " + str(arr[-1]))
            flag = True
            while flag:
                n = 1
                while n <=(length):
                    arr.append(get_nextstate(arr[-1]))
                    n+=1
                print("Array" + str(arr))
                arr_Size = len(arr)
                print("Array Size " + str(arr_Size))
                for j in range(arr_Size-1):
                    k = j+1
                    while k < arr_Size:
                        if arr[j] == arr[k]:
                            sub_array = arr[j:k]
                            print("Sub Array " + str(sub_array))
                            for item in sub_array:
                                mySet.add(item)
                        #if sortedAttractor not in mySet:
                            #print(sub_array)
                        k+=1
                    flag = False
            i+=1
                    
                    

if __name__ == '__main__':
    for i in range(len(functions)):
        functions[i] = (convertFunction(functions[i]+'+0'))
    starting()
  
    
