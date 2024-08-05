from pathlib import Path


# path=Path('ecommerce1')
# print(path.exists())
# path.mkdir()
# path.rmdir()


path=Path();
path.glob('*') # get all the dir and files (not the file inside the dir)
path.glob('*.*') # get only files in current dir
path.glob('*.py') # to get all python files in current dir

for file in path.glob('*.*'):
  print(file)