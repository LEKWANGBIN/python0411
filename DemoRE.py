#DemoRE.py
import re

print(dir(re))

result = re.search("[0-9]*th","35th")
print(result)
print(reult.group())

result = re.mathch("[0-9]*th","35th")
print(result)
print(reult.group())