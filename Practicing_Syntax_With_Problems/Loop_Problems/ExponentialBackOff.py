# Problem: Implement an exponential backoff strategy that 
# doubles the wait time between retries, starting from 1 second,
# but stops after 5 retries. 

import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print(f"attempts: {attempts} - wait time: {wait_time}")
    attempts += 1
    time.sleep(wait_time)
    wait_time *= 2
