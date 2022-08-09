#create a function that finds the largest number in a list.

def largestnumber(x):
    #the highest number is set to be 0

    highest_number=0

    for n in x:

        if n > highest_number:
            highest_number = n
    
    return highest_number

number = [1,2,3,4,5,6,7,8,76,444,3,5,75,5,6,66]

answer = largestnumber(number)
print("The largest number in the list is: ",answer)


