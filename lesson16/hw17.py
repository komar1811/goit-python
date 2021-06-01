import os
import sys
from pathlib import Path
import shutil
from threading import Thread


def normalize(text):
    map = {ord('а'): 'a', ord('б'): 'b', ord('в'): 'v', ord('г'): 'g', ord('д'): 'd', ord('е'): 'e', ord('ё'): 'e',
           ord('ж'): 'zh', ord('з'): 'z', ord('и'): 'i', ord('й'): 'i', ord('к'): 'k', ord('л'): 'l', ord('м'): 'm',
           ord('н'): 'n',
           ord('о'): 'o', ord('п'): 'p', ord('р'): 'fr', ord('с'): 's', ord('т'): 't', ord('у'): 'u', ord('ф'): 'f',
           ord('х'): 'h',
           ord('ц'): 'c', ord('ч'): 'ch', ord('ш'): 'sh', ord('щ'): 'shch', ord('ъ'): '', ord('ы'): 'y', ord('ь'): '',
           ord('э'): 'e',
           ord('ю'): 'u', ord('я'): 'ia', ord('А'): 'A', ord('Б'): 'B', ord('В'): 'V', ord('Г'): 'G', ord('Д'): 'D',
           ord('Е'): 'E', ord('Ё'): 'E',
           ord('Ж'): 'Zh', ord('З'): 'Z', ord('И'): 'I', ord('Й'): 'I', ord('К'): 'K', ord('Л'): 'L', ord('М'): 'M',
           ord('Н'): 'N',
           ord('О'): 'O', ord('П'): 'P', ord('Р'): 'R', ord('С'): 'S', ord('Т'): 'T', ord('У'): 'U', ord('Ф'): 'F',
           ord('Х'): 'H',
           ord('Ц'): 'C', ord('Ч'): 'Ch', ord('Ш'): 'Sh', ord('Щ'): 'Shch', ord('Ъ'): '', ord('Ы'): 'y', ord('Ь'): '',
           ord('Э'): 'E',
           ord('Ю'): 'U', ord('Я'): 'Ya', ord('ґ'): 'g', ord('Ґ'): 'G', ord('Є'): 'E', ord('.'): '_', ord('/'): '_',
           ord(' '): '_',
           ord(','): '_', ord('"'): '_', ord('\''): '_', ord('-'): '_', ord('='): '_', ord('+'): '_', ord('!'): '_',
           ord('@'): '_',
           ord('#'): '_', ord('$'): '_', ord('%'): '_', ord('^'): '_', ord('&'): '_', ord('*'): '_', ord('('): '_',
           ord(')'): '_'}
    translated = text.translate(map)
    return translated



def sort_files(path):
    picture_extension = ['jpeg', 'png', 'jpg', 'psd']
    documents_extension = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
    video_extension = ['avi', 'mp4', 'mov']
    music_extension = ['mp3', 'ogg', 'wav', 'amr']
    archive_extension = ['zip', 'gz', 'tar']
    files = os.listdir(path)
    if files:
        os.makedirs(f'{path}\images')
        os.makedirs(f'{path}\documents')
        os.makedirs(f'{path}\\video')
        os.makedirs(f'{path}\music')
        os.makedirs(f'{path}\\archives')
        for element in files:
            new_element = element.split('.')
            new_element_str = '.'.join(new_element[0:-1])
            if new_element[-1].lower() in picture_extension:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\images\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in documents_extension:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\documents\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in video_extension:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\\video\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in music_extension:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.copyfile(f'{path}\{element}', f'{path}\music\{normalize(new_element_str)}.{new_element[-1]}')
            if new_element[-1].lower() in archive_extension:
                if os.path.isfile(f'{path}\{element}'):
                    shutil.unpack_archive(f'{path}\{element}', f'{path}\\archives\{normalize(new_element_str)}')
    files = os.listdir(path)
    for element in files:
        if os.path.isdir(path + f'\{element}') and len(os.listdir(path + f'\{element}')) == 0:
            os.removedirs(path + f'\{element}')


def deep_sort(path):
    files = os.listdir(path)
    if files:
        for element in files:
            if os.path.isdir(f'{path}\{element}') and element not in ['images', 'documents', 'video', 'music', 'archives']:
                    sort_files(f'{path}\{element}')
    

def main():
    path = input("Choose directory: ")

    sort_files(path)

    t1 = Thread(target=deep_sort, args=(fr'{path}', ))
    t1.start()


if __name__ == "__main__":
    main()
