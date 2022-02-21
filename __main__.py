
def restart():
    from pdb import Restart
    import phonenumbers
    import time
    print("     ")
    print("------------------------")
    print("Enter Number with Counrty Code ")
    print("Example: +97255667788 ")
    print("------------------------")
    print("     ")


    number = input("")

    from phonenumbers import geocoder

    IL_nmber = phonenumbers.parse(number, "IL")
    print(geocoder.description_for_number(IL_nmber, "en"))

    from phonenumbers import carrier
    service_nmber = phonenumbers.parse(number, "RO")
    print(carrier.name_for_number(service_nmber, "en"))
    restart()
restart()
