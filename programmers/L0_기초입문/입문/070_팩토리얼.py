# 팩토리얼
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 26. 08:14:36

import math
def solution(n):
    answer = 0
    for i in range(1, 12):
        if math.factorial(i) <= n:
            answer = i
        else:
            break
    return answer