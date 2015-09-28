import re
import csv
import random
import numpy
from collections import defaultdict
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from itertools import cycle
__author__ = 'roopeshmangal'
fold_name = "/Users/roopeshmangal/PycharmProjects/similar_document/"
file=fold_name+"doc_content"
list_of_set_1=[]
list_of_set=[]
list_of_set_3=[]
s=set()
s1=set()
doc_list=[]
def jacard(s1,s2):
    if len(s1|s2)==0:
       return 0
    return float(len(s1&s2))/len(s1|s2)
#stopset = set(stopwords.words('english'))
with open(file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=";", quotechar='|')
    for row in spamreader:
       # data=row.split(';')
        doc_id=row[0]
        doc_list.append(doc_id)
        content=row[1].replace('\n', '')
        tokens = re.findall(r'\w+',content,flags = re.UNICODE | re.LOCALE)
        # s1 = set(w for w in tokens if not w in stopset)
        licycle = iter(tokens)
        nextelem = licycle.next()
        size=0
        while size<(len(tokens)-1):
              thiselem, nextelem = nextelem, licycle.next()
              item=thiselem+" "+nextelem
              s.add(item)
              size=size+1
        list_of_set.append(s)
        #list_of_set_1.append(s1)
        s=set()
        #s1=set()
#08049597571
i=0
j=0
print len(doc_list)
print len(list_of_set)
print doc_list.index('805050389594073')
print doc_list.index('10153424555010709')
print doc_list.index('10153176685581647')
list_item=[]
list_dummy=[]
for i in range(2,10):
 list_dummy[:]=[]
 list_item[:]=[]
 count=0
 #dataCSV = open('ProgramCheck_'+str(i)+'.csv', 'w')
 #writer = csv.writer(dataCSV, dialect='excel')
 #dataCSV1 = open('roopesh.csv', 'w')
 #writer1= csv.writer(dataCSV1, dialect='excel')
 #writer.writerow(['similarity', 'me', 'my-similaritems '])
 index=-1
 for item in list_of_set:
    index=index+1
    if index==82:
        print "chut"
    me=doc_list[index]
    if not me in list_dummy:
      list_dummy.append(me)
      max=0
      dum_item=""
      list_item[:]=[]
      #dis=float(i)/10
      dis=float(i)/10
      index1=index
      for item1 in list_of_set[index+1:len(list_of_set)]:
         index1=index1+1
         if not doc_list[index1] in list_dummy:
           jac=jacard(item,item1)
           #index1=list_of_set.index(item1)
           if index==82 and index1==7274:
               print "loda"
           #writer1.writerow([jac,doc_list[list_of_set.index(item1)]])

           if jac>dis:
              if numpy.isclose(jac,max, rtol=1e-05, atol=1e-08, equal_nan=False):
                   list_item.append(doc_list[index1])
              if (jac>max) :
                list_item[:]=[]
                max=jac
                dum_item=doc_list[index1]
                list_item.append(dum_item)
      list_dummy=list_dummy+list_item
      #writer1.writerow([count,list_dummy])
      count=count+1
     # writer.writerow([count,max,doc_list[list_of_set.index(item)],list_item])
 print count
