import sys
i=0
file=open("mytextfile.txt","r")
read =file.read()
l=read.rsplit(" ")
l=list(dict.fromkeys(l))
count=list()
while i<len(l):
    c=read.count(l[i])
    count.append(c)
    i+=1
words=dict(zip(l,count))
words=dict(sorted(words.items(), key=lambda item: item[1]))
n=int(sys.argv[1])
firstN=list(words.items())[:n]
firstN=str(firstN)
firstN=firstN.replace(")","")
firstN=firstN.replace("(","")
firstN=firstN.replace("[","")
firstN=firstN.replace("]","")
firstN=firstN.replace("'","")
firstN=firstN.rsplit(",")
i=0
while(i<len(firstN)-1):
    print(firstN[i]+firstN[i+1]+" times")
    i+=2













