from queue import Queue
from time import sleep

queue = Queue()
UUID = 0

# generate task and add it to queue
def generate_request(UUID):
    queue.put((UUID, f'TaskID: {UUID}'))

# process task from queue
def process_requests():
    if not queue.empty():
        task = queue.get()
        print(task)
        sleep(2)
    else:
        print('Черга пуста!')

if __name__ == "__main__":
    while True:
        process_requests()
        UUID += 1
        generate_request(UUID)
