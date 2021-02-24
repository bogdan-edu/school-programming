slovo=""
while slovo!="так":
    slovo=input("Купи слона (якщо погоджуєшся, то скажи так) ")
    if slovo=="":
        print("Не мовчи,будь ласка")
    else:
        print("Всі кажуть ", slovo, ",а ти купи слона") 
print("Дякую")
input()
