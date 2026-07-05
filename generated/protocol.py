def serialize_message(obj):
    data = bytearray()

    
    
    data += obj["id"].to_bytes(4, 'big')
    
    
    
    encoded = obj["text"].encode()
    data += len(encoded).to_bytes(4, 'big')
    data += encoded
    
    

    return data

def deserialize_message(data):
    obj = {}
    offset = 0

    
    
    obj["id"] = int.from_bytes(data[offset:offset+4], 'big')
    offset += 4

    
    
    
    length = int.from_bytes(data[offset:offset+4], 'big')
    offset += 4
    obj["text"] = data[offset:offset+length].decode()
    offset += length
    
    

    return obj

