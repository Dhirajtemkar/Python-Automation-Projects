from twilio.rest import Client 
 
account_sid = 'AC5186c7d0635033688ba7cfdfac1aaf64' 
auth_token = 'a47c33745db527ead9fc8f88fc88d058' 
client = Client(account_sid, auth_token) 

# twilio_whatsapp_number='whatsapp:+14155238886'
# count = 10
# while(count>0):
#     count-=1
message = client.messages.create( 
                            from_='whatsapp:ENTER_TWILIO-SANDBOX_NUMBER',  
                            body='You have been Spammed! ;)',      
                            to='whatsapp:ENTER_YOUR_NUMBER' 
                        ) 

print(message.sid)
