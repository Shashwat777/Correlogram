from PIL import Image
import numpy
import os
import _pickle as pickle

def compute_dis(dist1,dist2,ncolor):
    summation=0
    cnt=0
    for i in range (0,len(dist1)):
        for j  in range (0,len(dist1[i])):

            diff=dist1[i][j]-dist2[i][j]
            if(diff!=0):
                cnt=cnt+1
            if(diff<0):
                diff=diff*-1
            val=diff/(1+dist1[i][j]+dist2[i][j])
            summation =summation +val
    dis=(summation)/cnt
        
    return(dis)



def get_probdist(im, bins, d):
    colours = []
    parray = numpy.array(im)
    for c1 in bins:
        for c2 in bins:
            for c3 in bins:

                colours.append([c1, c2, c3])
                l = [c1, c2, c3]

    carray = []
    for i in parray:
        arr = []
        n=256/len(bins)
        for j in i:

            r = (j[0]//n)*n
            g = (j[1]//n)*n
            b = (j[2]//n)*n
            index = colours.index([r, g, b])
            arr.append(index)
        carray.append(arr)

    carray = numpy.array(carray)
   

    a = numpy.zeros(shape=(64, len(d), 2))
    for i in range(0, len(carray)):

        for j in range(0, len(carray[i])):
            clr = carray[i][j]
            for z in range(0, len(d)):
                k = d[z]
                for trvlr in range(1, k):
                    try:
                        one = carray[i+trvlr][j+k]
                        if(one == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        two = carray[i-trvlr][j+k]
                        if(two == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        three = carray[i+trvlr][j-k]
                        if(three == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:

                        four = carray[i-trvlr][j-k]
                        if(four == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        five = carray[i+k][j-trvlr]
                        if(five == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        six = carray[i+k][j+rvlr]
                        if(six == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        seven = carray[i-k][j-trvlr]
                        if(seven == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass
                    try:
                        eight = carray[i-k][j+rvlr]
                        if(eight == clr):
                            a[clr][z][0] = a[clr][z][0]+1
                            a[clr][z][1] = a[clr][z][1]+1
                        else:
                            a[clr][z][1] = a[clr][z][1]+1
                    except:
                        pass

    colour_dist_prob = []

    for i in a:
        l = []
        for j in i:
            div = j[0]/j[1]

            if(numpy.isnan(div)):
                l.append(0)
            else:
                l.append(div)

        colour_dist_prob.append(l)

    return([colour_dist_prob,n])

bins = [0, 64, 128, 192]
# # distances
d = [2] 
images=os.listdir("./images")
dict_features={}
c=1
for im in images:
    print (c)
    print (im)

    im="./images/"+im
    image = Image.open(im)
    dist=get_probdist(image,bins,d)
    dict_features[im]=dist
    print (im)
    c=c+1
    


file = open('important', 'wb')
pickle.dump(dict_features, file)
file.close()
file = open('important', 'rb')
print(pickle.load( file))




# s2="red.png"
# im1 = Image.open(s1)
# im2 = Image.open(s2)
# # colour bins

# dist1=get_probdist(im1,bins,d)
# ncolor=dist1[1]
# dist1=dist1[0]
# dist2=get_probdist(im2,bins,d)[0]

# # print (dist1)
# print (s1)
# # print(dist2)
# print (s2)
# print (d)
# print (compute_dis(dist1,dist2,ncolor))
