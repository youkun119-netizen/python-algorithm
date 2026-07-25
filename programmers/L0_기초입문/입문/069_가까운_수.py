# 가까운 수
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120890
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 25. 13:08:34

def solution(array, n):
    array.sort()
    answer = min(array, key = lambda x : abs(x - n))
    return answer
    