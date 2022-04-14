#DemoRE.py
import re

print(dir(re))

result = re.search("[0-9]*th","  35th")
#찾은 결과가 매칭 오브젝트
print(result)
print(result.group())
#약간의 함정을 추가(정확하게 일치하는 것만)
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

#년도를 검색
years = re.search("\d{4}", "올해는 2022년")
print(years.group())
postcode = re.search("\d{5}", "우리동네는 52000")
print(postcode.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))
