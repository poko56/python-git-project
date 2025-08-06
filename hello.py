import config
import datetime # เพิ่มบรรทัดนี้

def say_hello(name):
   print(f"Hello, {name} from {config.APP_NAME}!")

def greet_user():
   name = input("Please enter your name: ")
   say_hello(name)

if __name__ == "__main__":
   greet_user()


def say_hello(name):
   now = datetime.datetime.now() # เพิ่มบรรทัดนี้
   print(f"Hello, {name} from {config.APP_NAME}!")
   print(f"Today is {now.strftime('%Y-%m-%d')}.") # เพิ่มบรรทัดนี้
   print(f"Hello again, {name} from {config.APP_NAME}!") # แก้ไขให้เป็นข้อความที่ถูกต้อง
   print(f"Today is {now.strftime('%Y-%m-%d')}.")
   print(f"Today is {now.strftime('%Y-%m-%d')}.")
