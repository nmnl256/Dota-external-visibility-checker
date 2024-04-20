function get_address()
address = ReadPointer("libengine2.dylib + 0057B160")
address = ReadPointer(address + 0x0)
address = ReadPointer(address + 0xC8)
address = ReadPointer(address + 0x180)
address = ReadPointer(address + 0x0)
address = address + 0x1F0


return address
end

function change_offset()
correct_val = 1197957500880555496
address = ReadPointer("libclient.dylib + 04031A48")
address = ReadPointer(address + 0x8)
address = ReadPointer(address + 0x18)
address = ReadPointer(address + 0x338)
WriteQword(address+0x18, correct_val)

end
pointer_minimap = ReadPointer("libclient.dylib+ 043B4B50")
minimap_address = (pointer_minimap + 0xE0)


change_offset()

createThread(function()
  while true do
  a1ddress = get_address()

    value = ReadInteger(a1ddress)
    print(value)
    if (value == 14 or value == 30)
    then print("you are visible")

    writeFloat(minimap_address, "600.0")

    else
    writeFloat(minimap_address, "1200.0")
  end
      sleep(500)
end
end)
