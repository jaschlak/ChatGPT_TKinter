# -*- coding: utf-8 -*-

from support.config import get_configuration

from tkinter import Text, WORD, END
import customtkinter
import openai

config = get_configuration()

class TKInter_Class:
    
    def __init__(self):
        
        self.oai_key = config['oai_key']
        
        # Initiate App
        self.root = customtkinter.CTk()
        self.root.title("ChatGPT Bot")
        self.root.geometry('600x600')
        self.root.iconbitmap('ai_lt.ico') #https://tkinter.com/images/ai_lt.ico
        # Set Color Scheme
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        
        self.add_text_frame()
        self.add_scrollbar()
        self.add_button_frames()
        self.add_chat_entry()
        self.add_submit_button()
        self.add_clear_button()
        self.add_update_api_button()
        self.add_api_frame()
        self.add_save_api_button()
        self.add_api_entry_widget()

    def send_message_method(self):

        if self.chat_entry.get():
            
            try:
                
                openai.api_key = self.oai_key
                
                # create an oai instance
                openai.Model.list()
                
                #Define our Query /Response
                response = openai.Completion.create(
                    model = "text-davinci-003",
                    prompt = self.chat_entry.get(),
                    temperature = 1, # 0-2, higher is more specific
                    max_tokens = 200, # max text returned
                    top_p = 1.0,
                    frequency_penalty = 0.0,
                    presence_penalty = 0.0)
                
                self.my_text.insert(END, (response['choices'][0]['text']).strip())
                self.my_text.insert(END, "\n\n")
            
            except Exception as e:
                self.my_text.insert(END, "\n\n There was an error \n\n{}".format(e))
            
        else:
            self.my_text.insert(END, "\n\n No entry detected for textbox")
                    
    def clear_method(self):
        
        # clear main text box
        self.my_text.delete(1.0,END)
        # clear query entry box
        self.chat_entry.delete(0,END)
        
    def save_api_method(self):
        
        self.oai_key = self.api_entry.get()
        
        #resize app smaller
        self.root.geometry('600x600')
        
        
        
    def update_api_method(self):
        
        # resize app larger
        self.root.geometry('600x750')
        # reshow api frame
        self.api_frame.pack(pady=30)
        
        #output to entry box
        self.api_entry.insert(END, self.oai_key)
        
    def add_text_frame(self):
        
        # Create Text Frame
        self.text_frame = customtkinter.CTkFrame(self.root)
        self.text_frame.pack(pady=20)
        
        # Add Text Widget to get ChatGPT Responses    
        self.my_text = Text(self.text_frame,
                       bg="#343638",
                       width=65,
                       bd=1,
                       fg="#d6d6d6",
                       relief="flat",
                       wrap=WORD,
                       selectbackground="#1f538d")
        self.my_text.grid(row=0, column=0)
        
    def add_scrollbar(self):
        
        # Create scrollbar for text widget
        text_scroll = customtkinter.CTkScrollbar(self.text_frame,
                                                 command=self.my_text.yview)
        text_scroll.grid(row=0, column=1, sticky="ns")
        
        # Add scrollbar to textbox
        self.my_text.configure(yscrollcommand=text_scroll.set)
        
        
    def add_chat_entry(self):
        
        # Add Entry widget (type to chatgpt)
        self.chat_entry = customtkinter.CTkEntry(self.root,
                                            placeholder_text = "Type Something To ChatGPT",
                                            width=535,
                                            height=50,
                                            border_width=1)
        self.chat_entry.pack(pady=10)
        
    def add_button_frames(self):
        
        # Create button frame
        self.button_frame = customtkinter.CTkFrame(self.root, fg_color="#242424")
        self.button_frame.pack(pady=30)
        
    def add_submit_button(self):
        
        # Create submit button
        self.submit_button = customtkinter.CTkButton(self.button_frame,
                                                text="Speak To ChatGPT",
                                                command=self.send_message_method)
        self.submit_button.grid(row=0, column=0, padx=25)
        
        
    def add_clear_button(self):
        
        # create clear button
        self.clear_button = customtkinter.CTkButton(self.button_frame,
                                                text="Clear Response",
                                                command=self.clear_method)
        self.clear_button.grid(row=0, column=1, padx=35)
        
    def add_update_api_button(self):
        
        # create api button
        self.api_button = customtkinter.CTkButton(self.button_frame,
                                                text="Update API Key",
                                                command=self.update_api_method)
        self.api_button.grid(row=0, column=2, padx=30)
        
    def add_api_frame(self):
        # Create api frame
        self.api_frame = customtkinter.CTkFrame(self.root, border_width=1)
        self.api_frame.pack(pady=10)
        
    def add_save_api_button(self):
        
        self.api_save_button = customtkinter.CTkButton(self.api_frame,
                                          text="Save Key",
                                          command=self.save_api_method)
        self.api_save_button.grid(row=0, column=1, padx=10)
        
    def add_api_entry_widget(self):
        
        # Add API Entry Widget
        self.api_entry = customtkinter.CTkEntry(self.api_frame,
                                           placeholder_text="Enter your api key",
                                           width=350, height=50, border_width=1)
        self.api_entry.grid(row=0,column=0,padx=20,pady=20)
        
        self.api_save_button = customtkinter.CTkButton(self.api_frame,
                                                  text="Save Key",
                                                  command=self.save_api_method)
        self.api_save_button.grid(row=0, column=1, padx=10)