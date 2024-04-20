#offsets(0x....) are outdated

import pymem, time

#Change the size of icons in the game depending on the VBE indicator
def main():
    while True:
        a1ddress = get_address()
        value = handle.read_int(a1ddress)
        if (value == 14 or value == 30):

            handle.write_float(minimap_address, 600.0)

        else:
            handle.write_float(minimap_address, 1200.0)
        time.sleep(0.5)

def get_address():
    address = handle.read_longlong(engine + 0x0058B620)
    address = handle.read_longlong(address + 0x0)
    address = handle.read_longlong(address + 0xC8)
    address = handle.read_longlong(address + 0x180)
    address = handle.read_longlong(address + 0x0)
    address = address + 0x1F0
    return address


# valve mash the VBE netvar with an random int. A table (Netvar:Offset) exists in the process memory. Let's change VBE Offset with another offset. 
def change_offset(): 
    correct_val = 1197957500880555040
    address = handle.read_longlong("client.dll + 04555308")
    address = handle.read_longlong(address + 0x18)
    address = handle.read_longlong(address + 0x20)
    address = handle.read_longlong(address + 0x18)
    address = handle.read_longlong(address + 0x338)
    handle.write_longlong(address + 0x18, correct_val)


handle = pymem.Pymem("dota2.exe") # getting handle
client = pymem.process.module_from_name(handle.process_handle, "client.dll").lpBaseOfDll #getting client.dll 
engine = pymem.process.module_from_name(handle.process_handle, "engine2.dll").lpBaseOfDll #getting engine2.dll

miniMap = handle.read_longlong(client+ 0x0465F508)
minimap_address = miniMap+0x40

main()

#offsets(0x....) are outdated
