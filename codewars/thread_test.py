import threading as t

print("Hello check for current threat")

print("Current thread is ",t.current_thread().getName())
print(t.main_thread(),t.current_thread())
if (t.main_thread() == t.current_thread()):
    print("Current thread is main thread")
else:
    print("Current thread is not main thread")