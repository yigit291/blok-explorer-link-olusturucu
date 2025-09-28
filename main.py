# Bu script, popüler block explorer'lar için hızlıca link oluşturur.
# Hiçbir ek kütüphane gerektirmez.

def create_etherscan_link(address):
    """Verilen Ethereum adresi için Etherscan linki oluşturur."""
    base_url = "https://etherscan.io/address/"
    return base_url + address

def create_blockchain_com_link(tx_hash):
    """Verilen Bitcoin işlem hash'i için Blockchain.com linki oluşturur."""
    base_url = "https://www.blockchain.com/btc/tx/"
    return base_url + tx_hash

if __name__ == "__main__":
    print("--- Blok Explorer Link Oluşturucu ---")

    # Örnek bir Ethereum adresi (Vitalik Buterin'in adresi)
    eth_wallet_address = "0xde0B295669a9FD93d5F28D9Ec85E40f4cb697BAe"
    etherscan_link = create_etherscan_link(eth_wallet_address)
    print(f"\nEthereum Cüzdan Linki:")
    print(etherscan_link)

    # Bitcoin Genesis (ilk) bloğunun işlem hash'i
    btc_transaction_hash = "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16"
    blockchain_com_link = create_blockchain_com_link(btc_transaction_hash)
    print(f"\nBitcoin İşlem Linki:")
    print(blockchain_com_link)