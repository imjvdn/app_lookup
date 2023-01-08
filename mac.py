import os
import subprocess

# Get a list of all the installed applications on the device
output = subprocess.run(['/usr/bin/mdfind', 'kMDItemContentTypeTree=com.apple.application-bundle'],
                        stdout=subprocess.PIPE).stdout.decode('utf-8')
app_list = output.strip().split('\n')

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
