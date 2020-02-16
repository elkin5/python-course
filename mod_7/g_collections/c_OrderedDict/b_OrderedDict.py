from collections import OrderedDict

a = OrderedDict()
a["uno"] = 1
a["dos"] = 2

b = OrderedDict()
b["dos"] = 2
b["uno"] = 1

print(a == b)