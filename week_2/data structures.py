my_list=[]
print(my_list)

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
my_list[1]=15
print(my_list)
list=[50,60,70]
my_list.extend(list)
print("list after append:", my_list)
del my_list[6]
print(my_list)
for list in my_list:
    print(my_list)
print(my_list[2])   
