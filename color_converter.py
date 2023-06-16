### HEX to RGB Color Converter

# program input
color = input()
color_list = list(color)

# get hexadecimal values and transformation
first_value = ''.join(color_list[1:3])
first_value = int(first_value, 16)

second_value = ''.join(color_list[3:5])
second_value = int(second_value, 16)

third_value = ''.join([ color_list[-2], color_list[-1]])
third_value = int(third_value, 16)

# programa output
print(f"R: {first_value} G: {second_value} B: {third_value}")
