import zipfile, os
import pytest, shutil
from script_os import RESOURCE_DIR, TMP_DIR, ZIP_PATH


@pytest.fixture(scope='function',autouse=True)
def manage_way():
    # Создаем папку resource, если её нет
    if not os.path.exists(RESOURCE_DIR):
        os.mkdir(RESOURCE_DIR)

    with zipfile.ZipFile(ZIP_PATH, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
           # Копируем файлы из папки tmp в zip-архив
        for file_name in os.listdir(TMP_DIR):
            file_path = os.path.join(TMP_DIR, file_name)
            if os.path.isfile(file_path):
                zf.write(file_path, os.path.basename(file_path))


        # Проверяем содержимое архива
    with zipfile.ZipFile(ZIP_PATH, mode='r') as zf:
        for file_name in zf.namelist():
            print(file_name)


    yield

    # Удаляем папку resource и ее содержимое после завершения теста
    shutil.rmtree(RESOURCE_DIR, ignore_errors=True)

# Пример использования фикстуры в тесте
#def test_manage_way(manage_way):
    # В этом примере теста не требуется никакой специфической логики, так как фикстура сама создает и управляет архивом
 #   assert os.path.exists(ZIP_PATH)
  #  assert os.path.isfile(ZIP_PATH)
#if __name__ == "__main__":
#    manage_way()