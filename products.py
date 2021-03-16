product = []
while True:
    x = input('請輸入商品名稱: ')
    if x == 'Q':
        break
    y = input('請輸入商品價格: ')
    p = [x, y]
    product.append(p)
print(product)
print(product[0][1])#第0格的第1格
