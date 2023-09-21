lmonth = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    prio_date = input("Date: ").strip()
    if "," in prio_date:
        prio_date = prio_date.replace(",", "")
        outlist = prio_date.split(" ")
        for item in outlist:
            if item == "":
                outlist = [item for item in outlist if item != ""]
        if outlist[0].title() in lmonth:
            month_index = lmonth.index(outlist[0].title())
            day = int(outlist[1])
            if (month_index + 1) <= 12:
                if day <= 31:
                    print(f"{outlist[2]}-{month_index+1:02}-{day:02}")
                    break
                else:
                    pass
            else:
                pass
        else:
            pass
    elif "/" in prio_date:
        outlist = prio_date.split("/")
        if outlist[0].isdigit():
            month = int(outlist[0])
            day = int(outlist[1])
            if month <= 12:
                if day <= 31:
                    print(f"{outlist[2]}-{month:02}-{day:02}")
                    break
                else:
                    pass
            else:
                pass
        else:
            pass
    elif prio_date.isdigit() is False:
        outlist = prio_date.split(" ")
        for item in outlist:
            if item == "":
                outlist = [item for item in outlist if item != ""]
        if outlist[0].title() in lmonth:
            month_index = lmonth.index(outlist[0].title())
            day = int(outlist[1])
            if (month_index + 1) <= 12:
                if day <= 31:
                    print(f"{outlist[2]}-{month_index+1:02}-{day:02}")
                    break
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
