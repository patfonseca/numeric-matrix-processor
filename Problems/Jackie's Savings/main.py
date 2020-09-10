def final_deposit_amount(*interest, amount=1000):
    final_amount = amount
    for n in interest:
        final_amount *= (1 + n / 100)
    return round(final_amount, 2)
