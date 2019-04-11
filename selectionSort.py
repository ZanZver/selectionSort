import timeit
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        # find the index of the smallest remaining value
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        
        # swap the smallest value into place
        tmp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = tmp

lis = [4,1,7,5,2]
print(lis)
start_time = timeit.default_timer()
elapsed = timeit.default_timer() - start_time
selection_sort(lis)
print(elapsed)
print(lis)
