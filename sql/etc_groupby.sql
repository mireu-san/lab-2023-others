SELECT name as FruitName, SUM(quantity) as TotalQuantity
FROM Fruits
GROUP BY name;