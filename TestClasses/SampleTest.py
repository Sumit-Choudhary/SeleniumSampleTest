from PageClasses import loginPopUp


def login():
    loginPopUp.flipkartMainLoginPopOver.loadFlipKart()
    loginPopUp.flipkartMainLoginPopOver.loginToFlipKart('8939667714', 'cometome.12')


class ValidateFlipKartLogin:

    def __init__(self):
       self.loginPopUp = loginPopUp




