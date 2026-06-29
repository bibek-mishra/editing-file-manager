import os 

while True:
    project_name = input("> ")
    if os.path.exists(project_name):
        print("You can't use this file name.")
        continue
    else:
        os.mkdir(project_name)
        break 