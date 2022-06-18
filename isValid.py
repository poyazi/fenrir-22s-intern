import re

def isValid(s: str) -> bool:
    n = len(s)//2   # 括弧の組数
    for _ in range(n):
        # 括弧を''に置換し、sに代入
        s = re.sub(r'\(\)|\{\}|\[\]', '', s)
    
    # s=''であればTrue
    return len(s)==0

s = '()'
print(isValid(s))  # True

s = '({)}'
print(isValid(s))  # False
