# Today let's interact with another application from python
# We will use the builtin 'subprocess' module

import subprocess

# Our command is what you would normally type in the command line as a list
# Let's find docker version as an example
command = ['docker', '--version']
docker_subprocess = subprocess.run(command, stdout=subprocess.PIPE)

# Lets see the output 

print(docker_subprocess.stdout.decode("utf-8"))
# Output >>> Docker version 20.10.14, build a224086
