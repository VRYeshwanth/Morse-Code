import tkinter as tk

window = tk.Tk()
window.title('Decoding Morse')

code_list = {
    'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.','F': '..-.','G': '--.','H': '....','I': '..','J': '.---','K': '-.-','L': '.-..','M': '--','N': '-.','O': '---','P': '.--.','Q': '--.-','R': '.-.','S': '...','T': '-','U': '..-','V': '...-','W': '.--','X': '-..-','Y': '-.--','Z': '--..','0': '-----','1': '.----','2': '..---','3': '...--','4': '....-','5': '.....','6': '-....','7': '--...','8': '---..','9': '----.','&': '.-...',"'": '.----.','@': '.--.-.',')': '-.--.-','(': '-.--.',':': '---...',',': '--..--','=': '-...-','!': '-.-.--','.': '.-.-.-','-': '-....-','×': '-..-','%': '------..-.-----','+': '.-.-.','"': '.-..-.','?': '..--..','/': '-..-.', ' ': ''
}

def convert():
    convert_mode = mode.get()
    string = input_box.get("1.0", tk.END).strip()
    st = ""

    if convert_mode == "Text to Morse":
        output_box.delete("1.0", tk.END)
        for i in string:
            if i == " ":
                st += "/ "
            elif i.upper() in code_list:
                st += f"{code_list[i.upper()]} "
            else:
                st += "? "
        st = st.strip()  # Remove any trailing space or slash
        output_box.insert("1.0", st)
    
    if convert_mode == "Morse to Text":
        output_box.delete("1.0", tk.END)
        inp_list = string.split(" / ")  # Split by " / " to differentiate words

        final_str = ""
        for item in inp_list:
            letters = item.split(" ")  # Split each word into letters
            for letter in letters:
                for key, value in code_list.items():
                    if value == letter:
                        final_str += key
                        break
            final_str += " "  # Add space between words
        
        output_box.insert("1.0", final_str.strip())  # Strip to remove extra space

head = tk.Label(window, text="Morse Code Convertor", font=("Cascadia Code", 20, "bold"))
head.pack()

box_frame = tk.Frame(window)
box_frame.pack(padx=15, pady=15)

inp_head = tk.Label(box_frame, text="Input :-", font=("Cascadia Code", 16))
inp_head.grid(row=0, column=0, sticky=tk.W)

out_head = tk.Label(box_frame, text="Output :-", font=("Cascadia Code", 16))
out_head.grid(row=0, column=2, sticky=tk.W, padx=(20,0))

# Input text box with scrollbar
input_frame = tk.Frame(box_frame)
input_frame.grid(row=1, column=0, padx=(0,20))
input_box = tk.Text(input_frame, width=35, height=10, font=("Cascadia Code", 16))
input_box.pack(side=tk.LEFT)
input_scroll = tk.Scrollbar(input_frame, command=input_box.yview)
input_scroll.pack(side=tk.RIGHT, fill=tk.Y)
input_box.config(yscrollcommand=input_scroll.set)

arrow_label = tk.Label(box_frame, text="→", font=("Cascadia Code", 40))
arrow_label.grid(row=1, column=1, padx=10)

# Output text box with scrollbar
output_frame = tk.Frame(box_frame)
output_frame.grid(row=1, column=2, padx=(20,0))
output_box = tk.Text(output_frame, width=35, height=10, font=("Cascadia Code", 16))
output_box.pack(side=tk.LEFT)
output_scroll = tk.Scrollbar(output_frame, command=output_box.yview)
output_scroll.pack(side=tk.RIGHT, fill=tk.Y)
output_box.config(yscrollcommand=output_scroll.set)

radio_frame = tk.Frame(window)
radio_frame.pack()

mode = tk.StringVar()
mode.set("Text to Morse")

ch1 = tk.Radiobutton(radio_frame, text="Text to Morse", variable=mode, value="Text to Morse", font=("Cascadia Code", 16))
ch1.grid(row=0, column=0, padx=(0,50))
ch2 = tk.Radiobutton(radio_frame, text="Morse to Text", variable=mode, value="Morse to Text", font=("Cascadia Code", 16))
ch2.grid(row=0, column=1, padx=(50,0))

convert_btn = tk.Button(window, text="Convert", font=("Cascadia Code", 16), command=convert)
convert_btn.pack(pady=15, ipadx=10, ipady=3)

window.mainloop()
