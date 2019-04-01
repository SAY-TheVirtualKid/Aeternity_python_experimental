from aeternity import signing


def check_user_has_ae_account(user_id):
    return False


def create_aeternity_account(user_id):
    if check_user_has_ae_account(user_id):
        return 0
    aeternity_account = signing.Account.generate()
    aeternity_account.save_to_keystore_file(user_id + ".json", user_id)
    print("User account private key: ", aeternity_account.get_address())
    return aeternity_account.get_address()
