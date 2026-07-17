# 최댓값 만들기(1)
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 16:58:29

def solution(numbers):
     numbers.sort()
     return numbers[-1]*numbers[-2]