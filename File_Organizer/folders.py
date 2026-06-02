import os
def folders():
    # we will use this to make folders directly form the terminal
    num=int(input("What are the number of folders that you want to make..? "))
    for x in range(num):
        folder=input("Name of the folder that you want to make..? ")
        home = os.path.expanduser("~")
        location = os.path.join(home, folder)
        os.makedirs(location, exist_ok=True)
        print(f'{folder} has been made')