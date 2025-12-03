# NAME: Tanon Likhittaphong
# Student ID: 6710545547

from pathlib import Path

config = {}

choice = input("Load from 'file' or 'manual' input? ")

if choice == 'file':
    filename = input("Enter filename: ")
    if not Path(filename).exists():
        print(f"Error: File '{filename}' not found.")
        exit()
    with open(filename, 'r') as f:
        lines = f.readlines()

elif choice == 'manual':
    print("Enter configuration (type 'DONE' to finish):")
    lines = []
    while True:
        line = input()
        if line == 'DONE': break
        lines.append(line)
else:
    exit()

for line in lines:
    line = line.strip()
    if not line or line.startswith('#'): continue
    
    if '=' in line:
        key, val = line.split('=', 1)
        key, val = key.strip(), val.strip()
        
        if val.startswith('{') and val.endswith('}'):
            inner = {}
            for pair in val[1:-1].split(';'):
                if '=' in pair:
                    k, v = pair.split('=', 1)
                    inner[k.strip()] = v.strip()
            config[key] = inner
        elif ',' in val:
            config[key] = [item.strip() for item in val.split(',')]
        else:
            config[key] = val

if 'port' not in config or not str(config['port']).isdigit():
    print("Validation Error: Port must be an integer between 1 and 65535.")
    exit()

port = int(config['port'])
if port < 1 or port > 65535:
    print("Validation Error: Port must be an integer between 1 and 65535.")
    exit()

if 'allowed_users' not in config or not config['allowed_users']:
    print("Validation Error: Allowed users list must not be empty.")
    exit()

if 'database' not in config:
    print("Validation Error: Database dictionary must contain both 'user' and 'password' keys.")
    exit()

db = config['database']
if 'user' not in db or 'password' not in db:
    print("Validation Error: Database dictionary must contain both 'user' and 'password' keys.")
    exit()

if 'timeout' not in db or not str(db['timeout']).isdigit():
    print("Validation Error: Database timeout must be a positive integer.")
    exit()

timeout = int(db['timeout'])
if timeout <= 0:
    print("Validation Error: Database timeout must be a positive integer.")
    exit()

print("Configuration file is valid.")
print("Parsed Data:")
for key, value in config.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for k, v in value.items():
            print(f"   {k}: {v}")
    elif isinstance(value, list):
        print(f"{key}: {','.join(value)}")
    else:
        print(f"{key}: {value}")