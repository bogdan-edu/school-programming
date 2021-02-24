soldat = int(input("Скільки солдат в тебе? "))
if soldat <= 30:
    print("ти командир взводу")
elif soldat <= 100:
    print("ти командир роти")
else:
    print("ти командир батальйону")
