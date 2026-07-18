# 배열 두 배 만들기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120809
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 18:40:54

import numpy as np

def solution(numbers):
    answer = []
    answer = np.array(numbers)*2
    answer = answer.tolist()
    
    return answer