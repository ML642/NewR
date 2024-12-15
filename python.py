# [1,2,3,4,5,6]
def check(ciag,index1,index2):
            print(Startlist)
            x = int(input())
            y = int(input())
            if x == 2 and y == 0 :
                print(K2_0K(ciag,index1,index2))
            if x == 2 and y == 1 :
                print(K2_1K(ciag,index1,index2))
            if x == 2 and y == 2:
                print(K2_2K(ciag,index1,index2)) 
#            if x == 1 and y == 1:
                


def K2_0K (list , index1 , index2) :
     list1 = [0,1,2,3]
     list1.remove(index1)
     list1.remove(index2)
     
     list[list1[0]] = 5
     
     print(list)
      
     
     z = int(input())
     t = int(input())
     
     if( z == 3 ):
         list[list1[1]]=6
         print  (list)
         quit() 
     if( z == 2 and t==1):
         list[list1[1]]=5
         list[list1[0]]=6
         print(list)
         quit()
     
     #list[list1[0]] , list[list1[1]] =  list[list1[1]] , list[list1[0]]       
     return list       
def K2_2K (list , index1 , index2):
    list1 = [0,1,2,3]
    list1.remove(index1)
    list1.remove(index2)
    list[list1[0]] , list[list1[1]] =  list[list1[1]] , list[list1[0]]
    return list 
def K2_1K (list , index1 , index2) :
    list1 = [0,1,2,3]
    list1.remove(index1)
    list1.remove(index2) 
    list[list1[0]] , list[list1[1]] =  list[list1[1]] , list[list1[0]]
    K3_0K( list , index1, index2 )
    
def K3_0K (list,index1,index2):
    list1 = [0,1,2,3]
    list1.remove(index1)
    list1.remove(index2)
    value =  list[list1[1]]
    list[list1[1]]=5
    
    x = int(input(x))
    y = int(input(y))
    if(x == 2 and y == 1):
        list[list1 [0]]=5
        list[list1 [1]]=value
    if(x == 2 and y == 0):
        list[list1[0]]=6
        list[list1 [1]]=value
    if(x==3):
        list[list1[1]]=6
            
    print(list) 
# def K1_1 ( list , index1 , index2 ) :
#     list1 = [0,1,2,3]
#     value2 = index1
#     list1.remove(index1)
#     value = index2
#     list1.remove(index2)
#     list[value] , list[list1[1]] =  list[list1[1]] , list[value]
#     print(list)
#     x = input()
#     y = input()
#     if x == 1 :
#         KEYINDEX1 = value2 
#         return (value2)
#         
Startlist = [1,2,3,4]
print(Startlist)
# print("ile podanych cyfr jest na dobrym miejscu")
x = int(input())
# print(" ile podanych cyfr znajduje sie w kodzie , ale nie jest na dobrym mejscu "
y = int(input())

if x == 0 and y == 2:
    Startlist = [2,1,3,4]
    check(Startlist,0,1)
    
    if x == 0 : 
        Startlist = [2,1,4,3]
        check(Startlist,2,3)
        if x == 0 :
            Startlist = [2,4,1,3]
            print(Startlist)
            check(Startlist,1,2)
            if x == 0 : 
                Startlist = [3,4,1,2]
                print(K2_0K(Startlist,0,3))    
    
     
    
 
