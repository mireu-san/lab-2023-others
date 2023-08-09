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
    
    def test_post_list(self):
        print('-- 1차 테스트 시작 --')
        # Step 1
        # 테스트 목적 또는 시나리오, 기타 설명: 페이지 접속 및 상속 확인
        # 1.1 /blog/ 페이지 접속하여 목록을 가져옵니다.
        response = self.client.get('/blog/')
        # 1.2 정상 접속이 되면 페이지 타이틀은 'Blog'입니다.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        soup = BeautifulSoup(response.content, 'html.parser')
        self.assertEqual(soup.title.text, 'Blog')
        # 1.4 페이지 상속이 제대로 되어 메뉴와 Footer가 있습니다.
        navbar = soup.nav
        # footer = soup.footer
        # 1.5 Home, Blog, About 문구가 메뉴에 있습니다.
        self.assertIn('Home', navbar.text)
        self.assertIn('Blog', navbar.text)
        self.assertIn('About', navbar.text)
        # self.assertIn('Contact', navbar.text) # 실패 코드
        print('-- 1차 테스트 완료 --')
        print('-- 2차 테스트 시작 --')
        # Step 2
        # 테스트 목적 또는 시나리오, 기타 설명: None
        # 2.1 게시물이 하나도 없다면 '아직 게시물이 없습니다.'라는 문구가 나옵니다.
        # if Post.objects.count() == 0:
        #     self.assertIn('아직 게시물이 없습니다.', soup.body.text)
        # 2.2 게시물이 있다면 게시물의 타이틀과 날짜, 작성자가 나옵니다.
        # else:
        #     main_area = soup.find('div', id='main-area')
        #     self.assertIn(self.post_001.title, main_area.text)
        #     self.assertIn(self.post_001.author.username.upper(), main_area.text)
        #     self.assertIn(self.post_001.created.strftime('%Y-%m-%d'), main_area.text)
        print('-- 2차 테스트 완료 --')
        print('-- 3차 테스트 시작 --')
        # Step 3
        # 테스트 목적 또는 시나리오, 기타 설명: None
        # 3.1 포트스트 2개 만듦
        # 3.2 포스트 목록 페이지를 새로고침했을 때
        # 3.3 main area에 포스트 2개의 타이틀이 존재한다.
        # 3.4 '아직 게시물이 없습니다.'라는 문구는 더 이상 나타나지 않는다.
        print('-- 3차 테스트 완료 --')