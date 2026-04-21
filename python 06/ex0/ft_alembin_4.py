import alchemy

print(alchemy.create_air())
try:
    print(alchemy.create_earth())
except Exception:
    print("Error, earth element not accessed")
