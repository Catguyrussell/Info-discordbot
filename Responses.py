import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == '!5einfo':
        return 'Hey there! Heres 5E tools https://5e.tools/'
    
    if p_message == '!codeblock':
        return '```'
    
    if p_message == '!fullmtgrules':
        return 'here are the full mtg rules https://media.wizards.com/2023/downloads/MagicCompRules%2020230414.pdf'
    
    if p_message == '!topdeckstandard':
        return 'https://www.mtggoldfish.com/metagame/standard#paper'
    
    if p_message == '!topdeckmodern':
        return 'https://www.mtggoldfish.com/metagame/modern#paper'
    
    if p_message == 'hello':
        return 'Hey there!'
        
    if p_message == '!topdeckpioneer':
        return 'https://www.mtggoldfish.com/metagame/pioneer#paper'
        
    if p_message == 'rolld2':
        return str(random.randint(1, 2))
        
    if p_message == 'rolld4':
        return str(random.randint(1, 4))
    
    if p_message == 'rolld6':
        return str(random.randint(1, 6))
    
    if p_message == 'rolld8':
        return str(random.randint(1, 8))
    
    if p_message == 'rolld10':
        return str(random.randint(1, 10))
    
    if p_message == 'rolld12':
        return str(random.randint(1, 12))
    
    if p_message == 'rolld20':
        return str(random.randint(1, 20))
    
    if p_message == 'rolld100':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"

         #  return 'Yeah, I don\'t know. Try typing "!help".'
