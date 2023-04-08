import PyPDF2
import os
from pprint import pprint
from utils.log import logger


INPUT_FILES_PATH = 'input_files'

parts = []


def visitor_body(text, cm, tm, fontDict, fontSize):
    '''
    TODO add doc string
    '''
    y = tm[5]
    if y > 50 and y < 572:
        parts.append(text)


def get_images(file_name: str):
    '''
    TODO add doc string
    '''
    reader = PyPDF2.PdfReader(f'{INPUT_FILES_PATH}/{file_name}')

    page = reader.pages[0]
    count = 0

    for image_file_object in page.images:
        with open(str(count) + image_file_object.name, 'wb') as fp:
            fp.write(image_file_object.data)
            count += 1


def read_file(file_name: str):
    '''
    TODO add doc string
    '''
    files = os.listdir(INPUT_FILES_PATH)
    print('Files in directory: ', files)
    reader = PyPDF2.PdfReader(f'{INPUT_FILES_PATH}/{file_name}')
    pages = len(reader.pages)
    print(f'Pages: {pages}')
    pprint(f'Metadata: {reader.metadata}')
    for i in range(14):
        read_page = reader.pages[i].extract_text(visitor_text=visitor_body)
        # print(f'--------Text from page {i}: {read_page}')
        text_body = ''.join(parts)
    print(f'Text body: {text_body}')
    try:
        temp_file = file_name.replace('.pdf', '.txt')
        with open(temp_file, 'w', encoding='utf-8') as file:
            file.write(text_body)
    except IOError as error:
        logger.error('Error: %s', error)

    # Loop through files in input_files directory
    # for file in files:
    #     if file.endswith('pdf'):
    #         print(f'File: {file}')
    #         reader = PyPDF2.PdfReader(file)
    #         print(f'Pages in file: ', len(reader.pages))
            
    #         i = 12
    #         for page in reader.pages:
    #             if i < 14:
    #                 print('----------------------Page: ', i)
    #                 # print(reader.pages[i].extract_text())
    #                 read_page = reader.pages[i]
    #                 read_page.extract_text(visitor_text=visitor_body)
    #                 text_body = "".join(parts)
    #                 print(f'Text body: {text_body}')
    #                 i = i+1
                    
# def read_file(file_name: str):
#     print('Current dir: ', os.getcwd())
#     os.chdir(INPUT_FILES_PATH)
#     files = os.listdir()
#     print('Files in directory: ', files)
#     # Loop through files in input_files directory
#     for file in files:
#         if file.endswith('pdf'):
#             print(f'File: {file}')
#             reader = PyPDF2.PdfReader(file)
#             print(f'Pages in file: ', len(reader.pages))
            
#             i = 1
#             for page in reader.pages:
#                 if i < 6:
#                     print('----------------------Page: ', i)
#                     # print(reader.pages[i].extract_text())
#                     read_page = reader.pages[i]
#                     read_page.extract_text(visitor_text=visitor_body)
#                     text_body = "".join(parts)
#                     print(f'Text body: {text_body}')
#                     i = i+1