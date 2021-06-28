import asyncio
from aiopath import AsyncPath
from asyncio import run, gather
import os
import shutil

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
           ord('Ю'): 'U', ord('Я'): 'Ya', ord('ґ'): 'g', ord('Ґ'): 'G', ord('Є'): 'E', ord('.'): '.', ord('/'): '/',
           ord(' '): ' ',
           ord(','): ',', ord('"'): '"', ord('\''): '\'', ord('-'): '-', ord('='): '=', ord('+'): '+', ord('!'): '!',
           ord('@'): '@',
           ord('#'): '#', ord('$'): '$', ord('%'): '%', ord('^'): '^', ord('&'): '&', ord('*'): '*', ord('('): '(',
           ord(')'): ')'}

    translated = text.translate(map)
    return translated

async def file_handler(path, parametre):
    picture_extension = ['jpeg', 'png', 'jpg', 'psd']
    picture_file_list = []
    documents_extension = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
    documents_file_list = []
    video_extension = ['avi', 'mp4', 'mov']
    video_file_list = []
    music_extension = ['mp3', 'ogg', 'wav', 'amr']
    music_file_list = []
    archive_extension = ['zip', 'gz', 'tar']
    archive_file_list = []
    folders = []
    files = os.listdir(path)
    if files:
        for file in files:
            new_element = file.split('.')
            if new_element[-1] in picture_extension:
                picture_file_list.append(file)
            elif new_element[-1] in documents_extension:
                documents_file_list.append(file)
            elif new_element[-1] in video_extension:
                video_file_list.append(file)
            elif new_element[-1] in music_extension:
                music_file_list.append(file)
            elif new_element[-1] in archive_extension:
                archive_file_list.append(file)
            elif os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) != 0:
                folders.append(file)
            elif os.path.isdir(path + f'\{file}') and len(os.listdir(path + f'\{file}')) == 0:
                os.removedirs(path + f'\{file}')
        if parametre == "picture":
            return picture_file_list
        elif parametre == "documents":
            return documents_file_list
        elif parametre == "video":
            return video_file_list
        elif parametre == "music":
            return music_file_list
        elif parametre == "archive":
            return archive_file_list
        elif parametre == "folders":
            return folders
        else:
            return None
    else:
        os.removedirs(path)


async def picture_handle(path):
    files_list = await file_handler(path, 'picture')
    folders = await file_handler(path, 'folders')
    os.makedirs(f'{path}\images')
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\images\{normalize(file)}')
    await asyncio.sleep(1)
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await picture_handle(f'{path}\{folder}')
    

async def document_handle(path):
    files_list = await file_handler(path, 'documents')
    folders = await file_handler(path, 'folders')  
    os.makedirs(f'{path}\documents')
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\documents\{normalize(file)}')
    await asyncio.sleep(1)
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await document_handle(f'{path}\{folder}')

async def video_handle(path):
    files_list = await file_handler(path, 'video')
    folders = await file_handler(path, 'folders')   
    os.makedirs(f'{path}\\video')
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\\video\{normalize(file)}')
    await asyncio.sleep(1)
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await video_handle(f'{path}\{folder}')


async def music_handle(path):
    files_list = await file_handler(path, 'music')
    folders = await file_handler(path, 'folders')   
    os.makedirs(f'{path}\music')
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.copyfile(f'{path}\{file}', f'{path}\music\{normalize(file)}')
    await asyncio.sleep(1)
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await music_handle(f'{path}\{folder}')

async def archive_handle(path):
    files_list = await file_handler(path, 'archive')
    folders = await file_handler(path, 'folders')
    os.makedirs(f'{path}\\archives')
    for file in files_list:
        if os.path.isfile(f'{path}\{file}'):
            shutil.unpack_archive(f'{path}\{file}', f'{path}\\archives\{normalize(file)}')
    await asyncio.sleep(1)
    for folder in folders:
        if folder not in ['images', 'documents', 'music', 'video', 'archives']:
            await archive_handle(f'{path}\{folder}')


async def main():
    path = input("Choose directory: ")
    tasks = [picture_handle(path), document_handle(path), music_handle(path), video_handle(path), archive_handle(path)]
    await gather(*tasks)



if __name__ == "__main__":
    
    run(main())