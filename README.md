# Lab 4

## TCP Serialization Generator

This project demonstrates a simple protocol-driven TCP communication flow.
It uses a JSON interface definition, generates Python serialization/deserialization helpers with Jinja2, and applies them in a minimal client-server example.

## Project structure

- [interface.json](interface.json) - protocol schema definition
- [generator/generator.py](generator/generator.py) - entry point for the generator
- [generator/templates/protocol.j2](generator/templates/protocol.j2) - Jinja2 template for generated code
- [generated/protocol.py](generated/protocol.py) - generated protocol module
- [service_a/server.py](service_a/server.py) - TCP server implementation
- [service_b/client.py](service_b/client.py) - TCP client implementation
- [services.json](services.json) - service metadata description
- [requirements.txt](requirements.txt) - Python dependencies

## How it works

1. The protocol is defined in [interface.json](interface.json).
2. The generator reads that file and renders Python code from [generator/templates/protocol.j2](generator/templates/protocol.j2).
3. The generated module is written to [generated/protocol.py](generated/protocol.py).
4. The server listens for a TCP connection and deserializes incoming bytes.
5. The client serializes a message and sends it over the network.

## Requirements

Install the dependency:

```powershell
pip install -r requirements.txt
```

## Generate the protocol module

Run:

```powershell
python generator\generator.py
```

If your system uses `py` instead of `python`, use:

```powershell
py generator\generator.py
```

## Run the example

Start the server in one terminal:

```powershell
python service_a\server.py
```

In another terminal, run the client:

```powershell
python service_b\client.py
```

The server listens on `127.0.0.1:9000`.

## Example schema

The current interface includes a `Message` structure with nested metadata and a list field:

```json
{
  "structs": [
    {
      "name": "Message",
      "fields": [
        {"name": "id", "type": "int"},
        {"name": "text", "type": "string"},
        {"name": "tags", "type": "list", "element_type": "string"},
        {"name": "metadata", "type": "Metadata"}
      ]
    },
    {
      "name": "Metadata",
      "fields": [
        {"name": "count", "type": "int"},
        {"name": "label", "type": "string"}
      ]
    }
  ]
}
```

## Notes

- The generated module provides functions such as `serialize_message` and `deserialize_message`.
- The example supports primitive fields, lists, and nested structs.
- The service metadata is described in [services.json](services.json).