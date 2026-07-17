# 배열의 유사도
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 20:32:21

def solution(s1, s2):
    return len([x for x in s1 if x in s2])