import sys
import csv

def histogram_dict(list):
    frekans = {}
    for item in list:
        if item in frekans:
            frekans[item]= frekans[item]+1
        else:
            frekans[item] =1
    return frekans

def mean(list):
    s,t = 0,0
    for item in list:
        s = s+1
        t=t+item
    mean = t/s
    return mean

def median(my_list):
    n = len(my_list)
    if n%2 == 1:
        middle = int(n/2)
        median = my_list[middle]

    else:
        middle_1 = int(n/2)
        middle_2 = int(n/2)+1
        median = (my_list[middle_1-1]+my_list[middle_2-1])/2

    return median

def bubble_sort(list):
    n= len(list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(list[j]<list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list


input_path = sys.argv[1]+ "\\input_hw_2.csv"
output_path = sys.argv[2]+ "\\180401052_hw_2_output.txt"

input=open(input_path,"r+",encoding="utf-8")
contents = input.read()

hist_list = []

words = contents.split("\n")

for i in words:
    try:
        x = i.split(";")[3].split("-")[1]
        hist_list.append(x)
    except IndexError:
        pass



end_list = [(k) for k in histogram_dict(hist_list).values()]


median_end =median(bubble_sort(end_list))
mean_end =mean(end_list)

out_file = open(output_path,"w",encoding="utf-8")

out_file.write("Medyan : "+str(median_end)+"\n"+"Ortalama : "+str(mean_end))

