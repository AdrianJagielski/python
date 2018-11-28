from unittest import TestCase
from scrable import createparser,Scrabble,LETTER_SCORES


class CommandLineTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        parser = createparser()

        cls.parser = parser


c = Scrabble()


class ScrabbleTestCase(CommandLineTestCase):
    def test_with_empty_args(self):
        for word in Scrabble.words:
            temp = 0
            for char in word:
                temp = temp + LETTER_SCORES.get(char.upper())
            Scrabble.points.append(temp)
        self.assertMultiLineEqual(Scrabble.words[Scrabble.points.index(max(Scrabble.points))],c.fun())

    def test_words_points(self):
        args = self.parser.parse_args(['-w','dog'])
        result = c.mode_m(args.word)
        self.assertEqual(result,5)

    def test_find_word(self):
        args_1 = self.parser.parse_args(['-v', '9'])
        result_1 =c.mode_n(args_1.value)
        for word in Scrabble.words:
            temp = 0
            for char in word:
                if char.upper() in LETTER_SCORES:
                    temp = temp + LETTER_SCORES.get(char.upper())
            if temp == 9:
                Scrabble.value_words.append(word)
        self.assertIn(result_1,Scrabble.value_words)

    def test_words_no_input(self):
        args_2 = self.parser.parse_args(['-w',''])
        result_2 = c.mode_m(args_2.word)
        self.assertEqual(result_2,0)

    def test_value_no_input(self):
        Scrabble.value_words = []
        args_3 = self.parser.parse_args(['-v'])
        print(args_3)
        result_3 = c.mode_n(args_3.value)
        self.assertEqual(result_3, None)