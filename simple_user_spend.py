from aeternity import signing, node


def user_spend(user_id, amount):
    user_account = signing.Account.from_keystore(user_id + ".json", user_id)
    say_account = signing.Account.from_keystore("say.json", "ComplicatedIt123456")
    aeternity_cli = node.NodeClient(node.Config(
        external_url="https://sdk-testnet.aepps.com",
        network_id="ae_uat"
    ))

    tx = aeternity_cli.spend(user_account,
                             say_account.get_address(),
                             amount)
    print(f"https://testnet.explorer.aepps.com/#/tx/{tx.hash}")
    return tx.hash


user_spend("123456", 3000000000000000000)
