import openai
from dotenv import dotenv_values

config = dotenv_values('.env')
openai.api_key = config['API_KEY']

def get_response(message):
  try:
      response = openai.completions.create(
          model='gpt-3.5-turbo-instruct',
          prompt=message,
          max_tokens=400,
          temperature=0.3
      )
      return response.choices[0].text
  except Exception as e:
        print(f"❌ Error: {e}")
  return None

print('👽: Hello! You can ask me anything.')
print('Write something or just hit enter to exit')

connected = True
while connected:
    message = input('👾: ')
    if message == '':
      connected = False
      print('👽: Goodbye!')
    else:
      answer = get_response(message)
      if answer:
        print('👽: ' + answer)
      else:
        connected = False