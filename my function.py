


def write_from_TinL(file,list,sep):
    with open(file,"w") as f:
        for i in list:
            f.write(f"{sep}".join(map(str,i))+"\n")

def get_from_sep_file(file,sep):
    list_make=[]
    with open(file,"r")as b:
         for line in b:
            list_make.append(tuple(map(lambda x:str(x)if x.isalpha() else int(x),line.split(sep))))
         return list_make
   

def make_dict_valu_to_key(n):
     d={}
     for i in n.keys():
         d[n[i]]=i
     return d    

def remove_white_order(n):
    repited=set()
    for i in n:
        if i not in repited:
            yield i
            repited.add(i)

def remove_repit_all(n,key=None):
    see=set()
    for i in n:
        val=i if key==None else key(i)            
        if val not in see:
            yield i
            see.add(val)        

def sum_digit(n):
    s=0
    while n>0:
        s+=n%10
        n=n//10
    return s
print(sum_digit(123))    
       
def check_pa_ne(n):
    check=False
    if  (n[0]=="-" or n[0].isdigit()) and n[1:].isdigit():
        check=True
    return check    

from itertools import groupby
a=[{"a":1,"age":98,"work":"ioyg"},
{"b":1,"age":98,"work":"ioyg"},
{"c":3,"age":9,"work":"ioyg"},
{"f":1,"age":8,"work":"ioyg"}]
dic={}
for i in a:
    dic.setdefault(i["age"],[]).append(i)
print(dic)    
a=sorted(a,key=lambda x:x["age"])

print(list(groupby(a,key=lambda x:x["age"])))

def rindex_list(listt,element):
    listt=list(listt)
    return len(listt)-list(reversed(listt)).index(element)-1

print(rindex_list([9,9,12,7,9,0],9))