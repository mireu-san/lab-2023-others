fetch("censored")
  .then((response) => response.json())
  .then((data) => {
    // 배열.reduce((누적값, 현잿값, 인덱스, 요소) => { return 결과 }, 초깃값)
    const sumProducts = data.reduce((acc, cur) => acc + cur.stockCount, 0);
    const totalAvgPrice = Math.round(
      data.reduce((acc, cur) => acc + cur.price, 0) / data.length
    );

    console.log("전체 product의 갯수:", sumProducts);
    console.log("전체 가격의 평균:", totalAvgPrice);
  });
