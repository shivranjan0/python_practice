import os

def delete_file(project):
    if not os.path.exists(project):
        print("The file does not exist")
        return
    
    print("The file exists")


    for root, dirs, files in os.walk(project):
        print(f"root: {root}")

        if dirs:
            print("Subdirectories:")
            for d in dirs:
                print(f"\t{d}") 

        if files:
            print("files")
            for f in files:
                print(f"\t{f}")       
    print("")



directory_to_create = "/path/to/your/project" 
def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory {path} created")
    else:
        print(f"Directory {path} already exists")

create_directory(directory_to_create)


    
