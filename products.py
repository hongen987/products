product = []
while True:
    x = input('請輸入商品名稱: ')
    if x == 'Q':
        break
    y = input('請輸入商品價格: ')
    p = [x, y]
    product.append(p)
for p in product:
    print(p[0], '的價格是', p[1])
