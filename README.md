# Lab 4

## TCP Serialization Generator

This project demonstrates a simple code-generation workflow for binary TCP communication.
It reads a protocol definition from JSON, generates Python serialization/deserialization functions with Jinja2, and uses them in a minimal client-server example.

## Project structure

- [interface.json](interface.json) - protocol definition
- [generator/generator.py](generator/generator.py) - code generator entry point
- [generator/templates/serializer.j2](generator/templates/serializer.j2) - serializer template
- [generator/templates/deserializer.j2](generator/templates/deserializer.j2) - deserializer template
- [generated/protocol.py](generated/protocol.py) - generated protocol code
- [service_a/server.py](service_a/server.py) - TCP server
- [service_b/client.py](service_b/client.py) - TCP client
- [requirements.txt](requirements.txt) - Python dependencies

## How it works

1. The protocol is described in [interface.json](interface.json).
2. The generator reads that file and renders Python code using Jinja2 templates.
3. The generated code is saved to [generated/protocol.py](generated/protocol.py).
4. The server receives a binary message and deserializes it.
5. The client serializes a message and sends it over TCP.

## Requirements

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Generate the protocol code

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

## Example protocol

The current interface defines a single message structure:

```json
{
  "structs": [
    {
      "name": "Message",
      "fields": [
        {"name": "id", "type": "int"},
        {"name": "text", "type": "string"}
      ]
    }
  ]
}
```

## Notes

- The generated module contains functions such as `serialize_message` and `deserialize_message`.
- The example uses a very simple binary format with 4-byte integers and length-prefixed strings.