from jinja2 import Template
import sys
import json

template_file = sys.argv[1]
data_json_file = sys.argv[2]
out_html_file = sys.argv[3]


with open(template_file, 'r') as tf:
    template_html = tf.read()

with open(data_json_file, 'r') as djf:
    data = json.loads(djf.read())

html = Template(template_html)
res_html = html.render(data)

with open(out_html_file, 'w') as oht:
    oht.write(res_html)