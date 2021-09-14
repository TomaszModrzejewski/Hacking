import sys


def main():
    N, capacities_list, sources_list, linesfromindex = readfile(sys.argv[1])
    residuals = [i for i in capacities_list]
    second_line = []
    print(sources_list)
    print([capacities_list[i] for i in sources_list])
    print([linesfromindex[i] for i in sources_list])
    for source in sources_list:
        for i in linesfromindex[source]:
            second_line.append(i)
            if (residuals[i]>0):
                residuals[i]-=capacities_list[source]
    sum = 0
    second_line_set = set(second_line)
    second_line = list(second_line_set)
    print(second_line)
    for second_tier in second_line: 
        if (residuals[second_tier]<0):
            sum+=capacities_list[second_tier]
        else:
            sum+=capacities_list[second_tier]-residuals[second_tier]
    capacity = str(sum)
    new_file = open("output.txt", 'w')
    new_file.write(capacity)
    new_file.close()




def readfile(path):
    capacities_list = []
    file = open(path, 'r')
    N = int(file.readline())
    linesfromindex = [[] for i in range(N)]
    sources =[0 for i in range(N)]
    line = file.readline() #empty line
    line = file.readline() #
    while (line!='\n'):
        capacity = int(line)
        capacities_list.append(capacity)
        line = file.readline()
    #we have now reached an empty line
    line = file.readline() #going to 3rd part
    counter = 0
    while (counter<N-1 or line or (line!='\n') or (line!='') or (line!="\r\n")):
        if (line==''):
            break
        indexes = line.split(" ")
        sources[int(indexes[1])] = 1
        linesfromindex[int(indexes[0])].append(int(indexes[1]))
        line = file.readline()
    file.close()
    sources_list = []
    for index in range(N):
        if sources[index]==0:
            sources_list.append(index)
    print(linesfromindex.count([]))
    return N, capacities_list, sources_list, linesfromindex








if(__name__ == "__main__"):
    main()