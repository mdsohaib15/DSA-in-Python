class Queue:
          def __init__(self):
                    self.queue = []
          
          # add an element 
          def enqueue(self,item):
                    self.queue.append(item)
          
          # remove an element
          def dequeue(self):
                    if len(self.queue)<1:
                              return None
                    else:
                              return self.queue.pop(0)
          # display the queue
          def display(self):
                    print(self.queue)

          def size(self):
                    return len(self.queue)
          