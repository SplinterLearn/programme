"""Watchlist planner: Block 2 project, step 1 (M2.1). Reference checkpoint."""


def main():
    episodes_left = int(input("How many episodes are left? "))
    episodes_per_day = int(input("How many episodes can you watch per day? "))

    if episodes_left > 0 and episodes_per_day <= 0:
        print("At zero episodes a day you'll never finish. Even one a day gets you there!")
    else:
        days = days_to_finish(episodes_left, episodes_per_day)
        print(f"{days} days to finish. Verdict: {binge_verdict(days)}")


def days_to_finish(episodes_left, episodes_per_day):
    if episodes_left <= 0:
        return 0
    days = episodes_left // episodes_per_day
    if episodes_left % episodes_per_day > 0:
        days = days + 1
    return days


def binge_verdict(days):
    if days == 0:
        return "already done!"
    elif days <= 2:
        return "binge-able this weekend"
    elif days <= 7:
        return "done this week"
    else:
        return "long haul"


if __name__ == "__main__":
    main()
