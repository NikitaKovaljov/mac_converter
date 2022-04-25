#!/usr/bin/python3

def convert_mac(mac_address):
    if len(mac_address) == 17:
        # throw ff:fe in the middle
        fffe = mac_address[:8] + ':ff:fe' + mac_address[8:]
        # invert the bit at index 6 and convert it back to hex
        fffe = hex(int(fffe[0:2], 16) ^ 2)[2:].zfill(2) + fffe[2:]
        # remove semicolons for right ipv6 format
        positions = [2, 8, 14, 20]
        temp = list(fffe)
        for i in positions:
            temp[i] = ''
            fffe = ''.join(temp)
        # append link-local prefix
        ipv6 = 'fe80::' + fffe
        print("\n[✓] Result: " + ipv6 + "\n")
    else:
        print("Incorrect mac address length")
        exit()

if __name__ == "__main__":
    mac_address = input("\n[!] Enter mac address: ")
    convert_mac(mac_address)
