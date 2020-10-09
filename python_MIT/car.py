command = ""
started = False

while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("car already started")
        else:
            print("car started")
            started = True
    elif command == "stop":
        if not started:
            print("car already stopped")
        else:
            print("car stopped")
            started = False
    elif command == "help":
        print("""
    start - to start the car
    stop  - to stop the car
    help  - to get help
    exit  - to exit
        """)
    elif command == "exit":
        print("bye bye")
        break
    else:
        print("sorry i dont understand")