def pyramid(balls):
    if balls == 1:
        return 1
    else:
        i=0
        lst=[]
        while True:
            i+=1
            lst.append(i)
            print(i)
            if sum(lst)==balls:
                return len(lst)
            elif sum(lst)>balls:
                print(len(lst)-1)
                return len(lst)-1
def paul(x):
    points = {"kata":5,"Petes Kata":10,"life":0,"eating":1}
    op=sum([points[p] for p in x])
    if op < 40:
        return "Super happy!"
    elif op<70 and op>=40:
        return "Happy!"
    elif op<100 and op>=70:
        return "Sad!"
    else:
        return "Miserable!"
def binchange(x):
    l=list(x)
    for i in range(len(x)):
        if l[i] == "0":
            l[i] = "1"
        else:
            l[i] = "0"
    return "".join(l)

def meeting(rooms):
    return rooms.index("O") if "O" in rooms else "None available!"

def cat_mouse(x):
    return "Caught!" if x.count(".")<=3 else "Escaped!"
#cat_mouse("c...m")

def anagrams(w1, w2):
    l1=list(w1)
    l1.sort()
    nl = []
    print(l1)
    for w in w2:
        l2 = list(w)
        l2.sort()
        print(l1,l2)
        if l2 == l1:
            nl.append(w)
    print(nl)

    return nl
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])