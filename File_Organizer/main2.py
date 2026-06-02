# Small addition to project which allows us to make files and folders in bulk instantly by running this
# program in there respective terminals

from folders import folders
from bulk_files import bulk_files
from customized_files import customized_files
def main():
    print("=== Welcome ===")
    print("Chose from these options to perform the task you want \n 1. Make Folders in Bulk \n 2. Make Files in Bulk \n 3. Make Customized files")
    function=int(input("What is the function do you want to perform? "))
    if function==1:
        folders()
    elif function==2:
        bulk_files()
    elif function==3:
        customized_files()
if __name__=="__main__":
    main()

