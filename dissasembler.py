def read_instuctions():
    pass

def translate_instruction(instruction):
    pass

def get_opcode(i):
    m = 0b1111111
    return m & i

def get_type(instruction):
    pass


def main():
    test_instruction = 0b0000000101011010000001001011011
    
    oc = get_opcode(test_instruction)
    print(oc)
    
    print(int(0b0110011))
    
main()