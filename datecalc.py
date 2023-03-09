import datetime

def caldate(dob):
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    vac1date = dob + datetime.timedelta(days=42)
    vac2date = dob + datetime.timedelta(days=70)
    vac3date = dob + datetime.timedelta(days=98)
    return vac1date.date(), vac2date.date(), vac3date.date()
