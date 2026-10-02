def mincoin(coins, amount):
    coins.sort(reverse=True)
    coins_used = []
    total_coin_count = 0

    for coin in coins:
        while amount >= coin:
            amount -= coin
            coins_used.append(coin)
            total_coin_count += 1

    if amount != 0:
        return None, "It is not possible to exchange"

    return coins_used, total_coin_count


coin = [1, 5, 10, 25]
target_amount = 36

coins_used, total_coin_count = mincoin(coin, target_amount)

print(f"Target amount: {target_amount}")
print(f"Coins used: {coins_used}")
print(f"Total coins used: {total_coin_count}")