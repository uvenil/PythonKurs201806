from rdoclient import RandomOrgClient
r = RandomOrgClient(YOUR_API_KEY_HERE)
r.generate_integers(5, 0, 10)

print(r)
