import struct

scene = b''
ip = 0  # instruction pointer
dispatch_table = {}


def op_a7():
    global ip
    print(f"OPA7 {bytes(scene[ip:ip + 2]).hex()}")
    ip += 2
dispatch_table[0xa7] = op_a7


def dism_op():
    global ip
    op = scene[ip]
    if op < 0x3f:
        print(f"BIN {bytes(scene[ip:ip + 2]).hex()}")
        ip += 2
        while scene[ip] != 0x40:
            op = scene[ip]
            if op < 0x40:
                print(f"BIN {bytes(scene[ip:ip + 2]).hex()}")
                ip += 2
                raise Exception('todo')
            else:
                if op == 0x65:
                    raise Exception('todo')
                else:
                    if op < 0x60 or op >= 0xaf:
                        raise Exception('todo dispatch table 2')
                    else:
                        dism_op()
        if scene[ip] == 0x40:
            print("OP40")
            ip += 1
    elif op < 0x60 or op >= 0xaf:
        pass
    else:
        ip += 1
        if op not in dispatch_table:
            raise Exception(f"OP {op:02X} not implemented yet")
        else:
            dispatch_table[op]()


def dism():
    global ip
    print(f"LAB_{ip:04X}:")
    print(f"FIRST_BYTE {scene[ip]}")
    ip += 1
    while True:
        op = scene[ip]
        dism_op()
        if op == 0x63:
            print("OP63")
            break


with open('SCENE_00.COM', 'rb') as f:
    scene = f.read()

# read start offsets table
start_offsets = struct.unpack('4H', scene[:4*2])
for offset in start_offsets:
    print(f"OFFSET LAB_{offset:04X}")

ip = start_offsets[0]
dism()


