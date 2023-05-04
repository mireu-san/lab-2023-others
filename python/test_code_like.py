like = ["볶음밥", "라면", "국수", "파스타", "치킨", "짜장면", "국밥"]
dislike = ["국밥", "짬뽕", "찜닭", "파스타", "국수", "카레", "덮밥"]

plate = list(set(like + dislike))

conclusion = []

for i in like:
    if i not in dislike:
        conclusion.append(i)

print(conclusion)
