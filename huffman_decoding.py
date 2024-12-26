def huffman_decode():
    input_data = """
12 60
' ': 1011
'.': 1110
'D': 1000
'c': 000
'd': 001
'e': 1001
'i': 010
'm': 1100
'n': 1010
'o': 1111
's': 011
'u': 1101
100011110001001101000111111011001010011000010110011010111110
    """

    lines = input_data.strip().split('\n')

    _, _ = map(int, lines[0].split())

    huffman_codes = {}
    for line in lines[1:-1]:
        char, code = line.split(': ')
        huffman_codes[code] = eval(char)

    encoded_string = lines[-1]

    decoded_string = ""
    current_code = ""
    for bit in encoded_string:
        current_code += bit
        if current_code in huffman_codes:
            decoded_string += huffman_codes[current_code]
            current_code = ""

    print(decoded_string)

def main():
    huffman_decode()

if __name__ == "__main__":
    main()
