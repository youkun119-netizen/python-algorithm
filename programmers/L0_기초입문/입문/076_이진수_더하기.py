# 이진수 더하기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120885
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 08. 08. 19:11:27

def solution(bin1, bin2):
    answer = int(bin1, 2) + int(bin2, 2)
    return bin(answer)[2:]