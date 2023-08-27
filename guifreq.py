import tkinter as tk
from tkinter import messagebox

# Conversion factors
conversion = {
    "hz_to_khz": 0.001,
    "hz_to_mhz": 0.000001,
    "hz_to_ghz": 0.000000001,
    "khz_to_hz": 1000,
    "khz_to_mhz": 0.001,
    "khz_to_ghz": 0.000001,
    "mhz_to_hz": 1000000,
    "mhz_to_khz": 1000,
    "mhz_to_ghz": 0.001,
    "ghz_to_hz": 1000000000,
    "ghz_to_khz": 1000000,
    "ghz_to_mhz": 1000,
}

# Create the tkinter window
window = tk.Tk()
window.title("Frequency Converter")

# Frequency label and entry field
freq_label = tk.Label(window, text="Enter the frequency:")
freq_label.pack()
freq_entry = tk.Entry(window)
freq_entry.pack()

# Current unit label and entry field
from_unit_label = tk.Label(window, text="Enter the current unit (Hz, kHz, MHz, GHz):")
from_unit_label.pack()
from_unit_entry = tk.Entry(window)
from_unit_entry.pack()

# Desired unit label and entry field
to_unit_label = tk.Label(window, text="Enter the desired unit (Hz, kHz, MHz, GHz):")
to_unit_label.pack()
to_unit_entry = tk.Entry(window)
to_unit_entry.pack()

# Convert button
def perform_conversion():
    try:
        frequency = float(freq_entry.get())
        from_unit = from_unit_entry.get().lower()
        to_unit = to_unit_entry.get().lower()

        conversion_key = from_unit + "_to_" + to_unit
        reverse_conversion_key = to_unit + "_to_" + from_unit

        if conversion_key in conversion:
            converted = frequency * conversion[conversion_key]
            messagebox.showinfo("Conversion Result", f"{frequency} {from_unit} is equal to {converted} {to_unit}.")
        elif reverse_conversion_key in conversion:
            converted = frequency / conversion[reverse_conversion_key]
            messagebox.showinfo("Conversion Result", f"{frequency} {from_unit} is equal to {converted} {to_unit}.")
        else:
            messagebox.showerror("Invalid Units", "Invalid conversion units provided.")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the frequency.")

convert_button = tk.Button(window, text="Convert", command=perform_conversion)
convert_button.pack()

# Run the main loop
window.mainloop()