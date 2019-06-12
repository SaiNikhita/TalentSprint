def check_if_two_arguments_are_true(first,second,third):
	if (first and second and not third) or (first and not second and third) or (not first and second and third):
		return True
	else:
	    return False
print(check_if_two_arguments_are_true(True,False,False))

def check_if_two_arguments_are_true(first,second,third):
	count=0
	if first:
	    count=count+1
	if second:
	    count=count+1
	if third:
	    count=count+1
	if count==2:
	    return True
	else:
	    return False
print(check_if_two_arguments_are_true(True,True,True))

def nearest_higher_palindrome(num,size):
    
    mid = int(size/2) 
    #setting the left and right iterators from middle
    if size%2==0:  # if the number is even
        left_half_iterator = mid-1
        right_half_iterator = mid
    else:  #if the number is odd
        left_half_iterator = mid - 1
        right_half_iterator = mid + 1
    
    #Finding the palindrome(same digits) in middle Ex: 11(2332)49
    while (left_half_iterator >= 0 and right_half_iterator<size and num[left_half_iterator] == num[right_half_iterator]) : 
        left_half_iterator-=1
        right_half_iterator+=1
    left_dissimilar=left_half_iterator
    right_dissimilar=right_half_iterator
    
    # if left dissimiler integer is greater than the right dissimilar integer Ex: 12(3)12
    if (num[left_dissimilar]>num[right_dissimilar]) : 
        # Copy left side to right side in reverse
        while (left_half_iterator >= 0) : 
            num[right_half_iterator] = num[left_half_iterator]  
            right_half_iterator+=1
            left_half_iterator-=1
            
    # if left dissimiler integer is less than the right dissimilar integer Ex: 12(3)45
    elif (num[left_dissimilar]<num[right_dissimilar]) :
        # increment the mid term(s) and propagate the carry outwards
        carry = 1
        left_half_iterator = mid - 1
        if (size%2 == 1) :  # Odd number
            num[mid] = str(int(num[mid]) + carry)  
            carry = int(int(num[mid]) / 10 ) 
            num[mid] = int(num[mid])%10
            right_half_iterator = mid + 1
          
        else:  #Even number
            right_half_iterator = mid  
            
        #Propagate carry outward
        while (left_half_iterator >= 0) : 
          
            num[left_half_iterator] += carry  
            carry = int(num[left_half_iterator] / 10)
            num[left_half_iterator] %= 10
            num[right_half_iterator] = num[left_half_iterator] 
            right_half_iterator+=1
            left_half_iterator-=1
    return num

number=input("Enter the integer")
num=[int(x) for x in number]
num=nearest_higher_palindrome(num,len(number))
for i in num: 
    print(i, end="")

def sum_of_unique_integers(array,size):
    array.sort() #sort the array
    sum = array[0] 
    for i in range(0,size-1): 
        if (array[i] != array[i+1]): # if adjacent integers are not same integer is unique
            sum = sum + array[i+1] 
    return sum

array=[1,3,2,5,3,2,4,1,6,3,6,8,7]
print(sum_of_unique_integers(array,len(array)))