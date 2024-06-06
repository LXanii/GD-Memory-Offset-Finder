import pyperclip

min_address = 0x140000000 # change this according to ghidras min add during analyze

while True:
    address = input("\nMemory Address: ")
    print("Offset Address:", hex(int(address, 16) - min_address), "(Added to Clipboard)")
    pyperclip.copy(hex(int(address, 16) - 0x140000000))