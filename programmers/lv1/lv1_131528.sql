# 전체 COUNT 선택 AS USERS
SELECT COUNT(*) AS USERS
# 회원 정보
FROM USER_INFO
# 테이블에서 나이 정보가 없는 회원
WHERE AGE IS NULL;

# 추신: sql 풀었던 부분은 지금껏 여기에 기록하지 않았음. 프로그래머스 계정 내역 참고.