#!/usr/bin/python3
line1 = "#!/usr/bin/python3"
import os
for file in os.listdir('.'):
    if file.endswith('.py') and os.path.isfile(file):
        with open(file, 'a') as f:
            f.write(line1 + '\n')

#!/usr/bin/python3
#!/usr/bin/python3
#!/usr/bin/python3
#!/usr/bin/python3
#!/usr/bin/python3
