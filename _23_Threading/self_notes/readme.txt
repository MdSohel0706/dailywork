Threads in python are an entity within a process that can be scheduled for execution.
In simpler words, a thread is a computation process that is to be performed by a computer.
It is a sequence of such instructions within a program that can be executed independently of other codes.

Process based multitasking : Several programs are executed at a time by the microprocessor.
Thread based multitasking : Several parts of the same program is executed at a time by the microprocessor.

Process : A process represents a group of statements which are executed by the PVM using a main thread.
Each process has its own memory, a program counter that keeps track of the instruction being executed
and a stack that hold the data. The data of one process is generally isolated from another process.
The data of one process is not generally available to another process unless both the process
communicate explicitly.

Thread : A thread also represents a group of statements within a program. When we want to use threads,
we have to create them separately which are in turn run by the main method. Threads donot have their own
memory and program counter. The data of one thread is shared easily by another thread. So it is possible that
one thread can easily modify the data of another thread. Threads are called lightweight processes.

Concurrent programming : Executing the tasks or parts of a program simultaneously is called concurrent programming.

GIL : Global Interpreter Lock allows only a single thread to execute at any given moment. GIL does not
allow more than one thread to run at a time.

Creating threads in python :
1. Creating a thread without using a class
2. Creating a thread by creating a sub class to Thread class
3. Creating a thread without creating sub class to Thread class

Thread class methods:
t.start() - start the thread.
t.join([timeout]) - wait until the thread terminates or a timeout occurs. timeout is a floating point number
specifying the timeout for the operation in seconds.
t.is_alive() - returns true if the thread is alive in memory or else false. A thread is alive from the moment
the start() method returns until the run() method terminates.
t.setName(name) - give name to thread
t.getName() - returns name of the thread
t.name - represents the thread name
t.setDaemon(flag) - make a thread a daemon thread if the flag is true
t.isDaemon() - returns true if the thread is a daemon thread, otherwise False
t.daemon - represents a property that takes either True or False to set the thread as daemon or not

Race condition : Situation that occurs when threads are not acting in expected sequence.

Thread synchronization : When a thread is already acting on an object, preventing any other thread from acting
on the same object is called "thread synchronization" or "thread safe". The object on which the threads are
synchronized are called "synchronized object" or "mutex(mutually exclusive lock)"
Thread synchronization are done by two techniques:
1. using locks
2. using semaphores
