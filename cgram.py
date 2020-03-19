from PIL import Image
import numpy
import os
import _pickle as pickle

def compute_dis(dist1,dist2):
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

def reduce_image(img1):
    basewidth = 300
    wpercent = (basewidth / float(img1.size[0]))
    hsize = int((float(img1.size[1]) * float(wpercent)))
    image = img1.resize((basewidth, hsize), Image.ANTIALIAS)
    return (image)

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
                for trvlr in range(1, k+1):
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
                        six = carray[i+k][j+trvlr]
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
                        eight = carray[i-k][j+trvlr]
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

    return(colour_dist_prob)

bins = [0, 64, 128, 192]
# # distances
d = [2] 



bins = [0, 64, 128, 192]
# # distances
d = [2] 
image1="7.jpg"
image2="red2.png"
path="/Users/shashwatjain/desktop"




im1=path+"/"+image1
im2=path+"/"+image2

img1 = Image.open(im1)
img2 = Image.open(im2)

img1=reduce_image(img1)
img2=reduce_image(img2)

dist1=get_probdist(img1,bins,d)
dist2=get_probdist(img2,bins,d)
print (compute_dis(dist1,dist2))

    