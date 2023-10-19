myData = {
    "effective top tube length": 515,
    "seat tube length": 500,
    "seat tube angle": 74.4,
    "head tube angle": 70.5,
    "stack": 513,
    "reach": 367,
    "standover height": 755
}

keys_list = []
values_list = []

for key in myData:
    print("key:", key, ", value:", myData[key])
    keys_list.append(key)
    values_list.append(myData[key])

print("  ALL KEYS:", keys_list)
print("  ALL VALUES:", values_list)