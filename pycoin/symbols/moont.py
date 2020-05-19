from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    symbol="MOONT", network_name="Mooncoin", subnet_name="test",
    wif_prefix_hex="F1",  address_prefix_hex="71", pay_to_script_prefix_hex="C4",
    bip32_prv_prefix_hex="04358394", bip32_pub_prefix_hex="043587CF", bech32_hrp="moont",
    magic_header_hex="f3d2c8f1", default_port=14664,
    dns_bootstrap=["testnet-seed01.moonypool.com"],
	)
	
	