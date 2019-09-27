from random import *
import time

class Sort:
    def Bubble(self, array):
        for count1 in range(0, len(array)):
            for count2 in range(0, len(array) - 1):
                if array[count2] > array[count2 + 1]:
                    temp = array[count2]
                    array[count2] = array[count2 + 1]

                    array[count2 + 1] = temp

        return array

    def Test(self, array):
        count1 = 0
        done = False
        while not done:
            tempIndex = randint(0, len(array))
            if array[count1] > array[tempIndex]:
                temp = array[count1]
                array[count1] = array[tempIndex]
                array[tempIndex] = temp
                count1 = 0
            else:
                if count1 > len(array) - 2:
                    done = True

            count1 += 1

        return array
    
    def bubble_sort(self, arr):
        def swap(i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(arr)
        swapped = True
        
        x = -1
        while swapped:
            swapped = False
            x = x + 1
            for i in range(1, n-x):
                if arr[i - 1] > arr[i]:
                    swap(i - 1, i)
                    swapped = True
                        
        return arr

    def selection_sort(self, arr):        
        for i in range(len(arr)):
            minimum = i
            
            for j in range(i + 1, len(arr)):
                # Select the smallest value
                if arr[j] < arr[minimum]:
                    minimum = j

            # Place it at the front of the 
            # sorted end of the array
            arr[minimum], arr[i] = arr[i], arr[minimum]
                
        return arr

    def insertion_sort(self, arr):        
        for i in range(len(arr)):
            cursor = arr[i]
            pos = i
            
            while pos > 0 and arr[pos - 1] > cursor:
                # Swap the number down the list
                arr[pos] = arr[pos - 1]
                pos = pos - 1
            # Break and do the final swap
            arr[pos] = cursor

        return arr

    def merge_sort(self, arr):
        # The last array split
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        # Perform merge_sort recursively on both halves
        left, right = Sort().merge_sort(arr[:mid]), Sort().merge_sort(arr[mid:])

        # Merge each side together
        return Sort().merge(left, right, arr.copy())


    def merge(self, left, right, merged):

        left_cursor, right_cursor = 0, 0
        while left_cursor < len(left) and right_cursor < len(right):
        
            # Sort each one and place into the result
            if left[left_cursor] <= right[right_cursor]:
                merged[left_cursor+right_cursor]=left[left_cursor]
                left_cursor += 1
            else:
                merged[left_cursor + right_cursor] = right[right_cursor]
                right_cursor += 1
                
        for left_cursor in range(left_cursor, len(left)):
            merged[left_cursor + right_cursor] = left[left_cursor]
            
        for right_cursor in range(right_cursor, len(right)):
            merged[left_cursor + right_cursor] = right[right_cursor]

        return merged

    def partition(self, array, begin, end):
        pivot_idx = begin
        for i in range(begin+1, end+1):
            if array[i] <= array[begin]:
                pivot_idx += 1
                array[i], array[pivot_idx] = array[pivot_idx], array[i]
        array[pivot_idx], array[begin] = array[begin], array[pivot_idx]
        return pivot_idx

    def quick_sort_recursion(self, array, begin, end):
        if begin >= end:
            return
        pivot_idx = Sort().partition(array, begin, end)
        Sort().quick_sort_recursion(array, begin, pivot_idx-1)
        Sort().quick_sort_recursion(array, pivot_idx+1, end)
        return array

    def quick_sort(self, array, begin=0, end=None):
        if end is None:
            end = len(array) - 1        
        
        return Sort().quick_sort_recursion(array, begin, end)

if __name__ == "__main__":    
    num = []
    for i in range(0,100000):
        num.append(randint(0,300))
    # print(num)

    start = time.time()  # 시작 시간 저장
    sortNum = Sort().quick_sort(num)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    # print(sortNum)