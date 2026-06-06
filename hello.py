def greet(name):
    """跟用户打招呼"""
    return f"Hey {name}!"

def welcome(name):
    """欢迎新用户"""
    print(f"Welcome {name}! 欢迎加入！")

def farewell(name):
    """跟用户道别"""
    return f"Goodbye {name}! See you next time!"

def greet_users(users):
    """跟所有用户打招呼"""
    for user in users:
        print(greet(user))

if __name__ == "__main__":
    print("--- 欢迎使用 Git 练习项目 ---")
    greet_users(["Alice", "Bob", "Charlie"])
    print("--- 新增 welcome 功能 ---")
    welcome("NewUser")

    print("--- 同事A 加了 farewell 功能 ---")
    print(farewell("Alice"))
