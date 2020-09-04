# It's Friday!!
import speech_recognition
from gtts import gTTS, lang
from playsound import playsound

import random


# Funcao para falar
def speakText(command): 

	tts = gTTS(command, lang='pt-br')
	speechs = tts.get_urls()

	for speech in speechs:
		playsound(speech)



def hearSpeech(reconVoz):

	textPT = ""
	textEN = ""


	try:

		# Use o microfone como entrada
		with speech_recognition.Microphone() as inputVoice:

			# Ajuste o reconhecimento de voz para o ruido ambiente
			reconVoz.adjust_for_ambient_noise(inputVoice, duration=0.2)


			# Escute o que esta sendo falado
			# voice = reconVoz.listen(inputVoice, snowboy_configuration=("snowboys", "*.pmdl")''')
			voice = reconVoz.listen(inputVoice)


			# Use o google para reconhecer a voz
			#textPT = reconVoz.recognize_ibm(voice, language='pt-BR')
			textPT = reconVoz.recognize_google(voice, language='pt-BR')
			textEN = reconVoz.recognize_google(voice, language='en-US')

			#textPT = textPT.lower()
			#textEN = textEN.lower()
	

	except speech_recognition.RequestError as error:
		print("Could not request results; {0}".format(error))


	except speech_recognition.UnknownValueError:
		print("unknown error occured")


	return textPT, textEN



def answerSpeech(speechTextPT, speechTextEN):


	wordsPT = speechTextPT.split(' ')
	wordsEN = speechTextEN.split(' ')


	if 'friday' in wordsEN:
		return random.choice (['O que você quer?',
							   'Que eh?',
							   'Fala tu?'])
	

	elif ('beleza' in wordsPT) or ( ('tudo' in wordsPT) and ('bem' in wordsPT) ):
		return random.choice (['Tô maravilhosamente bem e voce?',
							   'Tô cansada de responder e voce?',
							   'É... to indo... e voce?'])


	elif ('bem' in wordsPT) or ('tranquilo' in wordsPT):
		return random.choice (['E o que eu tenho haver com isso?',
							   'Tanto faz...',
							   'De boas.'])
	

	elif 'tempo' in wordsPT:
		return 'Tá quente hoje né?'
	

	elif wordsPT == ['sim'] or wordsPT == ['nao']:
		return ''

	
	elif wordsPT == ['tu']:
		return random.choice (['Haha engraçadinho... ¬¬',
							   'Olha! Temos um palhaço aqui!',
							   'Sem tempo para as suas idiotices...'])
	

	elif ('claro' in wordsPT) and ('faz' in wordsPT):
		return random.choice (['A não faz não!',
							   'Só no teu mundinho!',
							   'Me poupe!'])


	return random.choice (["Essa pergunta nao faz o menor sentido!",
						   "Tua mãe não te ensinou a falar não?"])



# Funcao principal
if __name__ == "__main__":

	# Inicia o Reconhecimento de voz
	reconVoz = speech_recognition.Recognizer()


	# Linguagens
	# print(lang.tts_langs(tld='com'))


	# Variavel de decisao da parada da assistente
	stop = False


	print("Escutando...")


	while (not stop):

		speechTextPT, speechTextEN = hearSpeech(reconVoz)
		

		if (speechTextPT != ""):

			print("You    > " + speechTextPT)

			text2Speech = answerSpeech(speechTextPT, speechTextEN)


			# Repita o que foi falado
			if text2Speech != '':
				print("Friday > " + text2Speech)
				speakText(text2Speech)