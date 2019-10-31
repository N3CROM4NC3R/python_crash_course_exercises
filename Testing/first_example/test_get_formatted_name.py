from unittest import TestCase


from name_function import get_formatted_name

class TestGet_formatted_name(TestCase):
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart'?"""
        formatted_name = get_formatted_name(
        first='wolfgang',middle='amadeus',last='mozart')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

