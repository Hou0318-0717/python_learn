user_input = "100"
price = int(user_input)
print(f"商品价格：{price}元")

numbers_str = ["10","20","30"]
numbers = [int(n) for n in numbers_str]
print(numbers)

total = sum(numbers)
print(f"总和：{total}")

price_str = "19.99"
price2 = int(float(price_str))
print(f"价格（取整）：{price2}元")