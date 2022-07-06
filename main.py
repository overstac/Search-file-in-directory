from pathlib import Path
dir_root= Path("destination")
file_paths= dir_root.glob("**/*")

#noob
for path in file_paths:
  if path.is_file():
    if str(path).find("3") > 0:
      print(path.absolute())



#pro
search_term= "3"
for path in dir_root.rglob("*"):   #rglobe search even in subfolders
  if path.is_file():
    if search_term in path.stem:
      print(path.absolute())