#  print doc_list.index("86cc23673e9b0a05d22faccc4f9d870a61f698349155d67b9013adf402d891d2")
# dic_1={}
# dic_final=dict((doc_list[list_of_set.index(s1)],len(s1)) for s1 in list_of_set)
# l= sorted(dic_final.items(), key=lambda x:x[1])
# # for item in l:
# #     print item
# print len(doc_list)
# print len(list_of_set)
# print len(list_of_set_1)
#
#
# m= len(dict((list_of_set_1.index(s7),jacard(s7,s8))for s7 in list_of_set_1 for s8 in list_of_set_1 if not s7==s8))
# n=len(dict((list_of_set.index(s5),jacard(s5,s6))for s5 in list_of_set for s6 in list_of_set if not s5==s6))
# # print m
# # print n
# # dic_1=defaultdict(lambda: 0)
# # dic=defaultdict(lambda: 0)
# # small_key="91ce641b3ab426ec8a32d91072b29e11e2a41a904bdc7e7d3d067e137dada132"
# # sex=doc_list.index(small_key)
# # big_key="0d61e35ef89100a3aa750988555bc4dc7f99d30667a16c0b78f963db00e7e7e8"
# # chut=doc_list.index(big_key)
# # s=set()
# # s1=set()
# # s=list_of_set[sex]
# # s1= list_of_set[chut]
# # print s
# # print s1
# # print len(s1&s)
# # print len(s|s1)
# # print (s1&s)
# # print len(doc_list)
# # print len(list_of_set)
# dic_1=dict((doc_list[list_of_set_1.index(s3)]+","+doc_list[list_of_set_1.index(s4)],jacard(s3,s4)) for s3 in list_of_set_1 for s4 in list_of_set_1 if  not s3==s4)
# dic=dict((doc_list[list_of_set.index(s1)]+","+doc_list[list_of_set.index(s2)],jacard(s1,s2)) for s1 in list_of_set for s2 in list_of_set if  not s1==s2)
# print len(dic_1)
# print len(dic)
# #dic1=dict((doc_list[list_of_set_1.index(s1)]+","+doc_list[list_of_set_1.index(s2)],jacard(s1,s2)) for s1 in list_of_set_1 for s2 in list_of_set_1 if  not s1==s2)
# #list_keys1=[dic1.keys()]
# # dic_final={}
# # size=0
# dic_final=dict((key,float(dic_1[key]+dic[key])/2) for key in dic_1)
# l=[]
# m=[]
# n=[]
# x=0.0001
# y=0.1001
# for i in range(9):
#     l=filter(lambda key :x<dic[key]<y ,dic)
#     m=filter(lambda key :x<dic_1[key]<y ,dic_1)
#     n=filter(lambda key :x<dic_final[key]<y ,dic_final)
#     print "len of 2 gram between" , x ,y , "is" ,len(l)
#     randomindex = random.sample(xrange(len(l)-1), 10)
#     for item in randomindex:
#          print l[item]
#     print "len of 1 gram between" , x ,y , "is" ,len(m)
#     randomindex = random.sample(xrange(len(m)-1), 10)
#     for item in randomindex:
#          print m[item]
#     print "len of avg gram between" , x ,y , "is" ,len(n)
#     randomindex = random.sample(xrange(len(n)-1), 10)
#     for item in randomindex:
#          print n[item]
#     x=x+0.1
#     y=y+0.1
#     l[:]=[]
#     m[:]=[]
#     n[:]=[]
# # for key in dic:
# #     if dic[key]>0.1 and dic[key]<0.2:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #     if dic_1[key]>0.1 and dic_1[key]<0.2:
# #         #print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #     if dic[key]>0.2 and dic[key]<0.3:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #     if dic_1[key]>0.2 and dic_1[key]<0.3:
# #         #print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #     if dic[key]>0.3 and dic[key]<0.4:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.3 and dic_1[key]<0.4:
# #         #print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #      if dic[key]>0.4 and dic[key]<0.5:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.4 and dic_1[key]<0.5:
# #         #print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #      if dic[key]>0.5 and dic[key]<0.6:
# #        # print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.5 and dic_1[key]<0.6:
# #         print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #      if dic[key]>0.6 and dic[key]<0.7:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.6 and dic_1[key]<0.7:
# #         print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #      if dic[key]>0.7 and dic[key]<0.8:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.7 and dic_1[key]<0.8:
# #         print key , dic_1[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic:
# #      if dic[key]>0.8 and dic[key]<0.9:
# #         #print key , dic[key]
# #         size=size+1
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print "roopesh"
# # print size
# # size=0
# # for key in dic_1:
# #      if dic_1[key]>0.8 and dic_1[key]<0.9:
# #         print key , dic_1[key]
# #         size=size+1
# # print size
# # for key in dic_1:
# #      if dic_1[key]>0.9 and dic_1[key]<1.0:
# #         print key , dic_1[key]
# #         size=size+1
# # print size
# # print "roopesh"
# # print len(dic)
# # print len(dic_1)
# # print len(dic_final)