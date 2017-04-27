#coding=utf-8
# 实现队列
import threading
from logging import exception
mutex = threading.Lock()
class Queue():
    def __init__(self,size):
        self.size=size;
        self.front=-1;
        self.rear=-1;
        self.queue=[];
    def enqueue(self,ele):  #入队操作
        if mutex.acquire():
            if self.isfull():
                raise exception("queue is full");
            else:
                self.queue.append(ele);
                self.rear=self.rear+1;
            mutex.release()
    def dequeue(self):      #出队操作
        if mutex.acquire():
            if self.isempty():
                raise exception("queue is empty");
            else:
                self.front=self.front+1;
                return self.queue[self.front];
            mutex.release()

    def isfull(self):
        if mutex.acquire():
            return self.rear-self.front+1==self.size;
            mutex.release()
    def isempty(self):
        if mutex.acquire():
            return self.front==self.rear;
            mutex.release()

    def findMontion(self, montion):
        if mutex.acquire():
            for m in  self.queue:
                if montion == m.montionType:
                    return m;
            mutex.release()

    def remove(self, montionname):
        if mutex.acquire():
            for i in self.queue:
               if i.montionType == montionname:
                   self.queue.remove(i)
                   break
            mutex.release()