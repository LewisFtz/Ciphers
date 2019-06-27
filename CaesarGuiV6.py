from tkinter import *
import Caesar
import VernamGui

class CaesarGui():
        
    def __init__(self,master):
        self.master = master
        self.master.configure(background='light sea green')
        self.master.title("Caesar encrypt")
        self.master.option_add('*Font', 'Georgia 12') #font for all widgets
        self.master.option_add('Label.Font','helvetica 20 bold') # font for all lables
        self.master.option_add('*Background', 'light sea green')#background for widgets
        self.master.option_add('*Entry.Background', 'white') 
        self.master.geometry('410x325+100+100') #w,h,x,y
        self.top()
        self.middle()  
        self.bottom() 




    def top(self):        
        top_frame=Frame(self.master)        
        lbl_header=Label(top_frame)
        lbl_header.config(text="Caesar Cipher", font='helvetica 32 bold')      
        top_frame.grid_rowconfigure(0,minsize=150)
        top_frame.grid(row=0)

        btnOtp=Button(top_frame)
        btnOtp.config(text='OTP', borderwidth=2, padx=0)
        btnOtp.bind('<Button-1>',self.OTP)
        btnOtp.grid(row=0, column=2)
        

        
        lbl_header.grid(row=0, column=1, padx=20)
        

    def middle(self):       
        mid_frame=Frame(self.master)
        
         #Label - Text
        lbl_Text = Label(mid_frame)
        lbl_Text.config(text='Text: ')

        #Label - Key
        lbl_Key = Label(mid_frame)
        lbl_Key.config(text='Key(1-25): ')

        #Label - Output
        lbl_Out = Label(mid_frame)
        lbl_Out.config(text='Output: ')
        
        #Text Entry - Text
        self.Text=StringVar(mid_frame)
        txt_Text = Entry(mid_frame)
        txt_Text.config(textvariable=self.Text,  width=20)

        
        #Text Entry - Key
        self.Key=StringVar(mid_frame)        
        txt_Key = Entry(mid_frame)
        txt_Key.config(textvariable=self.Key,  width=20)

        #Text Entry - Output
        self.Out=StringVar(mid_frame)        
        txt_Out = Entry(mid_frame)
        txt_Out.config(textvariable=self.Out,  width=20)
   
            
        mid_frame.grid_columnconfigure(0,minsize=100)
        mid_frame.grid(row=1, sticky='w')
        
        #row 0
        lbl_Text.grid(row=0, column=0, sticky='e', padx=10)
        txt_Text.grid(row=0, column=1, padx=10)
        #row 1
        lbl_Key.grid(row=1, column=0, sticky='e', padx=10)
        txt_Key.grid(row=1, column=1, padx=10)

        #row 2
        lbl_Out.grid(row=2, column=0, sticky='e', padx=10)
        txt_Out.grid(row=2, column=1, padx=10)

     
    def bottom(self):
        
        #frame for bottom section
        bottom_frame=Frame(self.master)        
        self.useful_msg=StringVar(bottom_frame)
        self.useful_msg.set("Enter text and key")
        self.lbl_msg = Label(bottom_frame) 
        self.lbl_msg.config(textvariable=self.useful_msg, fg='gold', width=21)
        #encrypt buttons
        btn_encrypt=Button(bottom_frame)
        btn_encrypt.config(text='Encrypt Text', borderwidth=2, padx=0)
        btn_encrypt.bind('<Button-1>',self.encrypt)
        #decrypt buttons
        btn_decrypt=Button(bottom_frame)
        btn_decrypt.config(text='Decrypt Text', borderwidth=2, padx=0)
        btn_decrypt.bind('<Button-1>',self.decrypt)        
        bottom_frame.grid_rowconfigure(0,minsize=50)
        bottom_frame.grid(row=2)
        #row 0
        self.lbl_msg.grid(row=0, column=0)
        #row 1
        btn_encrypt.grid(row=1, column=0)
        btn_decrypt.grid(row=1, column=2)
        

    def OTP(self,event):
        print ("Test")
  
        self.newWindow = Toplevel(self.master)
        self.app=VernamGui.VernamGui(self.newWindow)


        
    def encrypt(self,event):
        InvalidKey = ("Invalid key, re-enter key")
        NotInt = ("Not an integer")
        
        PlainText = self.Text.get()
        Key = self.Key.get()

        while True:
            try:
                Key = int(Key)
            except ValueError:
                self.useful_msg.set(NotInt)
                return False
                
            else:            
                if Key >= 1 and Key <=25:
                    break                        
                    
                else:
                    self.useful_msg.set(InvalidKey)
                    return False
                    

        
        EncryptedText = Caesar.Encrypt(PlainText,Key)
                
        self.Out.set(EncryptedText)
        self.useful_msg.set("Encryption complete")       

 
    def decrypt(self,event):

        InvalidKey = ("Invalid key, re-enter key")
        NotInt = ("Not an integer")
        EncryptedText = self.Text.get()
        Key = self.Key.get()
        
        while True:
            try:
                Key = int(Key)
            except ValueError:
                self.useful_msg.set(NotInt)
                return False
            
            else:            
                if Key >= 1 and Key <=25:
                    break                       
                    
                else:
                    self.useful_msg.set(InvalidKey)
                    return False

        
        DecryptedText = Caesar.Decrypt(EncryptedText,Key)
        self.Out.set(DecryptedText)
        self.useful_msg.set("Decryption complete")


def main():
    root = Tk()#makes root window

    Gui = CaesarGui(root)   #makes instance of gui application
    root.mainloop() #starts frame handler
    
    

        
main()


    

        
