# [1,2,3,4,5,6]
def help(ciag) :
    x = int(input())
    y = int(input())
    print(ciag)
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
         return list 
     if( z == 2 and t==1):
         list[list1[1]]=5
         list[list1[0]]=6
            
     
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
    
    

Startlist = [1,2,3,4]


while (True): 
    help(Startlist)
    



# print(Startlist)

# print("ile podanych cyfr jest na dobrym miejscu")

x = int(input())

# print(" ile podanych cyfr znajduje sie w kodzie , ale nie jest na dobrym mejscu ")


y = int(input())
if x == 2 and y == 0 :
    K2_0K(Startlist ,  )

if x == 0 and y == 2:
    Startlist = [2,1,3,4]
    help(Startlist)
    if x == 0 : 
        Startlist = [2,1,4,3]
        print(Startlist)
        x = int(input())
        y = int(input())
        if x == 0 :
            Startlist = [2,4,1,3]
            print(Startlist)
            x = int(input())
            y = int(input())
            if x == 0 : 
                Startlist = [3,4,1,2]
                print()    
     
    
 
print(K2_0K([1,4,2,3] , 0 , 1))