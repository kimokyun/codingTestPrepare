from collections import *
class Solution(object):
    def clothChoice(clothes):
        clothSort = defaultdict(int)
        
        for cloth in clothes:
            clothSort[cloth[1]] += 1

        answer = 1
        for kind in clothSort:
            answer *= (clothSort[kind] + 1)  # 입지 않는 경우도 포함

        return answer - 1  # 아무것도 안 입는 경우 제외

                
    clothChoice([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])