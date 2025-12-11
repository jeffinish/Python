phone = input("Digite seu telefone: ")
phone_conv = ""
digits_conv = {
    "1":"Um",
    "2":"Dois",
    "3":"Três",
    "4":"Quatro",
    "5":"Cinco",
    "6":"Seis",
    "7":"Sete",
    "8":"Oito",
    "9":"Nove",
    "0":"Zero"
}

for num in phone:
    phone_conv += digits_conv.get(num,"Confira o número") + " "

print(phone_conv)