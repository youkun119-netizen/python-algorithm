# 옷가게 할인 받기
# 프로그래머스 L0 (기초·입문)
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 알고리즘: 기초
# 작성자: 학생
# 작성일: 2026. 07. 18. 20:44:06

def solution(price):
    discount_rates = {500000:0.8, 300000:0.9, 100000:0.95, 0:1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price*discount_rate)