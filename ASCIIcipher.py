i=0
cipher=''
a=input('')
if a=='암호화':
    original_text=input("문자를 입력하세요")
    number1=int(input("키숫자"))
    while(i < len(original_text)):
        ASCII_text=ord(original_text[i])
        cipher+=chr(ASCII_text+number)
        i+=1
    print(cipher)
elif a=='복호화':
    decording_text=input('문자를 입력하세요')
    number2=int(input("키숫자"))
    while(i < len(decording_text)):
        ASCII_text=ord(decording_text[i])
        cipher+=chr(ASCII_text-number2)
        i+=1
    print(cipher)
