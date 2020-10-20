import time
import sys

if __name__ == '__main__':
    # sys.stdout.write('[' + ' ' * 10 + ']')
    # # moved *11 on account of ]
    # sys.stdout.write('\b' * 10)
    # sys.stdout.flush()
    # for i in range(10):
    #     time.sleep(1)
    #     sys.stdout.write('.')
    #     sys.stdout.flush()
    # sys.stdout.write('] Done!\n')


    # sys.stdout.write('[' + ' ' * 10 + ']')
    # sys.stdout.write('\b' * 10)
    # sys.stdout.flush()
    # for i in range(10):
    #     time.sleep(1)
    #     sys.stdout.write('\b' + '=')
    #     if (i < 9):
    #         sys.stdout.write('>')
    #     sys.stdout.flush()
    # sys.stdout.write('] Done!\n')

    # sys.stdout.write('[' + ' ' * 10 + ']  0%')
    # sys.stdout.flush()
    # for i in range(10):
    #     time.sleep(1)
    #     sys.stdout.write('\b' * (15 - i) + '>')
    #     if (i < 9):
    #         sys.stdout.write('>')
    #     sys.stdout.write(' ' * (8 - i) + '] ' + str(i + 1) + '0%')
    #     sys.stdout.flush()
    # # overwrite the percentage sign and write Done instead
    # sys.stdout.write('\b\b\b\bDone!\n')