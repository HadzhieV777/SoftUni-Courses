# 03. Capitals
country_names = [i for i in input().split(", ")]
capital_cities = [i for i in input().split(", ")]

new_dict = {country_names: capital_cities for country_names, capital_cities in zip(country_names, capital_cities)}

for key, value in new_dict.items():
    print(f"{key} -> {value}")