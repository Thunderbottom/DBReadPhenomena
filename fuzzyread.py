#!/usr/env/ python3

from threading import Thread
import time

totalBal = 2000


class d_readSub(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global totalBal, transactionVal
        time.sleep(2)
        totalBal = totalBal - transactionVal
        message = "%s After Transaction Total Balance: %d" % (
            self.getName(), totalBal)
        print(message, "\nTime of Transaction:", time.strftime('%X'))


class d_readAdd(Thread):

    def __init__(self):
        Thread.__init__(self)

    def run(self):
        global totalBal, transactionVal
        time.sleep(2)
        totalBal = totalBal + transactionVal
        message = "%s After Transaction Total Balance: %d" % (
            self.getName(), totalBal)
        print(message, "\nTime of Transaction:", time.strftime('%X'))


def main():
    global transactionVal
    transactionVal = input("Enter Transaction Value: ")
    if not transactionVal.isdigit():
        print("Input value is invalid, please try again")
        main()
    else:
        transactionVal = int(transactionVal)
        readAdd = d_readAdd()
        readAdd.setName('Add Transaction')
        readSub = d_readSub()
        readSub.setName('Subtract Transaction')
        readSub.start()
        readSub.join()
        print("Transaction commited")
        print("Current remaining Balance: %d" % (totalBal))
        readBal = totalBal
        print("New Transaction found, rolling back previous Transaction")
        readAdd.start()
        readAdd.join()
        print("Current remaining Balance: %d" % (totalBal))
        print("\nSimultaneous Read Balance: %d\nActual Balance: %d" %
              (readBal, totalBal))
        print("Total Transaction error found in data: %d" % (totalBal - readBal))

if __name__ == '__main__':
    main()
