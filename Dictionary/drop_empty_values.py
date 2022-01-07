d = {'c1': 'Red', 'c2': 'Green', 'c3': None}

# dictionary keys cannot be deleetd in while iterating, 
# dicionary items are converted into list so that keys cam be deleted
for key, value in list(d.items()):
    if value is None:
        del d[key]


print(list(d.items()))

print(d.items())


