if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    higgest = max(arr)    
    secondHiggest = min(arr)

    for items in arr:
        if (items > secondHiggest and items < higgest):
            secondHiggest = items

    print(secondHiggest)