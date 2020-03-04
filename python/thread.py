import threading, time

str = ''
counter = 0
lock = threading.Lock()

def do_count():
    global counter
    print('%s counting to %d' %(threading.current_thread().name, counter))
    counter += 1
    time.sleep(1)

def count():
    global counter
    global str
    switcher = False
    while True:
        if str == 'stop':
            switcher = False
        elif str == 'start':
            switcher = True

        if switcher:
            do_count()
        else:
            counter = 0
            continue
    
def ask_loop():
    global str
    while True:
        print('input something:')
        lock.acquire()
        str = input()
        lock.release()
        print('recived %s' %str)

if __name__ == '__main__':
    count_thread1 = threading.Thread(target=count, name='count_thread1', args=())
    count_thread2 = threading.Thread(target=count, name='count_thread2', args=())
    count_thread1.start()
    time.sleep(0.3)
    count_thread2.start()
    ask_loop()
