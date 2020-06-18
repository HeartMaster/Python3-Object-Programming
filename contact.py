# ¶àÖØ¼Ì³Ð »ìÈë

class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest


class ContactList(list):
    def search(self,name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self,name,email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)


class Supper(Contact):
    def order(self,order):
        print(order,self.name)


class AddressHolder:
    def __init__(self,street,city,state,code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact,AddressHolder):
    def __init__(self,name,email,phone,street,city,state,code):
        Contact().__init__(name,email)
        AddressHolder().__init__(street,city,state,code)
        self.phone = phone


class MailSender:
    def send_mail(self,message):
        print(self.email)


class EmailableContact(Contact,MailSender):
    pass




