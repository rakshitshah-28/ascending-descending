
def Sort():
    #values = list()
    #while True:
    #    print("enter 0 to stop.")
    
    a = list(map(int, input().split()))
    #    if a == 0:
     #       break
    #values.append(a)
    a.sort()
    a.reverse()
    while True:        
        print("1.Ascending order")
        print("2.Descending order")
        print("3.BACK")
        print("select : 1/2/3")
        choice = int(input("Enter choice(1/2/3): "))
        if choice > 3:
            continue
        if choice == 1:
            print("Ascending order is ",a.sort)
        elif choice == 2:
            print("Descending order is ",a.reverse)
        elif choice == 3:
            print("Thank you for using List SORTER !!")
            break

    

    

