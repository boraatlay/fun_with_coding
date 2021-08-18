#########################

# Prime numbers summation for a given range
# Author: Naim Bora Atlay
# 02.06.2021

#########################
import time

def isPrime(num):
    flag = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break
        return flag

def main():
    s = 0
    tic = time.perf_counter()
    for i in range(0,2000000):
        if isPrime(i) == False:
            s = s + i
    print(s)
    toc = time.perf_counter()
    print(f"Calculation completed in {toc - tic:0.4f} seconds.")

if __name__ == "__main__":
    main()
