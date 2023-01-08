import os

# Get a list of all the installed applications on the device
app_list = []
for root, dirs, files in os.walk(r'C:\Program Files'):
    for file in files:
        if file.endswith('.exe') and 'LastPass' in file:
            app_list.append(file)

# Sort the list of applications alphabetically
app_list.sort()

# Open a file for writing
with open('installed_apps.txt', 'w') as file:
    # Write a bullet point for each application
    for app in app_list:
        file.write('- ' + app + '\n')

# Print the list of applications to the console
for app in app_list:
    print('- ' + app)
