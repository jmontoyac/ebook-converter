'''
TODO Add docstring
'''
from ebooklib import epub
from utils.log import logger


class EpubBook():
    '''
    TODO Add docstring
    '''
    book = epub.EpubBook

    def set_metadata(self, id: str, title: str, language: str,
                     author: str) -> bool:
        '''
        TODO Add docstring
        '''
        result = False

        try:
            self.book.set_identifier(id)
            self.book.set_title(title)
            self.book.set_language(language)
            self.book.add_author(author)
            result = True
        except UnicodeError as error:
            logger.error('Error: %s', error)

        return result

    def set_chapter(self, title: str, input_file: str,
                    language: str) -> any:
        '''
        TODO Add docstring
        '''

        chapter = epub.EpubHtml(title=title, file_name=input_file,
                                lang=language)
        chapter.content = (
            '<h1>Intro heading</h1>'
            '<p>texto del capitulo</p>'
        )

        return chapter
    
    def add_items(self, chapter):
        '''
        TODO Add docstring
        '''
        self.book.add_item(chapter)
        self.book.add_item(epub.EpubNcx)
        self.book.add_item(epub.EpubNav)
