class ContactList(list):
    def search(self, name):
        '''Return all contacts that contain the search value in their name.'''

        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts



class Contact:
    '''all_contacts = ContactList()     # Class Variable, it's shared by all instances of this class


    def __init__(self, name, email):
        self.name = name 
        self.email = email 
        Contact.all_contacts.append(self)'''

    all_contacts = []

    def __init__(self, name='', email='', **kwargs):
        super.__init__(**kwargs)
        self.name = name
        self.email = email
        self.all_contacts.append(self)

class Supplier(Contact):
    def order(self, order):
        print("If this were a real system we would send ", "{} order to {}".format(order, self.name))





class MailSender:
    def send_mail(self, message):
        print("Sending mail to " + self.email)


class EmailableContact(Contact, MailSender):
    pass


class AddressHolder:
    '''def __init__(self, street, city, state, code):
        self.street = street
        self.city = city
        self.state = state
        self.code = code'''

    def __init__(self, street='', city='', state='', code='', **kwargs):
        super.__init__(**kwargs)
        self.street = street
        self.city = city
        self.state = state
        self.code = code


class Friend(Contact, AddressHolder):
    '''def __init__(self, name, email, phone, street, city, state, code):
        Contact.__init__(self, name, email)
        AddressHolder.__init__(self, street, city, state, code)
        self.phone = phone '''

    def __init__(self, phone='', **kwargs):
        super.__init__(**kwargs)
        self.phone = phone



