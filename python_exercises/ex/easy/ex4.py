def find_number(list,num):
    list.sort()
    for i in list:
        if i==num :
            print("True")
            return True
        
    print("False")
    return False
list=[3,6,9,5,1,0]
num=3
find_number(list,num)
#done