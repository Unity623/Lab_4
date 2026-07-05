import json
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

BASE_DIR = Path(__file__).resolve().parent
INTERFACE_PATH = BASE_DIR.parent / "interface.json"
OUTPUT_PATH = BASE_DIR.parent / "generated" / "protocol.py"
TEMPLATE_DIR = BASE_DIR / "templates"


def generate_protocol_code(spec):
    structs = spec.get("structs", [])
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR), autoescape=False)
    template = env.get_template("protocol.j2")
    return template.render(structs=structs)


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with INTERFACE_PATH.open(encoding="utf-8") as f:
        spec = json.load(f)

    output = generate_protocol_code(spec)
    OUTPUT_PATH.write_text(output, encoding="utf-8")
    print(f"Generated {OUTPUT_PATH.name}")


if __name__ == "__main__":
    main()