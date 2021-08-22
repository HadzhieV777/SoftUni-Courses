# 02. Next Version
software_version = [str(el) for el in input().split(".")]
software_version_str = str("".join(software_version))
print(".".join(str(int(software_version_str) + 1)))