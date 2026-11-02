rates = {
    "bike": 10,
    "car": 20,
    "bus": 40
}

daily_limits = {
    "bike": 100,
    "car": 200,
    "bus": 400
}


def read_time(message):
    while True:
        value = input(message).strip()
        parts = value.split(":")

        if len(parts) == 2 and all(p.isdigit() for p in parts):
            hour = int(parts[0])
            minute = int(parts[1])

            if 0 <= hour <= 23 and 0 <= minute <= 59:
                return hour * 60 + minute

        print("Invalid time! Enter time as HH:MM.")


vehicle = input("Vehicle (bike/car/bus): ").strip().lower()

if vehicle not in rates:
    print("Invalid vehicle category.")

else:
    entry = read_time("Entry time (HH:MM): ")
    exit_time = read_time("Exit time (HH:MM): ")

    next_day = input("Exit on next day? (yes/no): ").strip().lower()
    lost = input("Lost ticket? (yes/no): ").strip().lower()

    if next_day not in ["yes", "no"] or lost not in ["yes", "no"]:
        print("Invalid yes/no input.")

    elif next_day == "no" and exit_time <= entry:
        print("Invalid parking duration.")

    else:
        if next_day == "yes":
            duration = (1440 - entry) + exit_time
        else:
            duration = exit_time - entry

        hours = (duration + 59) // 60

        charge = hours * rates[vehicle]
        charge = min(charge, daily_limits[vehicle])

        overnight_fee = 50 if next_day == "yes" else 0
        penalty = 100 if lost == "yes" else 0

        total = charge + overnight_fee + penalty

        print("\n--- PARKING BILL ---")
        print("Vehicle:", vehicle)
        print("Duration:", duration // 60, "hours",
              duration % 60, "minutes")
        print("Parking charge: Rs.", charge)
        print("Overnight fee: Rs.", overnight_fee)
        print("Penalty: Rs.", penalty)
        print("Total amount: Rs.", total)