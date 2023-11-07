# Partie 1
class Phone:
    
    def __init__(self, number_arg):
        self.number = number_arg
        
        
class Email:
    
    def __init__(self, mail_adress_arg):
        self.mail_adress = mail_adress_arg
        

# Partie 2   
class RegisterSystem:
    
    def _register_with_phone(self, phone:Phone):
        print(f"Un code de vérification a été envoyé au {phone.number}")
        
    def _regiter_with_mail(self, mail:Email):
        print(f"Un mail de confirmation a été envoyé à votre adresse mail: {mail.mail_adress}")
        
    def register(self, contact_info):
        if isinstance(contact_info, Phone):
            self._register_with_phone(contact_info)
        elif isinstance(contact_info, Email):
            self._regiter_with_mail(contact_info)
        else:
            print("Objet de classe non reconnue")

phone1 = Phone("0606060606")
mail1 = Email("mail@something.com")
system = RegisterSystem()


system.register(phone1)
system.register(mail1)