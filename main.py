import os 

folders = ["imgs","vids","audios","projectfiles","random"]

img = [".png",".jpg",".webp",".jpeg",".gif",".bmp",".tiff"]
vid = [".mp4",".mov",".mkv",".avi",".webm",".flv"]
audio = [".mp3",".wav",".acc",".m4a",".ogg",".aac",".flac"]
projectfile = [".aep",".prproj",".drp",".ai",".psd"]


# os.chdir("C:\Users\mishr\Documents\editing projects")

files = os.listdir()


while True:
    project_name = input("> ")
    if not os.path.exists(project_name):
        os.mkdir(project_name)
        break 
    else:
        print("You can't use this file name.")
        continue



for f in folders:
    folder_path = os.path.join(project_name,f)

    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print(f"{f} created")
    else:
        print(f"{f} already exists")




for file in files:
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)

        if ext.lower() in img:
            path = os.path.join(project_name,"imgs",file)
        elif ext.lower() in vid:
            path = os.path.join(project_name,"vids",file)
        elif ext.lower() in audio:
            path = os.path.join(project_name,"audios",file)
        elif ext.lower() in projectfile:
            path = os.path.join(project_name,"projectfiles",file)
        else:
            path = os.path.join("random",file)
        
        os.rename(file, path)