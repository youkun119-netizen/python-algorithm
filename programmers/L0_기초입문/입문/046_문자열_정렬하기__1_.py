# 문자열 정렬하기 (1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120850
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 13:48:04

def solution(my_string):
    return sorted(int(i) for i in my_string if i.isdigit())