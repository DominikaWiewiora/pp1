from contact import Contact
from contact_list import Contact_List
smartphone_contacts = Contact_List()
contact1 = Contact("John Brown", "brown@onet.pl", "555234000")
contact2 = Contact("Anna May", "am@o2.pl", "232000199")
contact3 = Contact("George Small", "smallg@google.pl", "222999100")
contact4 = Contact("Paola Big", "bigpaola@poczta.pl", "100200300")
smartphone_contacts.add_contact(contact1)
smartphone_contacts.add_contact(contact2)
smartphone_contacts.add_contact(contact3)
smartphone_contacts.add_contact(contact4)
smartphone_contacts.display_contacts()
