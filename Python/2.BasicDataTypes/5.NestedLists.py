#!/user/bin/env python3


if __name__ == '__main__':
    """
    my solution
    # store student names and their score in the list
    students = [[input(), float(input())] for _ in range(int(input()))]
    #find the second lowest score
    second_lowest = sorted(list(set([students[i][1] for i in range(len(students))])))[1]
    # print second lowest grade students
    l = []
    for i in range(len(students)):
        if students[i][1] == second_lowest:
            l.append(students[i][0])

    for i in range(len(l)):
        a = sorted(l)
        print(a[i])
    """
    #shorter solution
    # store student names and their scores in the list
    a = [[input(), float(input())] for _ in range(int(input()))]
    # get the second lowest grade
    s = sorted(set(x[1] for x in a))
    for name in sorted(x[0] for x in a if x[1] == s[1]):
        print(name)
