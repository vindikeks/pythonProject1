import os
import time

copy_files = ["D:\distr\RVtools", "D:\PKI" ]
copy_path = "D:\BACK"
target = copy_path + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr {0} {1}".format(target, ' '.join(copy_files))
if os.system(zip_command) == 0:
    print("Htpthdyfz rjgbz ujnjdf", target)
else:
    print("Error")