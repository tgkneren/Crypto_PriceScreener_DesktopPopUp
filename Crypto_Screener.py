import tkinter as tk
import requests

#Coins to be tracked (name, network, and address information).
pairs = [
    {"name": "uro", "chain": "solana", "pair_address": "3hsdbmfsich3ycsxofjgx4tvpxecsue9nrmgvaoyveqt"},
    {"name": "$rif", "chain": "solana", "pair_address": "a8inixg97ajk5kcxtdi5oodg2drkeebpnw2ghchpe4j1"},
    {"name": "roy", "chain": "avalanche", "pair_address": "0x86783a149fe417831ae8c59dd0e2b60664a3dfd1"},
    {"name": "boop", "chain": "arbitrum", "pair_address": "0x184fb097196a4e2be8dfd44b341cb7d13b41ea7e"},
    {"name": "kek", "chain": "solana", "pair_address": "csfpb7rhgn2vca72rfvvvfu4sfhyxqbqfny3pvtpmij3"},
    {"name": "cheems", "chain": "bsc", "pair_address": "0x38231d4ef9d33ebea944c75a21301ff6986499c3"},
    {"name": "fart", "chain": "solana", "pair_address": "bzc9nzfmqkxr6fz1dbph7bdf9broyef6pnzesp7v5iiw"},
    {"name": "bnb", "chain": "bsc", "pair_address": "0x172fcd41e0913e95784454622d1c3724f546f849"},
    {"name": "trenches", "chain": "solana", "pair_address": "8a9f1trenkznnx885ajfnoz5wjttadskzhean5ee6gjt"},


]

root = tk.Tk()
root.title("Fiyat Takibi")
root.geometry("300x200+1000+500")
root.resizable(False, False)

#The window always stays on top, even if you click elsewhere
root.attributes("-topmost", True)

#Making the window semi-transparent
root.attributes("-alpha", 0.75)  # Transparency: 0.0 fully transparent, 1.0 fully opaque

output_label = tk.Label(
    root,
    text="",
    justify="left",
    anchor="nw",
    font=("Arial", 10),
    bg="black",
    fg="white"
)
output_label.pack(fill="both", expand=True)


def update_prices():
    prices = []
    for pair in pairs:
        try:
            url = f"https://api.dexscreener.com/latest/dex/pairs/{pair['chain']}/{pair['pair_address']}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                price = float(data["pair"]["priceUsd"])
                prices.append(f"{pair['name']}: {price:.10f} $")
            else:
                prices.append(f"{pair['name']}: API Hatası")
        except Exception as e:
            prices.append(f"{pair['name']}: Hata")

    output_label.config(text="\n".join(prices))

    #update every 60 seconds
    root.after(60000, update_prices)

update_prices()

root.mainloop()
r