from collections import Counter
import heapq


def huffman_encode(s):
    freq = Counter(s)

    heap = [[freq, [symbol, ""]] for symbol, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = "0" + pair[1]
        for pair in hi[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[1]), p))
    codes = {symbol: code for symbol, code in huffman_codes}

    encoded_string = ''.join(codes[ch] for ch in s)

    print(len(codes), len(encoded_string))
    for symbol, code in codes.items():
        print(f"'{symbol}': {code}")
    print(encoded_string)

input_string = "Errare humanum est."
huffman_encode(input_string)
