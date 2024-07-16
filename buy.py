import random
from raydium_sdk import buy_token, sell_token
from solana.rpc.api import Client, Keypair
from solana.rpc.async_api import AsyncClient

RPC = "https://mainnet.helius-rpc.com/?api-key=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
async_solana_client = AsyncClient(RPC)
solana_client = Client(RPC)

token = input("Enter token address to start buying:")

min_sol = 0.01 # Minimum amount of SOL to buy
max_sol = 1 # Maximum amount of SOL to buy

min_delay = 1 # Minimum delay between buys (in seconds)
max_delay = 5 # Maximum delay between buys (in seconds)

keypairs = open("keypairs.txt").read().splitlines()
for key in keypairs:
    keypair = Keypair.from_base58_string(key)

    amount = random.uniform(min_sol, max_sol)

    buy_tx = buy_token(
        solana_client,
        async_solana_client,
        token,
        keypair,
        amount,
    )

    print(f"[+] [{key[:6]}] Bought {amount} SOL of {token}: https://solscan.io/tx/{buy_tx}")
    time.sleep(random.randint(min_delay, max_delay))
