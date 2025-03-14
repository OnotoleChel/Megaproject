import os
import random

def create_virus_files(directory, count):
    """
    Создает указанное количество файлов с именами Virus1.py, Virus2.py, ..., VirusN.py в заданной директории.
    Каждый файл содержит код, который выводит случайную фразу из списка и завершается вызовом input().
    
    :param directory: Путь к папке, где будут созданы файлы.
    :param count: Количество файлов для создания.
    """    
    # Проверяем, существует ли указанная директория
    if not os.path.exists(directory):
        print(f"Директория не существует: {directory}")
        return
    
    # Создаем файлы
    for i in range(1, count + 1):
        file_name = f"Virus{i}.py"
        file_path = os.path.join(directory, file_name)
        
        try:
            # Формируем содержимое файла
            file_content = f'''# Этот файл был создан автоматически
import random

# Список фраз для вывода
phrases = [
    "Форматирование диска С началось",
    "Переводим ваши деньги Анатолию",
    "Заменяем фон рабочего стола на фото Билли Харрингтона",
    "Меняем имя пользователя на Гачамучо",
    "Включаем платную подписку на все видео с ЧОрным властилином",
    "Записываем пользователя на курсы удушения питона",
    "Автоматически проставляю лайки всем книжкам Анатолия",
    "Делаю запись с вашей камеры",
    "Репилоиды смотрят на тебя со спины",
    "Истина где то рядом"
]
# Выбираем случайную фразу
random_phrase = random.choice(phrases)

# Выводим случайную фразу
print(random_phrase)

# Ждём подтверждения от пользователя
input("Нажмите Ентер или закройте это окно чтоб подтвердить...")
'''
            # Создаем файл и записываем содержимое
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(file_content)
            print(f"Файл создан: {file_path}")
        except Exception as e:
            print(f"Ошибка при создании файла {file_path}: {e}")

if __name__ == "__main__":
    # Определяем путь к папке, где находится скрипт
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Количество файлов для создания
    number_of_files = 10
    
    # Вызываем функцию для создания файлов в папке скрипта
    create_virus_files(script_directory, number_of_files)