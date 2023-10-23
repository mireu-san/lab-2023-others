#include <stdio.h>

int main(void)
{
    for (int i = 0; i < 10; i++)
    {
        printf("Starting outer loop iteration %d\n", i);  // 첫 번째 루프 내에서 메시지 출력
        for (int j = 0; j < 10; j++)
        {
            printf("(%d, %d) ", i, j);  // 두 번째 루프 내에서 좌표 출력
        }
        printf("\n");  // 각 행이 끝날 때마다 새 줄로 이동
    }
    return 0;
}
