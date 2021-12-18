from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('./templates'))
template = env.get_template('e4.html')

data = [
    {"name":"taro", "age":30}, 
    {"name":"jiro", "age":16}, 
    {"name":"saburo", "age":10}
]

print (template.render(data=data))
