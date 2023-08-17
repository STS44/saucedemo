from faker import Faker


def get_rand_first_name():
    return Faker().first_name()


def get_rand_last_name():
    return Faker().last_name()


def get_rand_postcode():
    return Faker().postcode()
