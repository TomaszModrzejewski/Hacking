import sys


def main():
    N, capacities_list, notsinks = readfile(sys.argv[1])
    for i in range(N):
        if notsinks[i] == 0:
            index = i
    capacities_list.pop(index)
    capacity = str(min(capacities_list))
    new_file = open("myfile.txt", 'w')
    new_file.write(capacity)
    new_file.close()




def readfile(path):
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
    while (counter<N-1):
        indexes = line.split(" ")
        notsinks[int(indexes[0])] = 1
        print(int(indexes[0]))
        line = file.readline()
        counter+=1
    file.close()
    return N, capacities_list, notsinks








if(__name__ == "__main__"):
    main()