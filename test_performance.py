import re
import time

FULL_PATTERN = re.compile(r"\w+")

start = time.time()
for i in range(1000000):
    FULL_PATTERN.fullmatch("hello")
end = time.time()
print("compiled version:", end - start)


start = time.time()
for i in range(1000000):
    re.fullmatch(r"\w+", "hello")
end = time.time()
print("Not compiled version:", end - start)
