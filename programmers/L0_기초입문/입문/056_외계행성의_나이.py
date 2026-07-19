# 외계행성의 나이
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120834
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 17:12:36

def solution(age):
    alphabet = "abcdefghij"
    return ''.join(alphabet[int(digit)] for digit in str(age))