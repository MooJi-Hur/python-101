from threading import Thread

class Animal(Thread):
    def __init__(self, name, message):
        Thread.__init__(self)
        self.name = name
        self.message = message

    def run(self):
        for i in range(3):
            print(f"{self.name}: {self.message} ({i})")

if __name__ == '__main__':
    first_thread = Animal("first_dog", "멍멍")
    second_thread = Animal("second_dog", "왈왈")
    third_thread = Animal("first_cat", "야옹")
    fourth_thread = Animal("second_cat", "애옹")

    first_thread.start()    # run 호출
    second_thread.start()
    third_thread.start()
    fourth_thread.start()


    print("End")