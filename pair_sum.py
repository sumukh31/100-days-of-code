# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17

def pair_sum(arr,k):

    #Edge-case:
    if len(arr) < 2:
        return

    # create set data structures since element insertion in set is O(1)  
    seen = set()
    output = set()

    # iterate through the array once
    # if the target is not in the "seen" set, add number to the "seen" set.
    # if not, the number & target sum up to "k" value - add it to the output as a tuple
    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            return True
            # IF problem had asked to return pairs:
            # Add pairs to the output set
            # output.add((min(num,target), max(num,target)))
    
    #if problem asked to print the pairs/length of the number of pairs.
    #print ("output", output)
    #return len(output)
    
    return False

# Test
print (pair_sum([1,3,2,2],4))
