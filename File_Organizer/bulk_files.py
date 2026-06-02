import os
# we are gonna make files in a bulk
def bulk_files():
    folder=input("What is the name of the folder for bulk files..? ")   
    name=input("What is the name you want it to give..? ")
    extension=input("What is the extension you want it to be..? ").lstrip(".")
    amount=int(input("How many files do you want to make..? "))

    home=os.path.expanduser("~")
    folder_path=os.path.join(home,folder)
    os.makedirs(folder_path, exist_ok=True)

    for x in range(1,1+amount):
        file_name=f"{name}_{x}.{extension}"
        file_path=os.path.join(folder_path,file_name)
        with open(file_path,"w") as f:
            f.write(f"{file_name} has been created")

    print(f"{folder} with bulk files has been made 🌟")
