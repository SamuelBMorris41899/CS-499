#solves 5.4 exercise 53b
#build function that checks for sets of elements/node that maps to itself
array = [[1,3], [2,1], [3,5], [4,4], [5,2]]

def permutation_cycle(inserted_array, cycled_array):
    x = inserted_array[0][0]
    y = inserted_array[0][1]
    inserted_array.pop(0)
    cycled_array.append(x)
    loop(inserted_array, cycled_array, y, [])

def loop (array, cycled_array, search_node, single_cycles_array):
    array_length = len(array)
    for i in range(array_length):
        if array[i][0] == search_node:

            cycled_array.append(array[i][0])
            search_node = array[i][1]
            array.pop(i)

            if len(array) == 0:

                break
            else:
                if array[0][0] == array[0][1]:
                    single_cycles_array.append(array[0])
                    array.pop(0)
            loop(array, cycled_array, search_node, single_cycles_array)
            print(cycled_array)
            print(single_cycles_array)
            break


if __name__ == '__main__':
    permutation_cycle(array, [])


