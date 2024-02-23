import os.path
import shutil

CURRENT_FILE = os.path.abspath("test.zip")#__file__

CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)

if not os.path.exists("resource"):
    os.mkdir("resource")

TMP_DIR = os.path.join(CURRENT_DIR, "resource")
print(TMP_DIR)

#shutil.rmtree(os.path.join(CURRENT_DIR, "resource"))