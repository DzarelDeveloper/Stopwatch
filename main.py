import tkinter as Tkinter

from datetime import datetime

counter = 0

running = False


def counter_label(label):
    def count():
        if running:
            global counter 
         #untuk mengatur penundaan awal
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string
    
            label['text'] = display
       # argumen pertama diberikan dalam milidetik
       # dan kemudian memanggil fungsi yang di berikan sebagai argumen kedua.
       # umumnya seperti disini kita perlu menelepon
       # fungsi yang hadir berulang kali
       # penundaan 1000 ms=1 detik dan panggilan dihitung lagi
    
            label.after(1000, count)
            counter += 1
    # mulai menghitung
    count()
    

# mulai fungsi stopwatch
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'
    
# hentikan fungsi stopwatch 
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

 # atur ulang fungsi stopwatch    
def Reset(label):
    global counter
    counter = 0 
  #jika reset di tekan setelah menekan stop
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
   # jika reset di tekan saat stopwatch sedang berjalan
    else:
        label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Stopwatch")

# ukuran jendela
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text='Ready!', fg='black', font='Verdana 30 bold')
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')
root.mainloop()