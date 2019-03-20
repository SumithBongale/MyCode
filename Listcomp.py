list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[ i for i in list1 if i%2==0]
# print(list2)

list2 = ["Even" if i%2==0 else "Odd" for i in list1]
print(list2)
