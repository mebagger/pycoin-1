from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    network_name="Mooncoin Testnet", symbol="MOONT", subnet_name="test",
    wif_prefix_hex="F1", sec_prefix="MOONTSEC:", address_prefix_hex="113", pay_to_script_prefix_hex="32",
    bip32_prv_prefix_hex="04358394", bip32_pub_prefix_hex="043587CF", bech32_hrp="moont",
    magic_header_hex="f3d2c8f1", default_port=14664,
    dns_bootstrap=["testnet-seed01.moonypool.com", "testnet-seed02.moonypool.com"])
	
	