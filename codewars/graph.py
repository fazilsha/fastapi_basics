values = input("enter values with space inbetween and dont append any space at the end:")
values = values.split(" ")
v = []

for i in values:  # creating the string values into individula integer vaules
    v.append(int(i))

summ = 0
rmax = 0
for i in range(len(v)):  # Calculating maxima for the given input
    if i % 2 == 0:
        summ += v[i]

    else:
        summ -= v[i]

    rmax = max(summ, rmax)

rmax *= 2
cmax = 0

for i in v:  # calculating number of columns
    cmax += i

# print(cmax)

g = []  # graph storing variable

for i in range(rmax):  # creating two dimentional array and populating it with 0's
    a = []
    for j in range(cmax):
        a.append(' ')

    g.append(a)

# vmax=len(v)-1
d = 0  # keeps track of type of pattern/direction to be printed
es = int(rmax // 2) - 1  # keeps track of even pattern start postion
# print(es)
ee = es - v[0] + 1  # keeps track of even pattern end postion
os = 0  # keeps track of odd pattern start postion
oe = 0  # keeps track of odd pattern end postion
i = 0  # Iteration variable

while len(v) and i < cmax:  # runs untils list has no values

    if d % 2 == 0:  # checks for pattern direction
        for j in range(es, ee - 1, -1):  # appending even pattern to the array/matrix
            g[j][i] = '/'
            i += 1

        if len(v) != 1:  # checking condition and calculating the odd pattern starting and ending postion
            # print(v[0],i)
            v.pop(0)
            # print(v[0])
            os = ee
            oe = ee + v[0]

    else:
        for j in range(os, oe, 1):  # appending odd pattern to the array/matrix
            g[j][i] = '\\'
            i += 1

        if len(v) > 1 and v[1] > oe:  # checking condition and calculating the even pattern starting and ending postion
            v.pop(0)
            es = oe - 1
            ee = v[0] - oe

        elif len(v) > 1:
            v.pop(0)
            es = oe - 1
            ee = oe - v[0]

    d += 1

im = 0  # Stores maxima occuring column
im = g[0].index('/')
# print(im)

fg = []  # final graph

for i in range(rmax + 2):  # creating two dimentional array and populating it with ' '
    a = []
    for j in range(cmax):
        a.append(' ')

    fg.append(a)

fg[0][im - 1] = '  o'
fg[1][im - 1] = ' <|>'

for n in range(2, rmax + 2):
    for j in range(cmax):
        fg[n][j] = g[n - 2][j]

for n in range(rmax + 2):  # printing the final pattern/graph
    for j in range(cmax):
        print(fg[n][j], end="")

    print()





