#empty list 
q=[]

#loop will run if true
choice ='Y'


while(ch=='Y' or ch=='y'):
    print("Enter 1 : Enqueue")
    print("Enter 2 : Dequeue")
    
    option = int(input('Enter ur choice:'))
    if option == 1: #Enququq
        d = int(input("Enter book no : "))
        q.append(d)
        
    elif option == 2: #Dequeue
        if (q==[]):
            print( "Queue empty")
        else:
            p = q.pop(0)
            print ("Deleted element: ", p)
            
    else:
        print('invalid choice')
choice = (input('want to continue?[Y/N]'))
