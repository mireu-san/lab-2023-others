# beautifulsoup!

import unittest

def add(x, y):
    return x + y


class TestAdd(unittest.TestCase):
    def test_add(self):
        # assertEqual - 두 값이 같은지 확인
        self.assertEqual(add(1, 2), 3)

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == '__main__':
    unittest.main()

# (메모용) cheat sheet - TDD method
# self.assertEqual(1 + 2, 3)
# self.assertTrue(10 == 10)
# self.assertFalse(1 == 10)
# self.assertGreater(10, 1)
# self.assertLess(1, 10)
# self.assertIn(1, [1, 2, 3, 4, 5])
# self.assertIsInstance('a', str)

# 핵심.
# 코드를 작성하기 전 테스트를 먼저 작성하고 그 테스트를 통과하도록 코드를 구현하는 개발 방법론
