import os
import sys
from pathlib import Path
import shutil

picture_extension = ['jpeg', 'png', 'jpg', 'psd']
video_extension = ['avi', 'mp4', 'mov']
documents_extension = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
music_extension = ['mp3', 'ogg', 'wav', 'amr']
archive_extension = ['zip', 'gz', 'tar']


def normalize(text):
    map = {ord('а'):'a',ord('б'):'b',ord('в'):'v',ord('г'):'g',ord('д'):'d',ord('е'):'e',ord('ё'):'e',
      ord('ж'):'zh',ord('з'):'z',ord('и'):'i',ord('й'):'i',ord('к'):'k',ord('л'):'l',ord('м'):'m',ord('н'):'n',
      ord('о'):'o',ord('п'):'p',ord('р'):'r',ord('с'):'s',ord('т'):'t',ord('у'):'u',ord('ф'):'f',ord('х'):'h',
      ord('ц'):'c',ord('ч'):'ch',ord('ш'):'sh',ord('щ'):'shch',ord('ъ'):'',ord('ы'):'y',ord('ь'):'',ord('э'):'e',
      ord('ю'):'u',ord('я'):'ia', ord('А'):'A',ord('Б'):'B',ord('В'):'V',ord('Г'):'G',ord('Д'):'D',ord('Е'):'E',ord('Ё'):'E',
      ord('Ж'):'Zh',ord('З'):'Z',ord('И'):'I',ord('Й'):'I',ord('К'):'K',ord('Л'):'L',ord('М'):'M',ord('Н'):'N',
      ord('О'):'O',ord('П'):'P',ord('Р'):'R',ord('С'):'S',ord('Т'):'T',ord('У'):'U',ord('Ф'):'F',ord('Х'):'H',
      ord('Ц'):'C',ord('Ч'):'Ch',ord('Ш'):'Sh',ord('Щ'):'Shch',ord('Ъ'):'',ord('Ы'):'y',ord('Ь'):'',ord('Э'):'E',
      ord('Ю'):'U',ord('Я'):'Ya',ord('ґ'):'g',ord('Ґ'):'G',ord('Є'):'E', ord('.'):'_', ord('/'):'_', ord(' '):'_',
      ord(','):'_', ord('"'):'_', ord('\''):'_', ord('-'):'_', ord('='):'_', ord('+'):'_', ord('!'):'_', ord('@'):'_',
      ord('#'):'_', ord('$'):'_', ord('%'):'_', ord('^'):'_', ord('&'):'_', ord('*'):'_', ord('('):'_', ord(')'):'_'}
    translated = text.translate(map)
    return(translated)



def sort_images(path = sys.argv[1]):
    files = os.listdir(path)
    os.makedirs(f'{sys.argv[1]}\images')
    for element in files:
        new_element = element.split('.')
        new_element_str = '.'.join(new_element[0:-1])
        if new_element[-1].lower() in picture_extension:
            if os.path.isfile(f'{path}\{element}'):
                shutil.copyfile(f'{path}\{element}', f'{sys.argv[1]}\images\{normalize(new_element_str)}.{new_element[-1]}')
            if os.path.isdir(f'{path}\{element}'):
                sort_images(f'{path}\{element}')


def sort_documents(path = sys.argv[1]):
    files = os.listdir(path)
    os.makedirs(f'{sys.argv[1]}\documents')
    for element in files:
        new_element = element.split('.')
        new_element_str = '.'.join(new_element[0:-1])
        if new_element[-1].lower() in documents_extension:
            if os.path.isfile(f'{path}\{element}'):
                shutil.copyfile(f'{path}\{element}', f'{sys.argv[1]}\documents\{normalize(new_element_str)}.{new_element[-1]}')
            if os.path.isdir(f'{path}\{element}'):
                sort_documents(f'{path}\{element}')

def sort_videos(path = sys.argv[1]):
    files = os.listdir(path)
    os.makedirs(f'{sys.argv[1]}\\video')
    for element in files:
        new_element = element.split('.')
        new_element_str = '.'.join(new_element[0:-1])
        if new_element[-1].lower() in video_extension:
            if os.path.isfile(f'{path}\{element}'):
                shutil.copyfile(f'{path}\{element}', f'{sys.argv[1]}\\video\{normalize(new_element_str)}.{new_element[-1]}')
            if os.path.isdir(f'{path}\{element}'):
                sort_documents(f'{path}\{element}')

def sort_music(path = sys.argv[1]):
    files = os.listdir(path)
    os.makedirs(f'{sys.argv[1]}\music')
    for element in files:
        new_element = element.split('.')
        new_element_str = '.'.join(new_element[0:-1])
        if new_element[-1].lower() in music_extension:
            if os.path.isfile(f'{path}\{element}'):
                shutil.copyfile(f'{path}\{element}', f'{sys.argv[1]}\music\{normalize(new_element_str)}.{new_element[-1]}')
            if os.path.isdir(f'{path}\{element}'):
                sort_music(f'{path}\{element}')

def sort_archives(path = sys.argv[1]):
    os.makedirs(f'{sys.argv[1]}\\archives')
    files = os.listdir(path)
    for element in files:
        new_element = element.split('.')
        new_element_str = '.'.join(new_element[0:-1])
        if new_element[-1].lower() in archive_extension:
            if os.path.isfile(f'{path}\{element}'):
                shutil.unpack_archive(f'{path}\{element}', f'{sys.argv[1]}\\archives\{normalize(new_element_str)}')
            if os.path.isdir(f'{path}\{element}'):
                sort_music(f'{path}\{element}')

def empty_folder_delete(path = sys.argv[1]):
    files = os.listdir(path)
    for file in files:
        if os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) == 0 and file not in ['video', 'documents', 'music', 'images', 'archives']:
            os.removedirs(path + f'\{file}')
        elif os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) > 0:
            empty_folder_delete(path + f'\{file}')

def main():
    sort_images()
    sort_documents()
    sort_videos()
    sort_music()
    sort_archives()
    empty_folder_delete()





if __name__ == "__main__":
    main()
