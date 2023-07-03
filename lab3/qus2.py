#Write a program to convert the given seconds into hours – minutes – seconds.
total_seconds = int(input("Enter the total number of seconds: "))
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = (seconds % 3600) % 60
    return hours, minutes, remaining_seconds

# Example usage:
hours, minutes, seconds = convert_seconds(total_seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

