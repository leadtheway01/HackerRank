#!/user/bin/env python3
if __name__ == '__main__':
    n = int(input())
    # [*map(func, item)] stores value as a list, integer_list
    integer_list = [*map(int, input().split())]
    # converts list to tuple
    t= tuple(integer_list)
    print(hash(t))

