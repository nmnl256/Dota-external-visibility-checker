import pymem
import time
#offsets are outdated
class Dota2Modifier:
    def __init__(self):
        self.handle = pymem.Pymem("dota2.exe")
        self.client = self.load_module_base("client.dll")
        self.engine = self.load_module_base("engine2.dll")
        self.minimap_address = self.setup_minimap_address()

    def load_module_base(self, module_name):
        """Retrieve the base address of a module."""
        module = pymem.process.module_from_name(self.handle.process_handle, module_name)
        return module.lpBaseOfDll

    def setup_minimap_address(self):
        """Calculate the memory address for the minimap."""
        minimap_base = self.handle.read_longlong(self.client + 0x0465F508)
        return minimap_base + 0x40

    def get_dynamic_address(self):
        """Retrieve the dynamically changing game address."""
        address = self.handle.read_longlong(self.engine + 0x0058B620)
        offset_chain = [0x0, 0xC8, 0x180, 0x0, 0x1F0]
        for offset in offset_chain:
            address = self.handle.read_longlong(address + offset)
        return address

    def update_icon_size(self):
        """Update the size of icons on the minimap based on the game's current state."""
        while True:
            address = self.get_dynamic_address()
            value = self.handle.read_int(address)
            if value in (14, 30):
                self.handle.write_float(self.minimap_address, 600.0)
            else:
                self.handle.write_float(self.minimap_address, 1200.0)
            time.sleep(0.5)

    def change_vbe_offset(self):
        """Update the VBE netvar offset to the correct value in memory."""
        correct_val = 1197957500880555040
        address = self.handle.read_longlong(f"{self.client} + 04555308")
        offset_chain = [0x18, 0x20, 0x18, 0x338, 0x18]
        for offset in offset_chain[:-1]:
            address = self.handle.read_longlong(address + offset)
        self.handle.write_longlong(address + offset_chain[-1], correct_val)


if __name__ == "__main__":
    game_modifier = Dota2Modifier()
    game_modifier.update_icon_size()
#offsets are outdated
