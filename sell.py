import random
from raydium import buy_token, sell_token
from solana.rpc.api import Client, Keypair
from solana.rpc.async_api import AsyncClient

RPC = "https://mainnet.helius-rpc.com/?api-key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
async_solana_client = AsyncClient(RPC)
solana_client = Client(RPC)

token = input("Enter token address to start selling:")

min_delay = 1 # Minimum delay between sells (in seconds)
max_delay = 5 # Maximum delay between sells (in seconds)

keypairs = open("keypairs.txt").read().splitlines()
for key in keypairs:
    keypair = Keypair.from_base58_string(key)

    sell_tx = sell_token(
        solana_client, 
        async_solana_client, 
        token,
        keypair
        None,
    ) 
    
    print(f"[+] [{key[:6]}] Sold {token}: https://solscan.io/tx/{sell_tx}")
    time.sleep(random.randint(min_delay, max_delay))