str1="The sky is blue"
dict1={}
#list1=str1.split()
for i in str1:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1
print(dict1)
