from jinja2 import Template
 
template = Template('このサンプルコードは、 {{ title }}用です。')
result = template.render(title='Jinja2の動作確認')
 
print(result)