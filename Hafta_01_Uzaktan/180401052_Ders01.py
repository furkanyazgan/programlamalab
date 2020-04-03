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


temp = get_random_list()

print(temp)
print(hist_dict(temp))
print(hist_tuple(temp))






