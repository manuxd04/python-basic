import unittest

class IsItANumberTask(unittest.TestCase):
    """
    Skriv ferdig metoden så sier om maybe_number er et tall eller ikke.

    """
    def is_a_number(self, maybe_number):
        ## TODO SKRIV KODEN HER
        is_number = False
        return is_number;

    def test_true(self):
        self.assertTrue(self.is_a_number("1"), True)

    def test_false(self):
        self.assertTrue(self.is_a_number("Tekst"), False)
        
    def test_pi(self):
        self.assertTrue(self.is_a_number("3.14"), True)

    def test_spaces(self):
        self.assertTrue(self.is_a_number("3    4"), False)
    
    def test_untrimmed(self):
        self.assertTrue(self.is_a_number("3  "), True)
        

if __name__ == '__main__':
    unittest.main()