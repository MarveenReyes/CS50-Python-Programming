def main():
    hours = convert(input("What time is it? "))
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <= 13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")
    

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    total = hours + (minutes/60)
    return total


if __name__ == "__main__":
    main()
