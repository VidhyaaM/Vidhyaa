import os
pathname= input("Enter the folder path: ")
file_ext = input("Input the File extension: ")
os.chdir(pathname)
print(os.getcwd())
print(os.listdir())

def write_file(file_path):
    with open("filenames."+file_ext,"a") as f:
        f.write(file_path)
  
for file in os.listdir():
    if file.endswith("."+file_ext):
        file_path = f"{pathname}\{file}"
        write_file(file_path)
    
    
