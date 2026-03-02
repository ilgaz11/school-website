from datetime import datetime, date


#get real date
now = datetime.now()
today = now.strftime("%b %d, %Y")
month = now.month
year = now.year

#assign semester string
if month > 7:
    semester = "Fall"
elif month > 5:
    semester = "Summer"
else:
    semester = "Winter"

#get semester end and start date
end_dates = {"Fall": f"Dec 18, {year}", "Winter": f"May 1, {year}", "Summer": f"Jul 31, {year}"}
start_dates = {"Fall": f"Aug 27, {year}", "Winter": f"Jan 5, {year}", "Summer": f"Jun 15, {year}"}

dates = {"today": today, "sem_end": end_dates[semester], "sem_start": start_dates[semester]}


if __name__ == "__main__":
    print(today)
    print(dates["sem_end"])
    