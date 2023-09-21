import time as Time

# get the seconds since epoch
seconds_since_epoch = Time.time()

# format the seconds with commas and 4 decimal places
formatted_seconds = f"{seconds_since_epoch:,.4f}"

# format the seconds in scientific notation
scientific_seconds = f"{seconds_since_epoch:.2e}"

# format the string with the time according to the pdf
formatted_time_string = (f"Seconds since January 1, 1970: {formatted_seconds}"
                         f" or {scientific_seconds} in scientific notation")

# convert to struct_time
converted_time = Time.localtime(seconds_since_epoch)

# format the date with abbreviated month, day of the month and the year
formatted_date = Time.strftime("%b %d %Y", converted_time)

# print the strings
print(formatted_time_string)
print(formatted_date)
