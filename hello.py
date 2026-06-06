def greet(name):
    """跟用户打招呼"""
    return f"Hello {name}!"

def greet_users(users):
    """跟所有用户打招呼"""
    for user in users:
        print(greet(user))

if __name__ == "__main__":
    print("--- 欢迎使用 Git 练习项目 ---")
    greet_users(["Alice", "Bob", "Charlie"])
