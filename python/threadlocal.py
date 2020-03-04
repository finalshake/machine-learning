import threading, time

local = threading.local()
str = ''

def process_thread(counter, start_str, stop_str):
    local.counter = counter
    local.start_str = start_str
    local.stop_str = stop_str
    count()

def do_count():
    print('%s counting to %d' %(threading.current_thread().name, local.counter))
    local.counter += 1
    time.sleep(1)

def count():
    global str
    switcher = False
    while True:
        if str == local.stop_str:
            switcher = False
        elif str == local.start_str:
            switcher = True

        if switcher:
            do_count()
        else:
            continue
    
def ask_loop():
    global str
    while True:
        print('input something:')
        str = input()
        print('recived %s' %str)

if __name__ == '__main__':
    count_thread1 = threading.Thread(target=process_thread, name='count_thread1', args=(0,'start1','stop1'))
    count_thread2 = threading.Thread(target=process_thread, name='count_thread2', args=(100,'start2','stop2'))
    count_thread1.start()
    time.sleep(0.3)
    count_thread2.start()
    ask_loop()
