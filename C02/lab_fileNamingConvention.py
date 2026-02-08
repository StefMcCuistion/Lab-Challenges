project_name = input("What is the project name? ")
asset_name = input("What is the asset name? ")
file_type = input("What is the file type? ")
description = input("What is the description? ")
version = input("What is the version number? ")
file_extension = input("What is the file extension? ")
final_filename = f"{project_name}_{asset_name}_{file_type}_\
{description}_v{version}.{file_extension}"
print(final_filename)
