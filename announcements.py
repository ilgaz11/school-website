from datetime import datetime, date



now = datetime.now()
today = now.strftime("%B %d, %Y")

dates = {"today": today}


if __name__ == "__main__":
    print(today)