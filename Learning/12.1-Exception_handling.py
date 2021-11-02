while(True):
    print("Press q to quit")
    a = input("enter a number: ")
    if a == 'q':
        break
    try:
        print("trying...")
        a = int(a)
        if a > 6:
            print("you entered a number greater than 6")
    except Exception as e:
        print(f"your input is invalid please enter a number {e}")

print("thanks for playing")
