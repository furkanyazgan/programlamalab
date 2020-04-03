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

temp = get_random_list()

print(temp)
print(hist_dict(temp))
print(hist_tuple(temp))

print(mode_hist_dict(hist_dict(temp)))

print(mode_hist_list(hist_tuple(temp)))



