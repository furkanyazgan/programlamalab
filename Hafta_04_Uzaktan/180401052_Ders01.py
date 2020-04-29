#Furkan Yazgan 180401052

def insertItemToHeap(my_heap,item):   # heap içine item ekler.
    my_heap.append(item)
    index = len(my_heap)-1
    if index <= 0:
        return
    parent = (index-1) // 2
    while parent >=0 and my_heap[parent] > my_heap[index]:
        my_heap[parent],my_heap[index] = my_heap[index],my_heap[parent]
        index = parent
        parent = (index-1)//2
def removeItemFrom(myheap_1): # Minumum itemi siler.
    index = len(myheap_1)
    if index<=0:
        print("Heap is NULL")
        return
    else:
        myheap_1_copy = myheap_1.copy()
        myheap_1_copy.pop(0)
        return heapsort(myheap_1_copy)

def heapsort(array): # Heap'i sıralar  geri return yapar yani  döndürür.
    array = array.copy()
    build_min_heap(array)
    sorted_array = []
    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array


def min_heapify(array,i): # liste'yi min heapify haline dönüştürür.
    left = 2 * i + 1
    right = 2 * i + 2
    length = len(array) - 1
    smallest = i
    if left <= length and array[i] > array[left]:
        smallest = left
    if right <= length and array[smallest] > array[right]:
        smallest = right
    if smallest != i:
        array[i], array[smallest] = array[smallest], array[i]
        min_heapify(array,smallest)

def build_min_heap(array): # item sayısını 2 ye böler ve  0'a kadar olanları min_heapify‘a gönderir.
    for i in reversed(range(len(array)//2)):
        min_heapify(array,i)


array_1 = [8,10,3,4,7,15,1,2,16]
array_2 = heapsort(array_1)
print(array_1,array_2)
