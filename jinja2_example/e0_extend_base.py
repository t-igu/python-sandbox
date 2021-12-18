from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('./templates'))
template = env.get_template('e0.html')

print (template.render(title='my title', message='hello'))
