for num in range(1, 101):
        flag = 1
        for i in range(2, num):
            if num % i == 0:
                flag = 0
                break 
        if flag == 1:
            print(num,"is prime")