import unittest
from models import source

Source = source.Source


class NewsTest(unittest.TestCase):
    '''
    testing the behaviour of the news class
    '''

    def setUp(self):
        '''
        set up method to run before every Test
        :return:
        '''
        self.new_source = Source('ABC News', 'http://abcnews.go.com', "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


if __name__ == "__main__":
    unittest.main()
