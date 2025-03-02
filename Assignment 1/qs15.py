with open("INDIA.txt", "r") as file:
    r = file.readlines()

line_num = int(input("Enter the specific number of line you want to remove: "))

if 1 <= line_num <= len(r):
    del r[line_num - 1]  # Remove the specified line

# Write the updated content back to the file
with open("INDIA.txt", "w") as file:
    file.writelines(r)

print("Updated content:", r)
