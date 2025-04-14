from abc import ABC, abstractmethod

class StorySource(ABC):
    @abstractmethod
    def get_story(self):
        pass


class Book(StorySource):
    def get_story(self):
        print("Чтение истории")


class AudioBook(StorySource):
    def get_story(self):
        print("Прослушивание истории")


class StoryReader():
    def __init__(self, story_source : StorySource):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()


book = Book()
audio_book = AudioBook()

readerbook = StoryReader(book)
readeraudiobook = StoryReader(audio_book)

readerbook.tell_story()
readeraudiobook.tell_story()