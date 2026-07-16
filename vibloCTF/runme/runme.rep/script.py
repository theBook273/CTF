local_78 = []

for i in range(21):
    local_78.append(0)

local_78[0] = 217
local_78[1] = 254
local_78[2] = 197
local_78[3] = 244
local_78[4] = 158
local_78[5] = 199
local_78[6] = 0x9B
local_78[7] = 0xDC
local_78[8] = 0xE7
local_78[9] = 0xD2
local_78[10] = 0xF4
local_78[0xB] = 0x93
local_78[0xC] = 0xFE
local_78[0xD] = 0xFF
local_78[0xE] = 0xF4
local_78[0xF] = 0x9E
local_78[0x10] = 0xDE
local_78[0x11] = 0xF9
local_78[0x12] = 0xCE
local_78[0x13] = 0xE7
local_78[0x14] = 0xD2

for i in local_78:
    i = i ^ 171
    print(chr(i), end="")
print()
