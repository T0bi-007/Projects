import unittest
import sys
from wordle import prepare_game, get_feedback, is_valid_guess, CORRECT_COLOR


class TestGetFeedback(unittest.TestCase):
    """Get Feedback Tests"""

    def test_get_feedback_1(self):
        """get_feedback(): secret word basil and guessed word basil"""
        secret_word = "basil"
        guessed_word = "basil"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;92mb\033[0m\033[1;92ma\033[0m\033[1;92ms\033[0m\033[1;92mi\033[0m\033[1;92ml\033[0m"
        else:
            expected = "\033[1;91mb\033[0m\033[1;91ma\033[0m\033[1;91ms\033[0m\033[1;91mi\033[0m\033[1;91ml\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_2(self):
        """get_feedback(): secret word lever and guessed word light"""
        secret_word = "lever"
        guessed_word = "light"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;92ml\033[0m\033[1;97mi\033[0m\033[1;97mg\033[0m\033[1;97mh\033[0m\033[1;97mt\033[0m"
        else:
            expected = "\033[1;91ml\033[0m\033[1;97mi\033[0m\033[1;97mg\033[0m\033[1;97mh\033[0m\033[1;97mt\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_3(self):
        """get_feedback(): secret word llama and guessed word ladle"""
        secret_word = "llama"
        guessed_word = "ladle"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;92ml\033[0m\033[1;93ma\033[0m\033[1;97md\033[0m\033[1;93ml\033[0m\033[1;97me\033[0m"
        else:
            expected = "\033[1;91ml\033[0m\033[1;94ma\033[0m\033[1;97md\033[0m\033[1;94ml\033[0m\033[1;97me\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_4(self):
        """get_feedback(): secret word aback and guessed word abaca"""
        secret_word = "aback"
        guessed_word = "abaca"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;92ma\033[0m\033[1;92mb\033[0m\033[1;92ma\033[0m\033[1;92mc\033[0m\033[1;97ma\033[0m"
        else:
            expected = "\033[1;91ma\033[0m\033[1;91mb\033[0m\033[1;91ma\033[0m\033[1;91mc\033[0m\033[1;97ma\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_5(self):
        """get_feedback(): secret word hello and guessed word label"""
        secret_word = "hello"
        guessed_word = "label"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;93ml\033[0m\033[1;97ma\033[0m\033[1;97mb\033[0m\033[1;93me\033[0m\033[1;93ml\033[0m"
        else:
            expected = "\033[1;94ml\033[0m\033[1;97ma\033[0m\033[1;97mb\033[0m\033[1;94me\033[0m\033[1;94ml\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_6(self):
        """get_feedback(): secret word gaily and guessed word hello"""
        secret_word = "gaily"
        guessed_word = "hello"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;97mh\033[0m\033[1;97me\033[0m\033[1;97ml\033[0m\033[1;92ml\033[0m\033[1;97mo\033[0m"
        else:
            expected = "\033[1;97mh\033[0m\033[1;97me\033[0m\033[1;97ml\033[0m\033[1;91ml\033[0m\033[1;97mo\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_7(self):
        """get_feedback(): secret word riped and guessed word crown"""
        secret_word = "riped"
        guessed_word = "crown"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;97mc\033[0m\033[1;93mr\033[0m\033[1;97mo\033[0m\033[1;97mw\033[0m\033[1;97mn\033[0m"
        else:
            expected = "\033[1;97mc\033[0m\033[1;94mr\033[0m\033[1;97mo\033[0m\033[1;97mw\033[0m\033[1;97mn\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_8(self):
        """get_feedback(): secret word table and guessed word metal"""
        secret_word = "table"
        guessed_word = "metal"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;97mm\033[0m\033[1;93me\033[0m\033[1;93mt\033[0m\033[1;93ma\033[0m\033[1;93ml\033[0m"
        else:
            expected = "\033[1;97mm\033[0m\033[1;94me\033[0m\033[1;94mt\033[0m\033[1;94ma\033[0m\033[1;94ml\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_9(self):
        """get_feedback(): secret word table and guessed word metal"""
        secret_word = "index"
        guessed_word = "linen"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;97ml\033[0m\033[1;93mi\033[0m\033[1;93mn\033[0m\033[1;92me\033[0m\033[1;97mn\033[0m"
        else:
            expected = "\033[1;97ml\033[0m\033[1;94mi\033[0m\033[1;94mn\033[0m\033[1;91me\033[0m\033[1;97mn\033[0m"
        self.assertEqual(actual, expected)

    def test_get_feedback_10(self):
        """get_feedback(): secret word bleak and guessed word helix"""
        secret_word = "bleak"
        guessed_word = "helix"
        actual = get_feedback(secret_word, guessed_word)
        if CORRECT_COLOR == "\033[1;92m":
            expected = "\033[1;97mh\033[0m\033[1;93me\033[0m\033[1;93ml\033[0m\033[1;97mi\033[0m\033[1;97mx\033[0m"
        else:
            expected = "\033[1;97mh\033[0m\033[1;94me\033[0m\033[1;94ml\033[0m\033[1;97mi\033[0m\033[1;97mx\033[0m"
        self.assertEqual(actual, expected)


class TestPrepareGame(unittest.TestCase):
    """Prepare Game Tests"""

    def test_prepare_game_1(self):
        """prepare_game(): 5 letter lowercase word"""
        sys.argv = ["wordle.py", "tests"]
        actual, _ = prepare_game()
        expected = "tests"
        self.assertEqual(actual, expected)

    def test_prepare_game_2(self):
        """prepare_game(): too many arguments"""
        sys.argv = ["wordle.py", "too", "many", "args"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_3(self):
        """prepare_game(): too many characters"""
        sys.argv = ["wordle.py", "toomanychars"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_4(self):
        """prepare_game(): invalid command line arguments"""
        sys.argv = ["wordle.py", "hello", "birdy", "again"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_5(self):
        """prepare_game(): bad user input"""
        sys.argv = ["wordle.py", "TESTS"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_6(self):
        """prepare_game(): seed"""
        sys.argv = ["wordle.py", "1234"]
        actual, _ = prepare_game()
        expected = "smell"
        self.assertEqual(actual, expected)

    def test_prepare_game_7(self):
        """prepare_game(): invalid command line argument"""
        sys.argv = ["wordle.py", "he110"]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_8(self):
        """prepare_game(): bad user input"""
        sys.argv = ["wordle.py", "1."]
        with self.assertRaises(ValueError):
            prepare_game()

    def test_prepare_game_9(self):
        """prepare_game(): 5 letter lowercase word"""
        sys.argv = ["wordle.py", "hello"]
        actual, _ = prepare_game()
        expected = "hello"
        self.assertEqual(actual, expected)

    def test_prepare_game_10(self):
        """prepare_game(): seed"""
        sys.argv = ["wordle.py", "554"]
        actual, _ = prepare_game()
        expected = "trick"
        self.assertEqual(actual, expected)


class TestIsValidGuess(unittest.TestCase):
    """Is Valid Guess Tests"""

    def test_is_valid_guess_1(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "table"]
        guess = "metal"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_guess_2(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "154"]
        guess = "stars"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_guess_3(self):
        """is_valid_guess(): invalid guess due to @"""
        sys.argv = ["wordle.py", "elbow"]
        guess = "@llow"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_guess_4(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "abaca"]
        guess = "gaily"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_guess_5(self):
        """is_valid_guess(): 5 letter lower case invalid guess (not a word)"""
        sys.argv = ["wordle.py", "hello"]
        guess = "djkaj"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_guess_6(self):
        """is_valid_guess(): 5 letter lower case invalid guess (nums)"""
        sys.argv = ["wordle.py", "hello"]
        guess = "1jkaj"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_guess_7(self):
        """is_valid_guess(): 5 letter invalid guess (casing)"""
        sys.argv = ["wordle.py", "train"]
        guess = "tRaIn"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_guess_8(self):
        """is_valid_guess(): invalid guess due to length and !"""
        sys.argv = ["wordle.py", "brain"]
        guess = "brains!"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = False
        self.assertEqual(actual, expected)

    def test_is_valid_guess_9(self):
        """is_valid_guess(): 5 letter lower case valid guess"""
        sys.argv = ["wordle.py", "lllll"]
        guess = "prays"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)

    def test_is_valid_guess_10(self):
        """is_valid_guess(): 5 letter lower case valid guess with custom word"""
        sys.argv = ["wordle.py", "bleak"]
        guess = "adept"
        _, valid_guesses = prepare_game()
        actual = is_valid_guess(guess, valid_guesses)
        expected = True
        self.assertEqual(actual, expected)


def main():
    """Main function to run tests based on command-line arguments."""
    test_cases = {
        "feedback": TestGetFeedback,
        "prepare": TestPrepareGame,
        "valid": TestIsValidGuess,
    }

    usage_string = (
        "Usage: python test_wordle.py [test_type] [test_number]\n"
        "Examples:\n"
        "    python test_traversals.py feedback 1\n"
        "    python test_traversals.py prepare 4\n"
        "Valid options for [test_type]: " + ", ".join(test_cases.keys()) + "\n"
        "Test cases range from 1-10."
    )

    if len(sys.argv) > 3:
        print(usage_string)
        return
    if len(sys.argv) == 1:
        unittest.main()
        return
    sys.argv = sys.argv[1:]
    test_name = sys.argv[0]
    if test_name not in test_cases:
        print(
            f"Invalid test name: {test_name}. Valid options are: {', '.join(test_cases.keys())}"
        )
        return
    if len(sys.argv) == 1:
        # Extract test case based on the first command-line argument
        suite = unittest.TestLoader().loadTestsFromTestCase(test_cases[test_name])
    else:
        grid_dimensions = sys.argv[1]
        loader = unittest.TestLoader()

        # Load all tests from the test case class
        all_tests = loader.loadTestsFromTestCase(test_cases[test_name])
        suite = unittest.TestSuite()
        # Filter tests that end with 'success'
        for test in all_tests:
            if test.id().split(".")[-1].endswith(grid_dimensions):
                suite.addTest(test)
        if not suite.countTestCases():
            print(usage_string)
            return
    unittest.TextTestRunner().run(suite)


if __name__ == "__main__":
    main()
