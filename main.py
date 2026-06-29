import os 

folders = ["imgs","vids","audios","projectfiles","random"]

img = [".png",".jpg",".webp",".jpeg",".gif",".bmp",".tiff"]
vid = [".mp4",".mov",".mkv",".avi",".webm",".flv"]
audio = [".mp3",".wav",".acc",".m4a",".ogg",".aac",".flac"]
projectfile = [".aep",".prproj",".drp",".ai",".psd",".prin"]


os.chdir("C:\\Users\\mishr\\Documents\\editing projects")
folder_names = os.listdir()

while True :
    name = input("Enter your folder name: ")

    if name not in folder_names:
        print("This project folder does not exist.")
        print("Create a folder and move all items to that folder to start sorting.")
        continue
    else:
        os.chdir(f"C:\\Users\\mishr\\Documents\\editing projects\\{name}")
        break


files = os.listdir()



if not os.path.exists("assets"):
    os.mkdir("assets")



for f in folders:
    folder_path = os.path.join("assets",f)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"{f} created")
    else:
        print(f"{f} already exists")




for file in files:
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)

        if ext.lower() in img:
            path = os.path.join("assets","imgs",file)
        elif ext.lower() in vid:
            path = os.path.join("assets","vids",file)
        elif ext.lower() in audio:
            path = os.path.join("assets","audios",file)
        elif ext.lower() in projectfile:
            path = os.path.join("assets","projectfiles",file)
        else:
            path = os.path.join("random",file)
        
        os.rename(file, path)