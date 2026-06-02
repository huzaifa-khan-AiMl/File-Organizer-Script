import os
# now we will make costumized files
def customized_files():
    folder=input("What is the name of the folder you want for customized files..? ")
    home=os.path.expanduser("~")
    folder_path=os.path.join(home,folder)
    os.makedirs(folder_path, exist_ok=True)
    number=int(input("What are the number of files do you want to make..? "))
    for x in range(1,number+1):
        file=input(f"What should be the file{x} be named.. ")
        extension=input(f"What is the extension do you want to give to file{x}..? ").lstrip(".")
        file_name=f'{file}.{extension}'
        file_path=os.path.join(folder_path,file_name)
        with open(file_path,"w") as f:
            f.write(f"your {file_name} has been created")
    print(f"== Congratulation you have made the {folder} with customized files 🌟 ==")
            