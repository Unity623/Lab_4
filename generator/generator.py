import json
from jinja2 import Environment, FileSystemLoader

# load json definition
with open("interface.json") as f:
    spec = json.load(f)

env = Environment(loader=FileSystemLoader("generator/templates"))

serializer_tpl = env.get_template("serializer.j2")
deserializer_tpl = env.get_template("deserializer.j2")

output = ""

for struct in spec["structs"]:
    output += serializer_tpl.render(struct=struct)
    output += "\n\n"
    output += deserializer_tpl.render(struct=struct)
    output += "\n\n"

with open("generated/protocol.py", "w") as f:
    f.write(output)

print("Generated protocol.py")