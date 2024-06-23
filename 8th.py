import time

def stopwatch():
    start_time = None
    while True:
        print("1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            start_time = time.time()
        elif choice == '2':
            if start_time:
                elapsed_time = time.time() - start_time
                print(f"Elapsed time: {elapsed_time} seconds")
        elif choice == '3':
            start_time = None
        elif choice == '4':
            break

stopwatch()
