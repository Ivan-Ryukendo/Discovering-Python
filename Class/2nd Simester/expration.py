import re
text = "The rain in spain The rain in spain"
x = re.findall("in",text)
print(x)
print(x.count("in"))