import datetime

def seconds_to_mm_ss(seconds):
    td = datetime.timedelta(seconds=seconds)
    return str(td)[-5:]

# Example usage:
total_seconds = 153
formatted_time = seconds_to_mm_ss(total_seconds)
print(f"{total_seconds} seconds is {formatted_time}")