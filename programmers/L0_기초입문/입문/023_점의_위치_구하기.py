# 점의 위치 구하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120841
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 17:48:28

def solution(dot):
    x, y = dot[0], dot[1]
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4