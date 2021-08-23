# 06. Electron Distribution
total_electrons = int(input())

electrons_config = []
current_layer = 1

while total_electrons > 0:
    current_layer_electrons = 2 * pow(current_layer, 2)

    if total_electrons >= current_layer_electrons:
        electrons_config.append(current_layer_electrons)
    else:
        electrons_config.append(total_electrons)

    total_electrons -= current_layer_electrons
    current_layer += 1

electrons_config_str = [str(layer) for layer in electrons_config]
print(f"[{', '.join(electrons_config_str)}]")