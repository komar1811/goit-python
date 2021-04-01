from collections import UserDict
from datetime import datetime 
from pickle import dump, load
import re


class AddressBook(UserDict):

    def __init__(self):
        self.data = {}
        self.counter = -1

    def __str__(self): 
        result = []

        for key, value in self.data.items():
            birth = value[1].strftime("%d/%m/%Y")
            if value[0]:
                new_value = []
                for number in value[0]:
                    if number:
                        new_value.append(number)
                phone = ', '.join(new_value)
            result.append(f"Name: {key} - phones: {phone} - birthday: {birth}")
        return '\n'.join(result)

    def __next__(self):
        keys = list(self.data.keys())
        self.counter += 1

        if self.counter == len(keys):
            self.counter = -1
            raise StopIteration
        result = f"{keys[self.counter]}:{self.data[keys[self.counter]]}"
        return result

    def __iter__(self):
        return self

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        return self.data[key]

    def add(self, record):
        account = {record.name:[record.phones, record.birthday]}
        self.data.update(account)

    def save(self, file_name):
        with open(file_name, 'wb') as file:
            dump(self.data, file_name)

    def load(self, file_name):
        with open(file_name, 'rb') as file:
            unpacked_data = load(file_name)
        return unpacked_data

    def search(self, pattern):
        keys = list(self.data.keys())
        values = list(self.data.values())
        result = ""
        for key in keys:
            if key.lower().startswith(pattern.lower()):
                result += f"{keys[keys.index(key)]}:{self.data[keys[keys.index(key)]][0]}\n"
        for key, item in self.data.items():
            for number in item[0]:
                if number.lower().startswith(pattern.lower()):
                    result += f"{keys[keys.index(key)]}:{self.data[keys[keys.index(key)]][0]}\n"
        return result
       
            


class Record:

    def __init__(self, name, birthday, *phones):

        self.birthday = Birthday(birthday).value
        self.name = Name(name).value
        self.phones = []
        for phone in phones:
            self.phones.append(Phone(phone).value)
        
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
    
    def __init__(self, value):
        try:
            if re.match('^\+48\d{9}$', value):
                self.value = value
            else: 
                raise ValueError
        except ValueError:
            self.value = ""
            print('Incorrect phone number! Please provide correct phone number.')

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

