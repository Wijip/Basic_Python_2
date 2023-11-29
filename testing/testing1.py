def terbesar (number):
    m = len(number)
    for i in number:
        for j in range(i+1,m):
             if number([i]>number[j]):
                temp = number[i]
                number[i] = number[j]
                number[j] = temp
def main():

    number = [50, 20, 30, 10, 40]
    terbesar(number)

if __name__ == '__main__':
    main()