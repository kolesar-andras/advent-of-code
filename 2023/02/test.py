import unittest
from code import Set, Game

class Test(unittest.TestCase):
    def test_set(self):
        self.assertEqual(3, Set('3 blue').blue)
        self.assertEqual(2, Set('2  red').red)
        self.assertFalse(Set('') > Set(''))
        self.assertFalse(Set('') > Set('0 red'))
        self.assertFalse(Set('') > Set('1 red'))
        self.assertFalse(Set('1 red') > Set('2 red'))
        self.assertFalse(Set('2 red') > Set('2 red'))
        self.assertTrue(Set('3 red') > Set('2 red'))
        self.assertTrue(Set('1 green') > Set('0 red'))
        self.assertTrue(Set('2 green') > Set('2 red'))
        self.assertTrue(Set('3 green, 2 red') > Set('1 red, 1 green'))
        self.assertTrue(Set('3 green, 2 red, 1 blue') > Set('1 red, 1 green'))
        self.assertTrue(Set('3 green, 2 red, 1 blue') > Set('1 red, 1 green, 1 blue'))
        self.assertTrue(Set('3 green') > Set('1 red, 1 green'))
        self.assertFalse(Set('3 green') > Set('1 red, 3 green'))
        self.assertEqual(Set('4 red, 2 green, 6 blue'), Set('3 blue, 4 red').max(Set('1 red, 2 green, 6 blue')))

    def test_game(self):
        game = Game('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
        self.assertEqual(1, game.id)
        self.assertEqual(3, len(game.sets))
        self.assertEqual(4, game.sets[0].red)
        self.assertEqual(Set('4 red, 2 green, 6 blue'), game.min())
        self.assertEqual(48, game.power())

        self.assertTrue(game.is_possible(Set('4 red, 6 blue, 2 green')))
        self.assertFalse(game.is_possible(Set('4 red, 6 blue, 1 green')))
        self.assertFalse(game.is_possible(Set('4 red, 6 blue')))
        self.assertFalse(game.is_possible(Set('4 red, 6 blue, 0 green')))

        game = Game('Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green')
        self.assertTrue(game.is_possible(Set('12 red, 13 green, 14 blue')))
        self.assertEqual(36, game.power())
