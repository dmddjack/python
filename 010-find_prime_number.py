print('prime number calculator')
while True:
    dummy = True
    prime = float(input('input a integer: '))
    root_prime = prime ** .5
    if prime != float(int(prime)) or prime < 1:
        print('[N/A]invalid input\n')
        root_prime = 1
        dummy = False
    elif prime == 1:
        print('[N]it is not a prime number\n')
        dummy = False
    for i in range(2,int(root_prime + 1)):
        if prime / i == prime // i:
            print('[N]it is not a prime number\n')
            dummy = False
            break
    if dummy:
        print('[Y]it is a prime number\n')