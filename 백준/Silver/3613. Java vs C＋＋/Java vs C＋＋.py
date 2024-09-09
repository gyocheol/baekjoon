import re

s = input()

if re.match(r'^[a-z]+([a-zA-Z]*)*$', s):      # 첫번째 문자 소문자
    ans = re.sub(r'([A-Z])', r'_\1', s).lower()     # 대문자를 찾아서 앞에 _를 붙이고 소문자로 변경
    print(ans)
elif re.match(r'^[a-z]+(_[a-z]+)*$', s):       # 첫번째 문자 소문자, _ 연속 금지
    ans = re.sub(r'_([a-z])', lambda match:match.group(1).upper(), s)
    print(ans)
else:
    print("Error!")

