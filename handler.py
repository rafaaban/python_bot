import requests
import json 


def received_message(event,token):

	pass
	sender_id = event['sender']['id']
	recipient_id=event['recipient']['id']
	time_message=event['timestamp']
	message=event['message']
	text = message['text']

	message = text_message(sender_id,text)
	call_send_API(message,token)

def text_message(recipient_id, message_text):
	
	mensaje = "no te entiendo"

	if message_text == "hola" :
		mensaje = "hola AGS DEVELOPERS"

	
	

	message_data = {
	'recipient' : {'id'  : recipient_id},
	'message' : {'text' : mensaje}
	}
	return message_data

def call_send_API(data,token):
	res = requests.post('https://graph.facebook.com/v2.6/me/messages',
		params = {'access_token': token},
		data = json.dumps(data),
		headers = {'Content-type' : 'application/json'}
		 )
	if res.status_code == 200 : 
		print 'mensaje enviado'

		

