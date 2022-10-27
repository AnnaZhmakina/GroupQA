def sort(array): 
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print(array)

def bin(array, element, left, right ):
    if left > right: 
        return True
    if element > array[-1] or element < array[0]:
        print('Число выходит за рамки последовательности')
        return False
    
    middle = (left + right) // 2 
    if array[middle] == element: 
        return middle  
        
    elif element < array[middle]: 
        
        return bin(array, element, left, middle - 1)
    else: 
        return bin(array, element, middle + 1, right)

def search(array, element):
       if bin(array, element, 0, len(array)):
           for i in range(len(array)):
               if array[i] < element <= array[i + 1]:
                   return array[i]
               elif array [i] == element and array [i-1] < element:
                   return array[i-1]
               else:
                   continue
           return 'Нет элемента, удовлетворяющего условиям'

numbers = input('Введите последовательность чисел через пробел\n')
element = int(input('Введите любое число\n'))

array = list(map(int, numbers.split()))
sort(array) 
                      
print(search(array, element))