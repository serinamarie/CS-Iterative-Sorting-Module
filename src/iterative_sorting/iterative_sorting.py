arr = [2,6,8,3,4,1,9,5,7]

def insertion_sort(arr):
    # for each unsorted element
    for i in range(1, len(arr)): 
        # store the reference to our cursor as a temporary ariable
        temp = arr[i]

        # create an element for the while loop to use
        j = i

        # while we're not at the beginning, compare to the value before it
        # while index of 3 is greater than 0 and while 3 is less than 8
        while j > 0 and temp < arr[j-1]:
            # swap
            #8 is now the current index
            arr[j] = arr[j-1]

            # decrement
            j-= 1
            # that keeps happening until we find the right place for the temp

        arr[j] = temp

    return arr

print("Arr:", arr)
# copying an array
sorted_arr = insertion_sort(arr[:])
print("Ins:", sorted_arr)

def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
 
        # set the current value to be the smallest, for now
        smallest_index = i

        # find minimum element 
        for j in range(i+1, len(arr)):

            # if the value is smaller than the smallest value
            if arr[smallest_index] > arr[j]:

                # set the current value to the new smallest
                smallest_index = j
        
        # swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr

print("Arr:", arr)
select_sort_arr = selection_sort(arr[:])
print("Sel:", select_sort_arr)

def bubble_sort(arr):

    # n = 9
    n = len(arr)

    # for # in range(8)
    for i in range(n-1):

        # first time through, for element in range(0,8)
        # second time through will be a range(0,7), etc.
        for j in range(0,n-i-1):

            # if value on left is greater than value on right
            if arr[j] > arr[j+1]:

                # swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

        



    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
