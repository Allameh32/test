


def copress(n):
    d={}
    for i in n:
        d[i]=d.setdefault(i,0)+1
    
    k=[j for j in d.items() if j[1]>1]
    anser=""
    for i in k:
        anser+="".join(str(j) for j in i)
    return "".join((anser))

n=input()
while True:
    com=copress(n)
print("888888888888888888888")
print("888888888888888888888")
print("888888888888888888888")
print("88888888hsfgsdfsfds8888")