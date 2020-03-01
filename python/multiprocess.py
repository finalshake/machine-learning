from multiprocessing import Process, Queue
import os
import time

def count(str, queue):
    print('process name is %s, id is %s.' % (str, os.getpid()))
    print('about to count.')
    counter = 0
    while True:
        if queue.empty() == False:                      #must have this condition, or it will stuck in queue.get() when queue is empty.
            print('queue size is %d' %queue.qsize())
            value = queue.get()
            if value == 'show':
                print(counter)
            elif value == 'stop':
                break
        counter += 1
        print('count to %d' %counter)
        time.sleep(1)

def ask_for_input(queue):
    while True:
        print('please input something:')
        str = input()                                   #Note: using input() only in main process, unless leading to 'EOF when reading a line' error
        print('You just input %s' %str)
        queue.put(str)


if __name__ == '__main__':
    q = Queue(0)                                        #size paramater seems not working.
    p = Process(target=count, args=('count', q))
    p.start()
    ask_for_input(q)
