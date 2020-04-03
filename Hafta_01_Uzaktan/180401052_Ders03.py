import random

def get_random_list(n=10,x=-5,y=5):
    random_list=[]
    for i in range (n):
        random_list.append(random.randint(x,y))
    return random_list

def hist_dict(list):
    frekans = {}
    for item in list:
        if item in frekans:
            frekans[item]= frekans[item]+1
        else:
            frekans[item] =1
    return frekans

def hist_tuple(list_1):
    frekans_list =[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frekans_list)):
            if (list_1[i]==frekans_list[j][0]):
                frekans_list[j][1] = frekans_list[j][1]+1
                s=True
        if(s == False):
            frekans_list.append([list_1[i],1])
    return frekans_list

def mode_hist_dict(dict_hist):
    frekans_max = -1
    mode = -1
    for key in dict_hist.keys():
        if (dict_hist[key] > frekans_max):
            frekans_max = dict_hist[key]
            mode = key
    return mode,frekans_max

def mode_hist_list(hist):
    frekans_max = -1
    mode = -1
    for item, frekans in hist:
        if (frekans > frekans_max):
            frekans_max = frekans
            mode = item
    return mode,frekans_max

def liner_index_search(list,item):
    found=(-1,-1)
    n = len(list)
    for index in range(n):
        if (list[index]==item):
            found=(list[index],index)
    return found

def my_mean(list):
    s,t = 0,0
    for item in list:
        s = s+1
        t=t+item
    mean = t/s
    return mean

def bubble_sort(list):
    n= len(list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(list[j]<list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

def binary_search(list,item):
    found=(-1,-1)
    low = 0
    high=len(list)-1

    while(low<=high):
        mid = (low+high)//2
        if (list[mid]==item):
            return list[mid],mid
        elif list[mid]>item:
            high=mid-1
        else:
            low=mid+1

    return found

def my_median(list):
    list_2=bubble_sort(list)
    n = len(list_2)
    if (n%2==1):
        middle=int(n/2)+1
        median=list_2[middle]
    else:
        middle_1=list_2[int(n/2)]
        middle_2=list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
    return median
##temp = get_random_list(5,-5,5)

##print(bubble_sort(temp))
##print(hist_dict(temp))
##print(hist_tuple(temp))
##print(mode_hist_dict(hist_dict(temp)))
##print(mode_hist_list(hist_tuple(temp)))

#print(liner_search(temp,4))

##print(my_mean(temp))

##print(bubble_sort(temp))

##print(binary_search(bubble_sort(temp),3))

##print(my_median(temp))