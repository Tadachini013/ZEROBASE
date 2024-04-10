money = 1000
print("現在の所持金"+str(money)+"円")
items = {'apple': 100, 'banana': 200, 'orange': 400}
Firstbuy = True

print("本日の売り出しもの")
for dis_mess in items:
    print(dis_mess + '：1個' + str(items[dis_mess]) + '円')
      
for item_name in items:
    print('-----------------ご注文---------------------------')
    
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    #print('購入する' + item_name + 'の個数は' + input_count + '個です')
    print(item_name+":"+input_count+"個")
    count = int(input_count)
    total_price = items[item_name] * count
    
    #そもそもお金が足りなかった場合
    if((total_price > money) & Firstbuy):
        print("お金が足りません。買い物を中断します")
        break 
    #少なくとも買い物はできる
    Firstbuy=False

    print('支払い金額：' + str(total_price) + '円')
    
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        
        if money == 0:
            print('財布が空になりました')
            break
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
        
print('残金は' + str(money) + '円です')
