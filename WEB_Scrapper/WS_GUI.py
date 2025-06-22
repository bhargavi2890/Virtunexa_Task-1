import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
from bs4 import BeautifulSoup
import csv
import json

def scrape_website(url, tag, class_name, output_box):
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch URL:\n{e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    if class_name:
        elements = soup.find_all(tag, class_=class_name)
    else:
        elements = soup.find_all(tag)

    if not elements:
        messagebox.showinfo("No Results", f"No <{tag}> elements found with class '{class_name}'")
        return

    data = []
    output_box.delete('1.0', tk.END)  # Clear previous output
    for el in elements:
        text = el.get_text(strip=True)
        if text:
            data.append({'tag': tag, 'text': text})
            output_box.insert(tk.END, f"<{tag}>: {text}\n")

    # Save to CSV
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['tag', 'text'])
        writer.writeheader()
        writer.writerows(data)

    # Save to JSON
    with open('scraped_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Success", f"Scraped {len(data)} elements.\nSaved to scraped_data.csv and scraped_data.json.")

def main():
    window = tk.Tk()
    window.title("Web Scraper GUI")
    window.geometry("600x600")

    tk.Label(window, text="Website URL:").pack(pady=5)
    url_entry = tk.Entry(window, width=70)
    url_entry.pack()

    tk.Label(window, text="HTML Tag (e.g., h1, p, a):").pack(pady=5)
    tag_entry = tk.Entry(window, width=70)
    tag_entry.pack()

    tk.Label(window, text="Class Name (optional):").pack(pady=5)
    class_entry = tk.Entry(window, width=70)
    class_entry.pack()

    output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20)
    output_box.pack(pady=10)

    scrape_button = tk.Button(
        window, 
        text="Scrape Website", 
        command=lambda: scrape_website(url_entry.get(), tag_entry.get(), class_entry.get(), output_box)
    )
    scrape_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
