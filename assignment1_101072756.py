"""
Author: Mohammad Akib shaikh
Assignment: #1
"""



gym_member = "Alex Alliton"
preferred_weight_kg = 20.5
highest_reps = 25
membership_active = True

workout_stats = {
    "Alex": (45, 30, 35),
    "Jamie": (50, 40, 30),
    "Taylor": (25, 60, 45),
    "Jordan": (35, 35, 40)
}

for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

print("Updated workout_stats with totals:")
for key, value in workout_stats.items():
    print(f"  {key}: {value}")

workout_list = []
for friend in ["Alex", "Jamie", "Taylor", "Jordan"]:
    workout_list.append(list(workout_stats[friend]))

print("\n2D workout_list (yoga, running, weightlifting):")
for row in workout_list:
    print(row)

print("\nYoga and running minutes for all friends:")
for i, row in enumerate(workout_list):
    yoga_running = row[:2]
    print(f"Friend {i+1}: {yoga_running}")

print("\nWeightlifting minutes for the last two friends:")
last_two_weightlifting = [row[2] for row in workout_list[-2:]]
print(last_two_weightlifting)

print("\n--- Active friends (total >= 120 minutes) ---")
for friend in ["Alex", "Jamie", "Taylor", "Jordan"]:
    total_key = f"{friend}_Total"
    if total_key in workout_stats and workout_stats[total_key] >= 120:
        print(f"Great job staying active, {friend}!")

print("\n--- Friend Lookup ---")
user_input = input("Enter a friend's name: ").strip()

if user_input in workout_stats and isinstance(workout_stats[user_input], tuple):
    minutes = workout_stats[user_input]
    total = workout_stats[f"{user_input}_Total"]
    print(f"{user_input}'s workout minutes:")
    print(f"  Yoga: {minutes[0]} min")
    print(f"  Running: {minutes[1]} min")
    print(f"  Weightlifting: {minutes[2]} min")
    print(f"  Total: {total} min")
else:
    print(f"Friend {user_input} not found in the records.")

friend_names = ["Alex", "Jamie", "Taylor", "Jordan"]
totals = [workout_stats[f"{name}_Total"] for name in friend_names]

max_total = max(totals)
min_total = min(totals)
max_friends = [friend_names[i] for i, val in enumerate(totals) if val == max_total]
min_friends = [friend_names[i] for i, val in enumerate(totals) if val == min_total]

print("\n--- Highest and Lowest Total Minutes ---")
print(f"Friend(s) with highest total ({max_total} min): {', '.join(max_friends)}")
print(f"Friend(s) with lowest total ({min_total} min): {', '.join(min_friends)}")
