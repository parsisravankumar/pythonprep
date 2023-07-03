def convert_seconds(seconds):

    total_seconds = int(input("Enter the total number of seconds: "))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = (seconds % 3600) % 60
    return hours, minutes, remaining_seconds
    convert_seconds(total_seconds) == hours, minutes, seconds
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

