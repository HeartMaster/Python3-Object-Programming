from threading import Thread

class InputReader(Thread):
    def run(self):
        self.line_of_text = input()

print("enter:")
thread = InputReader()
thread.start()

count = result = 1
while thread.is_alive():
    result = count * count
    count +=1

print(count,result)
print(thread.line_of_text)