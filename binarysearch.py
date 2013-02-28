def binary_search(data, key):
    low = 0
    high = len(data) -1
    while(low <= high):
        mid = low + (high - low) / 2
        if(key < data[mid]):
            high = mid -1 # so we don't check the current mid again
        elif(key > data[mid]):
            low = mid + 1
        else:
            return mid
    return False

if __name__ == '__main__':
    data = [1, 2, 5, 6, 11, 15, 16, 19, 20, 22, 26, 31, 32, 35, 36, 38, 39, 
            45, 47, 52, 53, 58, 59, 60, 67, 69, 74, 76, 77, 79, 81, 82, 90, 
            94, 95, 97, 99, 143, 146, 153, 187, 196, 201, 210, 230, 301, 355]
    print binary_search(data, 90)
    print binary_search(data, 222)
