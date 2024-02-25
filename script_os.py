import os


CURRENT_DIR = os.getcwd()
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RESOURCE_DIR = os.path.join(CURRENT_DIR, 'resource')
ZIP_PATH = os.path.join(RESOURCE_DIR, 'test.zip')
print(CURRENT_DIR)
print(TMP_DIR)
print(RESOURCE_DIR)
print(ZIP_PATH)
