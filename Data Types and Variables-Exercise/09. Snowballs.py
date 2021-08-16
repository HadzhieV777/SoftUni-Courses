# 09. Snowballs
snowballs_cnt = int(input())

max_snowball_value = 0
max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0

for i in range (0, snowballs_cnt):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = str(input())

    snowball_value = (snowball_snow / snowball_time) ** float(snowball_quality)

    if snowball_value >= max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {max_snowball_value:.0f} ({max_snowball_quality})")