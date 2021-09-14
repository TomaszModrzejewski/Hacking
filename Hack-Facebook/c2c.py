import sys


def main():
    N, capacities_list, listoflists = readfile(sys.argv[1])
    sum = 0
    for lst in listoflists:
        lst.pop()
        sum+=min(lst)
    capacity = str(sum)
    new_file = open("output.txt", 'w')
    new_file.write(capacity)
    new_file.close()




def readfile(path):
    listoflists = []
    capacities_list = []
    file = open(path, 'r')
    N = int(file.readline())
    notsinks = [0 for i in range(N)]
    line = file.readline() #empty line
    line = file.readline() #
    while (line!='\n'):
        capacity = int(line)
        capacities_list.append(capacity)
        line = file.readline()
    #we have now reached an empty line
    line = file.readline() #going to 3rd part
    counter = 0
    first_index = 0
    second_index = 0
    prev_index = 0
    while (counter<N-1 or line or (line!='\n') or (line!='') or (line!="\r\n")):
        if (line==''):
            break
        indexes = line.split(" ")
        if (prev_index!=int(indexes[0])):
            listoflists.append(capacities_list[first_index:prev_index+1])
            first_index = int(indexes[0])
        prev_index = int(indexes[1])
        line = file.readline()
    listoflists.append(capacities_list[first_index:])
    file.close()
    return N, capacities_list, listoflists








if(__name__ == "__main__"):
    main()