import os
import re
all_list=[]
len_all_list=0
my_hist={}


def dic_max(temp_dict):
    if not temp_dict:
        return " "
    max_key = max(temp_dict, key=temp_dict.get)
    return max_key



def get_words(my_file):
    my_list=[]
    f=open(my_file,"r+")
    contents=f.readlines()
    for line in contents:

        words=line.split(" ")
        for word in words:
            if (word.count("\n") > 0):
                word=word[:len(word) -1]
            if(word.count(",") > 0 or word.count(".") > 0):
                word = word[:len(word) -1]
            my_list.append(word)
    f.close()
    return my_list


def get_hist(str):

    if str in my_hist.keys():
        my_hist[str]= my_hist[str]+1
    else:
        my_hist[str]=1




def search (str):
    my_hist.clear()

    len_word = (str.count(" ")+1)
    if(len_word > 5):
        return("error_1")
    all_string=""

    for index in range(0,len_all_list-len_word):

        for index_2 in range(index,(index+len_word)):
            all_string+=all_list[index_2]+" "
        all_string=all_string[:len(all_string)-1]

        if (all_string == str):
            get_hist(all_list[index+len_word])
        all_string = ""
    return "true_1"




def get_files(path_1):
    file_s=[file for file in my_list if os.path.isfile(file)]
    return file_s



txt_list=os.listdir(os.getcwd()+"\\data_files")
for txt in txt_list:
    all_list.extend(get_words(os.getcwd()+"\\data_files\\"+txt))

len_all_list=len(all_list)



input=open(os.getcwd()+"\\input.txt","r+",encoding="utf-8")
input_list=input.readlines()
input.closed

input=open(os.getcwd()+"\\input.txt","a",encoding="utf-8")


for w in range (len(input_list)):
    input_list[w] = re.sub('\n', '', input_list[w])

input.write("\n...")
for item in input_list:
    if(search(item) == "error_1"):
        input.write("\n" + item + "-hatalı giriş : en fazla 5 kelime girmelisiniz")
    else:
        input.write("\n"+item +"-"+ dic_max(my_hist))
