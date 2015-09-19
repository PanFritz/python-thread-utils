#thread-utils

Thread-utils adds `@synchronized` and `@asynchronized` decorators.

#Example:

```python
import threading
import time
from thread-utils import synchronized as sync
from thread-utils import asynchronized as async

my_print_lock = threading.Lock() #Lock to use in our sync function

@sync(lock = my_print_lock) #It requires you to pass a lock for it to use.
def my_print(*args):
    print " ".join(args)

@async(daemon=True) #Set daemon to true, so the thread dies when the main thread does.
def my_print_spam():
    while True:
        my_print(str(time.time()))

for x in range(50): #Calls my_print_spam 50 times, since its @async it always create its own thread.
    my_print_spam()

try:
    while True: #Here to keep the main thread going until you kill it with ctrl+c
        pass
except KeyboardInterrupt:
    quit()
```