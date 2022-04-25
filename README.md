### mac_converter

## Theory

1. take the mac address: 52:74:f2:b1:a8:7f
2. throw ff:fe in the middle: 52:74:f2:ff:fe:b1:a8:7f
3. reformat to IPv6 notation 5274:f2ff:feb1:a87f
4. convert the first octet from hexadecimal to binary: 52 -> 01010010
5. invert the bit at index 6 (counting from 0): 01010010 -> 01010000
6. convert octet back to hexadecimal: 01010000 -> 50
7. replace first octet with newly calculated one: 5074:f2ff:feb1:a87f
8. prepend the link-local prefix: fe80::5074:f2ff:feb1:a87f
