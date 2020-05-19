from pycoin.networks.bitcoinish import create_bitcoinish_network


network = create_bitcoinish_network(
    network_name="Mooncoin", symbol="MOON", subnet_name="main",
    wif_prefix_hex="83", sec_prefix="MOONSEC:", address_prefix_hex="3", pay_to_script_prefix_hex="32",
    bip32_prv_prefix_hex="0488ADE4", bip32_pub_prefix_hex="0488B21E", bech32_hrp="moon",
    magic_header_hex="f9f7c0e8", default_port=44664,
    dns_bootstrap=["dnsseed01.moonypool.com", "dnsseed02.moonypool.com", "dnsseed03.moonypool.com",])
	
	
