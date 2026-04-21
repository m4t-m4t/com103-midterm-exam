# ROOM MONITOR NAME (letters only, NO SPACES)
while True:
    monitor_name = input("Room monitor name: ")

    valid = True

    if monitor_name == "":
        valid = False
    else:
        for ch in monitor_name:
            if not (("A" <= ch <= "Z") or ("a" <= ch <= "z")):
                valid = False

    if valid:
        break
    else:
        print("Invalid! Name must be letters only (no spaces).\n")


# ROOM NUMBER (letters + numbers only, NO SPACES, NO SYMBOLS)
while True:
    room_number = input("Room number: ")

    valid = True

    if room_number == "":
        valid = False
    else:
        for ch in room_number:
            if not (("A" <= ch <= "Z") or ("a" <= ch <= "z") or ("0" <= ch <= "9")):
                valid = False

    if valid:
        break
    else:
        print("Invalid! No spaces or symbols allowed.\n")
        
# CHORE LIST
chore_names = [
    "Sweeping / Mopping",
    "Dishwashing",
    "Taking Out Trash",
    "Cleaning Bathroom",
    "Buying Groceries"
]

chore_freq = [
    "Daily",
    "After meals",
    "Every other day",
    "Weekly",
    "Weekly"
]

print("\n==========================================")
print("   DORM ROOM -- CHORE LIST")
print("==========================================")

for i in range(5):
    print(f" {i+1}. {chore_names[i]:<22} [{chore_freq[i]}]")

print("==========================================\n")


assigned_chores = []
assigned_names = []
assigned_status = []

completed = 0
total_assigned = 0