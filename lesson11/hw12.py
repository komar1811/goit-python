import re
from collections import UserDict
from datetime import datetime 


class AddressBook(UserDict):

    data = {}

    def add(self, record):
        account = {record.name:[record.phones, record.birthday]}
        self.data.update(account)

    def __str__(self): 
        result = []

        for key, value in self.data.items():
            birth = value[0].strftime(" %d/%m/%Y ")
            phone = ', '.join(value[1])
            result.append(f"Name: {key} - phones: {phone}, - birthday: {birth}")
        return '\n'.join(result)

    def __next__(self):
        keys = []
        counter = 0
        for key in self.data.keys():
            keys.append(key)
        if counter < len(keys):
            yield keys[counter], self.data(keys[counter])
            counter += 1
        raise StopIteration

    def __iter__(self):
        return AddressBook()

class Record:

    def __init__(self, name, birthday, *phones):

        self.birthday = Birthday(birthday).value
        self.name = Name(name).value
        self.phones = []
        for phone in phones:
            self.phones += Phone(phone).value
        
    def days_to_birthday (self):
        current_datetime = datetime.now()
        self.birthday = self.birthday.replace(year = current_datetime.year)
        if self.birthday >= current_datetime:
            result = self.birthday - current_datetime
        else:
            self.birthday = self.birthday.replace(year = current_datetime.year + 1)
            result = self.birthday - current_datetime
        return result.days

class Field:

    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value

class Name(Field):
    pass


class Phone(Field):

    def __setitem__(self, new_value):
        try:
            if re.match('^\+48\d{9}$', new_value):
                self.value = new_value
            else: 
                raise ValueError
        except ValueError:
            print('Incorrect phone number! Please provide correct phone number.')


class Birthday(Field):
    
    def __init__(self, value):
        self.value = datetime.strptime(value, "%d/%m/%Y")

    def __setitem__(self, new_value):
        try:
            if re.match('^\d{2}/\d{2}/\d{4}$', new_value):
                self.value = new_value
            else:
                raise ValueError
        except ValueError:
            print('Incorrect date! Please provide correct date format.')




