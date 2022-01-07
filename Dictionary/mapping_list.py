# mapping lists into dicionary 

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

color = dict(zip(keys,values))

print(color)