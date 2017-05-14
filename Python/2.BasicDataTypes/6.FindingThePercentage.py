#!/usr/bin/env python3
from decimal import Decimal

if __name__=='__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l = len(student_marks[query_name])
    total_score = sum(student_marks[query_name])
    avg = Decimal(total_score/l)
    print(round(avg, 2))
