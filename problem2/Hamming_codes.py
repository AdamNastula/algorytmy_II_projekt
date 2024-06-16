from math import log
"""kody hamminga dzialaja na blokach dlugosci poteg dwojki"""
#FRAME_SIZE = 256
FRAME_SIZE = 16
PARITY_BITS_QUANTITY = int(log(FRAME_SIZE, 2)) + 1
parity_bits_values = [2 ** i for i in range(PARITY_BITS_QUANTITY - 1)]

"""tutaj kodujemy pojedynczy blok nie wywolujemy samodzielnie"""
def encode_frame(data):
    parity_bits_values = [2 ** i for i in range(PARITY_BITS_QUANTITY - 1)]
    frame = [0 for i in range(FRAME_SIZE)]

    if (len(data) != FRAME_SIZE - PARITY_BITS_QUANTITY):
        return

    i = 3
    for bit in data:
        if (i in parity_bits_values):
            i += 1
        
        for parity_bit in parity_bits_values:
            if ((i & parity_bit) == parity_bit):
                if (int(bit) == 1):
                    frame[parity_bit] += 1

        frame[i] = int(bit)
        i += 1
    
    for parity_bit in parity_bits_values:
        if (frame[parity_bit] % 2 == 1):
            frame[parity_bit] = 1
        else:
            frame[parity_bit] = 0

    ones_quantity = 0
    for bit in frame:
        if (bit == 1):
            ones_quantity += 1
    
    if (ones_quantity % 2 == 0):
        frame[0] = 0
    else:
        frame[0] = 1
    
    return_frame = ""
    for bit in frame:
        if (bit == 1):
            return_frame += '1'
        else:
            return_frame += '0'

    return return_frame

"""zeby zakodowac cala wiadomosc trzeba ja podzielic na bloki wielkosci jak wyzej"""
def encode_message(message):
    encoded_message = ""
    data = ""

    for bit in message:
        data += bit

        if (len(data) == FRAME_SIZE - PARITY_BITS_QUANTITY):
            encoded_message += encode_frame(data)
            data = ""
    
    if (len(data) != 0):
        while (len(data) != FRAME_SIZE - PARITY_BITS_QUANTITY):
            data += '0'

        encoded_message += encode_frame(data)
    
    return encoded_message

"""tutaj sprawdzamy czy wystapil blad w ramce(jesli tak to naprawiamy), nie wywolujemy samodzielnie"""
def validate_frame(frame):
    validation = -1

    for i, bit in enumerate(frame):
        if (bit == '1'):
            if (validation == -1):
                validation = i
                continue
                
            validation = validation ^ i
    
    print(validation)
    if (validation != 0):
        new_frame = frame[0:validation]
        new_frame += '0' if frame[validation] == '1' else '1'
        new_frame += frame[validation + 1:]
        return new_frame
    
    return frame

"""sprawdzamy i naprawiamy bledy w calej zakodowanej wiadomosci"""
def validate_message(message):
    frame = ""
    validated_message = ""

    for bit in message:
        frame += bit

        if (len(frame) == FRAME_SIZE):
            validated_frame = validate_frame(frame)
            frame = ""
            validated_message += validated_frame
    
    return validated_message

"""odkodowuje originalna wiadomosc z postaci kodow hamminga"""
def decode_message(message):
    original_message = ""
    frames = []
    frame = ""

    for bit in message:
        frame += bit

        if (len(frame) == FRAME_SIZE):
            frames.append(frame)
            frame = ""
        
    for current_frame in frames:
        i = 3

        while (i < FRAME_SIZE):
            if (i in parity_bits_values):
                i += 1
                continue
            
            original_message += current_frame[i]
            i += 1

    return original_message  

if __name__ == "__main__":
    encoded_mes = encode_message('0010101110100101011')
    validated_message = validate_message(encoded_mes)
    decoded_message = decode_message(encoded_mes)
    print(decoded_message)
    print(validated_message)
    print(encoded_mes)