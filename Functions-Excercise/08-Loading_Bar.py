# 08. Loading Bar
def loading(percent):
    if percent >= 10:
        return percent // 10
    else:
        return percent


def remaining(rem):
    return 10 - rem


percents_input = int(input())

if loading(percents_input) == 10:
    print(f"{percents_input}% Complete!")
    print("[" + (loading(percents_input) * '%') + (remaining(loading(percents_input)) * '.') + "]")
else:
    print(str(percents_input) + '%' + ' ', end='')
    print("[" + (loading(percents_input) * '%') + (remaining(loading(percents_input)) * '.') + "]")
    print('Still loading...')