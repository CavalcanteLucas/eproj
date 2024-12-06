
def calc(input_data):
    debt = input_data["value"]
    value = input_data["value"]

    time = input_data["time"]
    rate_buy = input_data["rate_buy"]
    rate_save = input_data["rate_save"]

    fixed = debt/time

    print(f"+-------+-----------+---------+-----------+------------+------------+-----------+")
    print(f"| Month |   Debt    |  Fixed  | Interest  |  Partial  |||  Invested |   Yield   |")
    print(f"+-------+-----------+---------+-----------+------------+------------+-----------+")

    total_interest = 0
    total_partial = 0
    total_yield = 0

    for i in range(time):
        interest = debt * rate_buy / 100
        total_interest = total_interest + interest
        partial = interest + fixed
        total_partial = total_partial + partial

        yield_ = value * rate_save / 100
        total_yield = total_yield + yield_


        print(f"| {i + 1:<5} | {debt:>9.2f} | {fixed:>6.2f} | {interest:>9.2f} | {partial:>9.2f} ||| {value:>9.2f} | {yield_:>9.2f} |")

        debt = debt - fixed
        value = value + yield_ - partial
        if value < 0:
            value = 0


    print(f"+-------+-----------+---------+-----------+------------+------------+-----------+")
    print(f"|       |           |         |  {total_interest:>8.2f} | {total_partial:>8.2f} ||| {value:>9.2f} | {total_yield:>8.2f} |")
    print(f"+-------+-----------+---------+-----------+------------+------------+-----------+")


def main():

    input_data = {
        "value": 150000.00,
        "time": 120,
        "rate_buy": 0.75,
        "rate_save": 0.5,
    }

    calc(input_data)
    

if __name__ == "__main__":
    main()