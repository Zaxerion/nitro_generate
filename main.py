import requests
import random
import string
import time
import background

repeat_count = 0

background.keep_alive()

while True:
    num = int(10)
    valid_codes = []

    print(f"Generated {num} codes\n")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=16
        ))

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\nValid | {code}\n\n")
            valid_codes.append(code)
        else:
            print(f"*", end="")

    with open("valid.txt", "a") as valid_file:
        for code in valid_codes:
            valid_file.write(f"https://discord.gift/{code}\n")

    repeat_count += 1
    print(f"\n\n--- Program repeated {repeat_count} times ---\n\n")

    time.sleep(0.1)  # 5-second delay before repeating the loop
