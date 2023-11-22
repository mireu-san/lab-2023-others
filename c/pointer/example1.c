#include <stdio.h>

// 책에 대한 구조체 정의
typedef struct {
    char title[50];
    int borrowed; // 0은 안 빌려진 상태, 1은 빌려진 상태
} Book;

// 책을 빌려주는 함수
void borrowBook(Book *book) {
    book->borrowed = 1; // 책의 상태를 '빌려짐'으로 변경
    printf("'%s'가 빌려졌습니다.\n", book->title);
}

int main() {
    Book myBook = {"메모리와 C, 그리고 포인터", 0}; // 책 생성

    printf("책을 빌려주기 전 상태: %d\n", myBook.borrowed);
    borrowBook(&myBook); // 책의 주소를 전달하여 빌려줌
    printf("책을 빌려준 후 상태: %d\n", myBook.borrowed);

    return 0;
}
