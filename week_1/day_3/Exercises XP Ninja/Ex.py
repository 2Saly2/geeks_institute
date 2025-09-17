class Phone :
    def __init__(self,phone_nmb):
        self.phone_nmb= phone_nmb
        self.call_history = []
        self.messages=[]
    def call(self, other_phone):
        call_info =f"{self.phone_nmb} called {other_phone.phone_nmb}"
        print(call_info)
        self.call_history.append(call_info)
    
    def show_call_history(self):
        print("\ncall history :")
        for call in self.call_history:
            print(call)
    def send_message(self, other_phone, content):
        message = {
            "to": other_phone.phone_nmb,
            "from": self.phone_nmb,
            "content": content
        }
        self.messages.append(message)
        print(f"Message sent to {other_phone.phone_nmb}: {content}")

    def show_outgoing_messages(self):
        print("\nOutgoing Messages:")
        for msg in self.messages:
            if msg["from"] == self.phone_nmb:
                print(f"To: {msg['to']} | Content: {msg['content']}")

    def show_incoming_messages(self):
        print("\nIncoming Messages:")
        for msg in self.messages:
            if msg["to"] == self.phone_nmb:
                print(f"From: {msg['from']} | Content: {msg['content']}")

    def show_messages_from(self, phone_nmb):
        print(f"\nMessages from {phone_nmb}:")
        for msg in self.messages:
            if msg["from"] == phone_nmb:
                print(f"Content: {msg['content']}")


phone1 = Phone("06122456")
phone2 = Phone("06208745")


phone1.call(phone2)
phone1.call(phone2)
phone1.show_call_history()


phone1.send_message(phone2, "Hi, how are you?")
phone1.send_message(phone2, "Don't forget our meeting!")
phone1.show_outgoing_messages()


phone2.messages.append({
    "to": phone2.phone_nmb,
    "from": phone1.phone_nmb,
    "content": "Hello from phone1"
})

phone2.show_incoming_messages()
phone2.show_messages_from("0730245670")