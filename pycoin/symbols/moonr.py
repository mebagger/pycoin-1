from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    network_name="Mooncoin", symbol="MOONR", subnet_name="regtest",
    wif_prefix_hex="EE", sec_prefix="MOONRSEC:", address_prefix_hex="112", pay_to_script_prefix_hex="39",
    bip32_prv_prefix_hex="04358394", bip32_pub_prefix_hex="043587CF", bech32_hrp="moonr",
    magic_header_hex="f5d6c4f7", default_port=13664,
    dns_bootstrap=["10.0.0.132"])
	
	
	