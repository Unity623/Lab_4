# Lab_4

# TCP Serialization Generator

## Opis projektu

Projekt implementuje generator kodu serializacji i deserializacji danych na podstawie definicji zapisanej w JSON (`interface.json`). Na jego podstawie generowany jest kod Pythona, który umożliwia binarną komunikację między dwoma serwisami przez TCP/IP.

System składa się z:
- generatora kodu (Python + Jinja2)
- dwóch serwisów komunikujących się przez TCP:
  - ServiceA (serwer)
  - ServiceB (klient)

## Architektura

ServiceB wysyła wiadomość do ServiceA przez TCP/IP.

ServiceA odbiera dane binarne i deserializuje je do obiektu Pythona.

## Definicja protokołu

Definicja struktur danych znajduje się w pliku:

interface.json

Przykład:

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

## Generator kodu

Generator:
- czyta plik interface.json
- generuje funkcje serializacji i deserializacji
- wykorzystuje szablony Jinja2

Uruchomienie generatora:

python generator/generator.py

Wynik generacji:

generated/protocol.py

## Uruchomienie projektu

### Instalacja zależności

pip install jinja2

### Generowanie kodu

python generator/generator.py

### Uruchomienie serwera (ServiceA)

python service_a/server.py

Serwer działa na:
127.0.0.1:9000

### Uruchomienie klienta (ServiceB)

python service_b/client.py

## Przebieg komunikacji

1. ServiceA uruchamia serwer TCP i czeka na połączenie
2. ServiceB łączy się z ServiceA
3. ServiceB serializuje obiekt Message do formatu binarnego
4. Dane są wysyłane przez TCP/IP
5. ServiceA deserializuje dane i wypisuje wynik

## Technologie

- Python
- TCP/IP (socket)
- JSON (definicja protokołu)
- Jinja2 (generator kodu)
- serializacja binarna

## Cel projektu

Celem projektu jest pokazanie:
- generowania kodu na podstawie specyfikacji JSON
- implementacji prostego protokołu komunikacyjnego
- komunikacji między dwoma serwisami przez TCP/IP
- serializacji i deserializacji danych binarnych