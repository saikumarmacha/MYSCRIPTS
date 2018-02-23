import json
#loading data from json files that has some mistakes in it
json_data1 = open("first Json file Path", 'r')
data1 = json.load(json_data1)
#the below file is the source of truth file
json_data2 = open("second Json file path", 'r')
data2 = json.load(json_data2)
#neglecting the first datapoint i.e., channels for first file
data3 = data1["channels"]
#neglecting the first datapoint i.e., channels for first file
data4 = data2["channels"]
#print(data3)

#creating empty lists where list1 is the list of all channels in data1
#and list2 is the list of all channels in data2
list1 = []
list2 = []
for i in data3:
    list1.append(i)
for j in data4:
    list2.append(j)
#joining both the lists to a single list
list3 = list1 + list2
#removing duplicates in a list3(which is the combination of list of channels of given two json files)
list4 = []
for i in list3:
    if i not in list4:
        list4.append(int(i))

list4.sort(key = int)
#print(list4)
#converting the datatype of list4 into unicode
list5 = []
for m in list4:
    n = str(m).encode("utf-8").decode("utf-8")
    list5.append(n)
#opening an empty list dic
dic={}
#based on the keys in both the files(which are nothing but channel numbers) itterating through both the files
# and updating the empty dictonary(dic) with all the union of channel numbers and there respective values
#here the source of truith is the newton file and hence we are printing the key values from newtow  file and later we are printing given wrong files
for A in list5:
    if A in data4.keys():
        dic[A] = data4[A]
    elif A in data3.keys():
        dic[A] = data3[A]
#adding the dic as a value to "channels" key and saving them to a dictonary
dic2 = {}
dic2["channels"] = dic
#Printing the channels with union of both files
with open("Result JSON file after comparing", 'w') as fp:
    json.dump(dic2, fp, indent = 4)
