import subprocess, time

while 1:
    print("Lock'n'load, dank bot is starting..\n")

    subprocess.run("python3.5 ~/greenoznique/bot.py", shell = True)

    print("\n\n--- Bot has crashed, restarting in 10 seconds ---\n\n")

    time.sleep(10)