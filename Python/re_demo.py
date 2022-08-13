import re
test="aB12:cD/34\3"
print(test)
if re.match(r'\s+',test):
    print("ok")
test="1111s"
print(re.match(r'^\d+\d$',test))
test="     ss+42asd"
m=re.match(r'^([\s]*)([^-+0-9]*)([-,+]{0,1})(\d*)',test)
print(m.group(2))