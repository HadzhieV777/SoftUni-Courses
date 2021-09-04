# 03. Extract File
path_data = input().split('\\')

for index in range(0, len(path_data)):

    file_info = path_data[index - 1]
    file_name = file_info.split(".")[0]
    file_extension = file_info.split(".")[1]

    print(f'File name: {file_name}')
    print(f'File extension: {file_extension}')

    break