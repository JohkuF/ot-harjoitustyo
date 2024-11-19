import unittest

from constants import TILE_SIZE, HEIGHT, WIDTH


class TestWorld(unittest.TestCase):

    def test_world_shape(self):
        """
        Test that current world size fits to screen
        """
        self.assertTrue(HEIGHT % TILE_SIZE == 0)
        self.assertTrue(WIDTH % TILE_SIZE == 0)
