import os

def folder(path="./New_Folder"):
    
    if not os.path.exists(path):
    
        print("Creating Folder...")
        os.makedirs(path)

    
# folder()
