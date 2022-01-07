d = {'stu1': [50, 45, 39], 'stu2': [80, 85, 79]}

for name, marks_list in d.items():
    d[name] = sum(marks_list)/len(marks_list)


print(d)