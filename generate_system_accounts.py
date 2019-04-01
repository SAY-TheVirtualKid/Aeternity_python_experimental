from aeternity import signing

say_account = signing.Account.generate()
say_account.save_to_keystore_file("say.json", "ComplicatedIt123456")
print("say account address: ", say_account.get_address())
