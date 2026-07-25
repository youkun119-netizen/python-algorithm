# 진료순서 정하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 25. 12:12:20

def solution(emergency):
    s = sorted(emergency, reverse = True)
    return [s.index(i) + 1 for i in emergency]