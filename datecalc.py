import datetime

def caldate(dob):
    dob = datetime.datetime.strptime(dob, '%Y-%m-%d')
    vac1date = dob + datetime.timedelta(days=30)
    vac2date = dob + datetime.timedelta(days=60)
    vac3date = dob + datetime.timedelta(days=90)
    return vac1date, vac2date, vac3date

l = caldate('2023-02-28')
for i in l:

    print(i.date())