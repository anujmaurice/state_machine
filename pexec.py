import Queue
import threading


class pexecute(threading.Thread):

    def __init__(self, in_queue, out):
        threading.Thread.__init__(self)
        self.in_queue = in_queue
        self.out = out

    def run(self):
        while True:
            process = self.in_queue.get()
            p, name, arg = process
            # print "^"*5,p,name,arg
            estatus = getattr(p, name).__call__(*arg)
            # change state by executing
            # return state
            if not estatus:
                print "ERROR"*3
            print process
            self.out.put(process)
            self.in_queue.task_done()


class prunner():

    def __init__(self, process_objects=[], pool=5):

        self.pool = 5
        self.process_objects = process_objects
        self.queue = Queue.Queue()
        self.out_queue = Queue.Queue()
        for i in range(self.pool):
            p = pexecute(self.queue, self.out_queue)
            p.setDaemon(True)
            p.start()
        for obj in process_objects:
            self.queue.put(obj)

    def join(self):

        self.queue.join()
