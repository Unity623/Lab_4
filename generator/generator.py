import os
import json
from jinja2 import Environment, FileSystemLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# create output folder if not exists
os.makedirs(os.path.join(BASE_DIR, "..", "generated"), exist_ok=True)

with open(os.path.join(BASE_DIR, "..", "interface.json")) as f:
    spec = json.load(f)

env = Environment(loader=FileSystemLoader(os.path.join(BASE_DIR, "templates")))

serializer_tpl = env.get_template("serializer.j2")
deserializer_tpl = env.get_template("deserializer.j2")

output = ""

for struct in spec["structs"]:
    output += serializer_tpl.render(struct=struct)
    output += "\n\n"
    output += deserializer_tpl.render(struct=struct)
    output += "\n\n"

with open(os.path.join(BASE_DIR, "..", "generated", "protocol.py"), "w") as f:
    f.write(output)

print("Generated protocol.py")