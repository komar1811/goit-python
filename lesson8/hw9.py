from datetime import datetime, timedelta

WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def get_current_week():
    now = datetime.now()
    current_weekday = now.weekday()
    if current_weekday < 5:
        week_start = now - timedelta(days = 2 + current_weekday)
    else:
        week_start = now - timedelta(days = current_weekday - 5)
    return [week_start.date(), week_start.date() + timedelta(days = 7)]
    
    

def congratulate(users):
    current_year = datetime.now().year
    congratulate = {'Monday': [],'Tuesday':[],'Wednesday':[],'Thursday':[],'Friday':[]}
    for user in users:
        new_birthday = user['birthday'].replace(year = current_year)
        birthday_weekday = new_birthday.weekday()
        if get_current_week()[0] <= new_birthday.date() < get_current_week()[1]:
            if birthday_weekday < 5:
                congratulate[WEEKDAYS[birthday_weekday]].append(user['name'])
            else:
                congratulate['Monday'].append(user['name'])
    for key, value in congratulate.items():
        if len(value):
            print(f"{key}: {' '.join(value)}")
        



congratulate([{'name':'Mike', 'birthday':datetime(year = 1989,month = 2, day = 23)},
              {'name':'Julia', 'birthday':datetime(year = 1970,month = 2, day = 20)},
              {'name':'Andrij', 'birthday':datetime(year = 1958,month = 11, day = 24)}])
    
