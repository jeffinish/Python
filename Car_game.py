command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("O carro já está ligado!")
        else:
            started = True
            print("O carro ligou...")
    elif command == "stop":
        if started:
            started = False
            print("O carro desligou...")
        else:
            print("O carro já está desligado")
    elif command == "help":
        print("""
        start - Para ligar o carro
        stop - para desligar o carro
        quit - para sair
        """)
    elif command == "quit":
        break
    else:
        print("Desculpe, não entendi")
