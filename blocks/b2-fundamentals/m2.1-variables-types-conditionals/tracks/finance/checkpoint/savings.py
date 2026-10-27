"""Savings planner: Block 2 project, step 1 (M2.1). Reference checkpoint."""


def main():
    price = float(input("How much does it cost? "))
    saved = float(input("How much have you saved so far? "))
    per_week = float(input("How much can you save each week? "))

    if saved < price and per_week <= 0:
        print("Saving nothing per week, you'll never get there. Even a little each week helps!")
    else:
        weeks = weeks_to_goal(price, saved, per_week)
        print(f"{weeks} weeks to go. Verdict: {verdict(saved, price)}")


def weeks_to_goal(price, saved, per_week):
    remaining = price - saved
    if remaining <= 0:
        return 0
    weeks = int(remaining // per_week)
    if remaining % per_week > 0:
        weeks = weeks + 1
    return weeks


def verdict(saved, price):
    if saved >= price:
        return "buy it!"
    elif saved >= price * 0.8:
        return "almost there"
    else:
        return "keep saving"


if __name__ == "__main__":
    main()
