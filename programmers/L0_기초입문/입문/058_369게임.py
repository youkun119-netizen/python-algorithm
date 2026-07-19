# 369게임
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120891
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 19. 17:53:54

def solution(order): 
    order_str = str(order)
    answer = order_str.count("3") + order_str.count("6") + order_str.count("9")
    return answer