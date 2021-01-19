'''
# bubble sort function
def actual_good_code_bubble(array):
    print(array) # print array before sorting
    
    # iterating through length of array
    for i in range(len(array)):
        # iterating through each pass
        for j in range(len(array)-1):
            # compare and swap if necessary, and print results
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(str(array) + "  " + str(array[j+1]) + " > " + str(array[j]) + ", swap occurred")
            else:
                print(str(array) + "  " + str(array[j]) + " < " + str(array[j+1]) + ", no swap occurred")
    return array        
  
actual_good_code_bubble([9, 7, 2, 6, 1])
'''

# shittiest code ever
def lab1_bubble(array):
    # keep count of comparisons
    comparisons = 0
    print("Inefficient bubble sort: ")
    print(array) # print array before sorting

    # loop runs continously till it is told to break, analogous to "Go to step 1" in the lab
    while True:
        # Initialize variables
        count = 0
        swap = False
        
        # Loop to iterate while count is less than 3
        while count <= 3:
            # compare if out of order
            if array[count] > array[count+1]:
                array[count], array[count+1] = array[count+1], array[count] # swap
                swap = True
                comparisons += 1 # keep count of comparisons
                
                # output what happened
                print(str(array) + "  " + str(array[count+1]) + " > " + str(array[count]) + ", swap       count = " + str(count) + "   swap = " + str(swap))
            else:
                comparisons += 1 # keep count of comparisons
                
                # output what happened
                print(str(array) + "  " + str(array[count]) + " < " + str(array[count+1]) + ", no swap    count = " + str(count) + "   swap = " + str(swap))
            
            # increment count
            count += 1
        
        # analogous to the "If swap is false, then stop, sorting is complete" step
        if swap == False:
            print("\n" + str(array) + " done! " + str(comparisons) + " comparisons were made")
            print("\n")
            break




# second shittiest code ever
def lab1_efficient_bubble(array):
    # keep count of comparisons
    comparisons = 0
    
    # maximum value for each pass (n, n-1, n-2, etc.)
    max_value = 3
    
    print("More efficient bubble sort: ")
    print(array) # print array before sorting

    # loop runs continously till it is told to break, analogous to "Go to step 1" in the lab
    while True:
        # Initialize variables
        count = 0
        swap = False
        
        # Loop to iterate while count is less than 3
        while count <= max_value:
            # compare if out of order
            if array[count] > array[count+1]:
                array[count], array[count+1] = array[count+1], array[count] # swap
                swap = True
                comparisons += 1 # keep count of comparisons
                
                # output what happened
                print(str(array) + "  " + str(array[count+1]) + " > " + str(array[count]) + ", swap       count = " + str(count) + "   swap = " + str(swap) + "   max_value = " + str(max_value))
            else:
                comparisons += 1 # keep count of comparisons
                
                # output what happened
                print(str(array) + "  " + str(array[count]) + " < " + str(array[count+1]) + ", no swap    count = " + str(count) + "   swap = " + str(swap) + "  max_value = " + str(max_value))
            
            # increment count
            count += 1
        
        # analogous to the "If swap is false, then stop, sorting is complete" step
        if swap == False:
            print("\n" + str(array) + " done! " + str(comparisons) + " comparisons were made")
            break
            
        # decrement max value    
        max_value -= 1


            
# calling the functions
lab1_bubble([9, 7, 2, 6, 1])
lab1_efficient_bubble([9, 7, 2, 6, 1])


