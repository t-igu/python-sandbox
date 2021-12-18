from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('./templates'))

template = env.get_template('e3.html')

val = None
print ("\ntest1:********************\n",template.render(val=val))

val:int = 0
print ("\ntest2:********************\n",template.render(val=val))

val:int = 1
print ("\ntest3:********************\n",template.render(val=val))

val:int = 2
print ("\ntest4:********************\n",template.render(val=val))
