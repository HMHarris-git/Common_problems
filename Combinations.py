import time

def combinations(arr):
    n = len(arr)
    # Result array to store all combinations
    res=[]
    for i in range(1,2**n):
        '''
        A new string variable to store individual combination and 
        then reset for new iteration of outer loop
        '''
        data = ''
        for j in range(0,n):
            # This if statement will check if right most element in binary form of i is 1 or not
            if (i&1): 
                # if right-most is 1 the charcter will be added to data
                data+=arr[j]
            # Right-shift of i so that if statement can check for each element in binary form of i    
            i>>=1         
        res.append(data)
    return sorted(res)

def starter():
    print("xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox Choose your type of input xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxox")
    time.sleep(1)
    print("Enter 1 for Array")
    print("Enter 2 for String")
    print("Enter 0 for Exit.")
    time.sleep(1)
    choice = input("Enter here: ")
    if choice in ['0','1','2']:
        if choice == '1':
            arr = input("Enter your Array seperated by single space: \n").split()
            print(combinations(arr))
        elif choice == '2':
            arr = input("Enter your string here: \n")
            print(combinations(arr))
        elif choice == '0':
            return
    else:
        print("Invalid Input")
    
    starter()


if __name__ == "__main__":
    starter()