from excel_services import get_data_from_toloka
from config import Config


def toloka_to_txt(index=0):
    filename = f'{Config.RESULT_FILE_NAME}{str(index) if index != 0 else ""}.txt'
    try:
        with open(filename, 'x') as f:
            f.write(get_data_from_toloka())
    except FileExistsError:
        toloka_to_txt(index=index+1)


if __name__ == '__main__':
    toloka_to_txt()
