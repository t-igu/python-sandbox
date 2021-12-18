from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('./templates'))
template = env.get_template('e2.html')

print (template.render(message='hello'))
