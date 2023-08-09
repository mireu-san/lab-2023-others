# from django.test import TestCase

# # Create your tests here.
# class Test(TestCase):
#     def test_something_one(self):
#         '''
#         블로그 리스트 체크
#         '''
#         self.assertEqual(True, False)

#     def test_something_two(self):
#         '''
#         템플릿 상속 체크
#         '''
#         self.assertEqual(True, True)

from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class Test(TestCase):
    def setUp(self):
        # 가상의 client를 만들어서 사용합니다. 이때 DB는 비어있는 채로 시작합니다.
        self.client = Client()
        # setUp()에서는 주로 테스트를 진행하기 전 아래와 같이 데이터를 생성합니다.
        # self.post_001 = Post.objects.create(
        #     title='첫 번째 포스트입니다.',
        #     content='Hello World. We are the world.',
        # )
    
    def test_name(self):
        pass