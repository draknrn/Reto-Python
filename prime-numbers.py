with open("results.txt", "w") as primos:
    for n in range(2, 251):
        primo = True

        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                primo = False
                break

        if primo:
            print(n)
            primos.write(str(n) + "\n")