import os
import sys
from pathlib import Path

picture_list = []
video_list = []
documents_list = []
music_list = []
archive_list = []
other_elements_list = []

picture_extension = ['jpeg', 'png', 'jpg', 'psd']
video_extension = ['avi', 'mp4', 'mov']
documents_extension = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'xls', 'pptx']
music_extension = ['mp3', 'ogg', 'wav', 'amr']
archive_extension = ['zip', 'gz', 'tar']

all_extension_list = []


def sort_files(path=sys.argv[1]):

    print(f"Start in {path}")
    files = os.listdir(path)

    for element in files:
        new_element = element.split(".")

        if len(new_element) >= 2:
            all_extension_list.append(new_element[-1].lower())

            if new_element[1].lower() in picture_extension:
                picture_list.append(".".join(new_element))

            elif new_element[1].lower() in documents_extension:
                documents_list.append(".".join(new_element))

            elif new_element[1].lower() in music_extension:
                music_list.append(".".join(new_element))

            elif new_element[1].lower() in video_extension:
                video_list.append(".".join(new_element))

            elif new_element[1].lower() in archive_extension:
                archive_list.append(".".join(new_element))

            else:
                other_elements_list.append(".".join(new_element))

        else:
            if os.path.isdir(path + (f'\{element}')):
                sort_files(path + (f'\{element}'))
            # other_elements_list.append(".".join(new_element))


sort_files()
print("Picture list\n", picture_list)
print("Documents list\n", documents_list)
print("Video list\n", video_list)
print("Music list\n", music_list)
print("Archive list\n", archive_list)
print("Other elements list\n", other_elements_list)
print("All extensions\n", set(all_extension_list))
