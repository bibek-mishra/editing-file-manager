import os 

folders = ["imgs","vids","audios","sfx","projectfile","random"]

while True:
    project_name = input("> ")
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        break 
    else:
        print("You can't use this file name.")
        continue

for f in folders:
    path = os.path.join(project_name,f)

    if not os.path.exists(path):
        os.mkdir(path)
        print(f"{f} created")
    else:
        print(f"{f} already exists")