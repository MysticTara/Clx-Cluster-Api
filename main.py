import requests
import random
import string
import time

print("""MYTSYTIC""")
print("""starting up... """)
time.sleep(5)
print("""processing stufffff """)
time.sleep(2)
print("Nitro Checker")
time.sleep(0.3)
print("")
time.sleep(0.2)

num = int(input('Input How Many Codes to Generate and Check: '))

with open("Cluster Api.txt", "w", encoding='utf-8') as file:
    print("Your nitro codes are being generated, BETTER BE PATIENT")

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"cluster@import.llx://NeyoGolden:neji@webupt.vhkov.cluster.neyo.//{code}\=newcode.clx\n")

    print(f"Generated {num} codes | Time taken: {time.time() - start}\n")

with open("Cluster Api.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f" Invalid | {nitro} ")
            break
        else:
            print(f" Valid | {nitro} ")

input("\nend")
