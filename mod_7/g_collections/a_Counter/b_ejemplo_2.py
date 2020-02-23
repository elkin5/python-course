from collections import Counter

lenguajes_usuarios = ['Python', 'C++', 'Java', 'Python', 'C#', 'Ruby', 'Python', 'C++', 'JS', 'Java', 'Go']

count = Counter(lenguajes_usuarios)

print(count.most_common(1))
print(count.most_common())

#for k,v in count.items():