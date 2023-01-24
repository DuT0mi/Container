class Time:
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0
    second = 0
    def setYear(self,pYear) -> None:
        if pYear >= 2023:
            self.year = pYear
        else:
            assert(pYear < 2023),"Invalid Date"

    def __init__(self,pYear,pMonth,pDay,pHour,pMinute,pSecond) -> None:
        self.setYear(pYear)
    # ...
        