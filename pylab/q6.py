list1=["said","zeid","27"]
path="/home/said/Desktop/pylab/myfile.txt"
filew= open(path,'w')
for x in list1:
    filew.write(x+" ")
filew.close()
