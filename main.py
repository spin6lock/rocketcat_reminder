#encoding:utf8
import config
import time
import random
import datetime
import rocketchat


def main():
    sleep_time = random.randint(config.randint_low, config.randint_high) 
    now = datetime.datetime.now()
    diff = datetime.timedelta(seconds=sleep_time)
    future = now + diff
    print(f"sleep for {sleep_time}, about {future}")
    time.sleep(sleep_time)
    response = rocketchat.send_msg(config.channel, config.text, config.emoji, config.alias)
    if response:
        print("Success!")
    else:
        raise Exception(f"Non-success status code: {response.status_code}")

if __name__ == "__main__":
    main()
