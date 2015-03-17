# This python code moves a text files with prefix 'a' and 'r' and moves it to two different director.


import os
import shutil

srcDir ='path/intital_directory'
targetDir = 'path/destination_derictory'
for fname in os.listdir(srcDir):
    if not os.path.isdir(os.path.join(srcDir, fname)):
        # 'a' is prefix.
        for prefix in ['a']:
            if fname.startswith(prefix):
                if not os.path.isdir(os.path.join(targetDir, prefix)):
                    os.mkdir(os.path.join(targetDir, prefix))
                shutil.move(os.path.join(srcDir, fname), targetDir)


test = 'path/destination_derictory/a'
shutil.rmtree(test)



srcDir = 'path/intital_directory'
targetDir = 'path/destination_derictory'
for fname in os.listdir(srcDir):
    if not os.path.isdir(os.path.join(srcDir, fname)):
       # 'r' is prefix
        for prefix in ['r']:
            if fname.startswith(prefix):
                if not os.path.isdir(os.path.join(targetDir, prefix)):
                    os.mkdir(os.path.join(targetDir, prefix))
                shutil.move(os.path.join(srcDir, fname), targetDir)


test = 'path/destination_derictory/r'
shutil.rmtree(test)
