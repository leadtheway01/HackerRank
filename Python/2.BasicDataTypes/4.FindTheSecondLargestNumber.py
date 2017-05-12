#!/user/bin/env python3

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set(map(int, input().split()))))
    print(arr[-2])
    
    """ method 2
    arr = [*map(int, input().split()]
    arr.sort();
    t=list(set(arr))
    print(t[-2])
    """

    """ method 3
    #tmp is the largest number
    tmp = arr[n-1]
    for i in range(n-2, -1, -1):
        if tmp > arr[i]:
            print(arr[i])
            break;
    """
