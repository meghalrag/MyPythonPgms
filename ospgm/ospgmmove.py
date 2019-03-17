import os
import shutil
# make sure that these directories exist
dir_src = "G:\\hello\\"
dir_dst = "G:\\hello1\\"
for file in os.listdir(dir_src):
    print file # testing
    src_file = os.path.join(dir_src, file)
    dst_file = os.path.join(dir_dst, file)
    shutil.move(src_file, dst_file)