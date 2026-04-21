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


# CHORE INPUT (must be number only)
for i in range(4):
    print(f"--- CHORE {i+1} ---")

    while True:
        chore_input = input("Chore number (0 to skip): ")

        valid = True

        if chore_input == "":
            valid = False
        else:
            for ch in chore_input:
                if not ("0" <= ch <= "9"):
                    valid = False

        if valid:
            chore_num = int(chore_input)
            break
        else:
            print("Invalid input! Numbers only.")

    if chore_num == 0:
        print()
        continue

    if 1 <= chore_num <= 5:
        name = input("Roommate name: ")
        status = input("Status (done/not done): ")

        assigned_chores.append(chore_num)
        assigned_names.append(name)
        assigned_status.append(status)

        total_assigned += 1

        if status == "done":
            completed += 1

    print()


# COMPUTE
if total_assigned > 0:
    rate = (completed * 100) // total_assigned
else:
    rate = 0


# STATUS
if rate == 100:
    room_status = "ROOM IS SPOTLESS!"
elif rate >= 50:
    room_status = "ALMOST THERE!"
else:
    room_status = "NEEDS CATCHING UP!"


# OUTPUT
print("=============================================")
print(f"     ROOM {room_number} -- WEEKLY CHORE REPORT")
print("=============================================")
print(f"Room Monitor : {monitor_name}")
print("---------------------------------------------")

for i in range(len(assigned_chores)):
    index = assigned_chores[i] - 1

    print(f"[{i+1}] {chore_names[index]:<22} [{chore_freq[index]}]")
    print(f"    Roommate : {assigned_names[i]}")
    print(f"    Status   : {assigned_status[i]}\n")

print("---------------------------------------------")
print(f"Completed      : {completed} out of {total_assigned} assigned")
print(f"Completion Rate: {rate}%")
print(f"Room Status    : {room_status}")
print("=============================================")
