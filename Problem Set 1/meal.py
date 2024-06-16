def main():
    time = input("What time is it? ")
    time = convert(time)
    if 8.0 >= time >= 7.0:
        print("breakfast time")
    elif 13.0 >= time >= 12.0:
        print("lunch time")
    elif 19.0 >= time >= 18.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours) + (float(minutes) / 60)
    return hours

if __name__ == "__main__":
    main()
