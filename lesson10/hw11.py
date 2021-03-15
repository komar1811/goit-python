from collections import UserDict


class AddressBook(UserDict):

        
    
    def add(self, record):
        account = {record.name:record.phones}
        self.data.update(account)


    def __str__(self): 
        result = []
        for key, value in self.data.items():
            result.append(f"Name: {key} - phones: {', '.join(value)}")
        return '\n'.join(result)


class Record:

    def __init__(self, name, *phones):

        self.name = name.value
        self.phones = []
        for phone in phones:
            self.phones += phone.value


class Field:

    def __init__(self, value):
        self.value = value



class Name(Field):
    pass


class Phone(Field):
    pass


    
