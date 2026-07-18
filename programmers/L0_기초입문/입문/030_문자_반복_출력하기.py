# 문자 반복 출력하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 15:55:00

def solution(my_string, n):
    answer = ''
    for char in my_string:
        answer += char * n
    return answer
