# 각도기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120829
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 17. 14:41:15

def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer