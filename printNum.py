
import ourModule

if __name__ == "__main__":
    results = ourModule.getNumbers(5,9)
    print(results)

from datetime import timedelta, date
delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

today = date.today() #comments
print("Today's date:", today)
