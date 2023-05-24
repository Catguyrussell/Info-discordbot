import random


def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == '!5einfo':
        return 'Hey there! Heres 5E tools https://5e.tools/'
    
    if p_message == '!codeblock':
        return '``'
    
    if p_message == '!fullmtgrules':
        return 'here are the full mtg rules https://media.wizards.com/2023/downloads/MagicCompRules%2020230414.pdf'
    
    if p_message == '!topdeckstandard':
        return 'https://www.mtggoldfish.com/metagame/standard#paper'
    
    if p_message == '!topdeckmodern':
        return 'https://www.mtggoldfish.com/metagame/modern#paper'
    
    if p_message == '!topdeckhistoric':
        return 'https://www.mtggoldfish.com/metagame/historic#paper'
        
    if p_message == '!topdeckpioneer':
        return 'https://www.mtggoldfish.com/metagame/pioneer#paper'
        
    if p_message == '!topdeckalchemy':
        return 'https://www.mtggoldfish.com/metagame/alchemy#paper'
        
    if p_message == '!topdeckexplorer':
        return 'https://www.mtggoldfish.com/metagame/explorer#paper'
        
    if p_message == '!topdecklegacy':
        return 'https://www.mtggoldfish.com/metagame/legacy#paper'
        
    if p_message == '!topdeckpauper':
        return 'https://www.mtggoldfish.com/metagame/pauper#paper'
        
    if p_message == '!topdeckvintage':
        return 'https://www.mtggoldfish.com/metagame/vintage#paper'
    
    if p_message == '!topdeckcedh':
        return 'https://cedh-decklist-database.com/'
        
    if p_message == '!topcommander':
        return 'https://edhrec.com/commanders'
    
    if p_message == '!topthemeedh':
        return 'https://edhrec.com/themes'
    
    if p_message == '!toptribeedh':
        return 'https://edhrec.com/tribes'
    
    if p_message == '!saltedh':
        return 'https://edhrec.com/top/salt'
    
    if p_message == '!dnddamcal':
        return 'https://rpgbot.net/dnd5/tools/dpr-calculator/'
    
    if p_message == 'hello':
        return 'Hey there!'
        
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message == 'rolld2':
        return str(random.randint(1, 2))
    
    if p_message == 'rolld3':
        return str(random.randint(1, 3))
        
    if p_message == 'rolld4':
        return str(random.randint(1, 4))
    
    if p_message == 'rolld5':
        return str(random.randint(1, 2))
    
    if p_message == 'rolld6':
        return str(random.randint(1, 5))
    
    if p_message == 'rolld8':
        return str(random.randint(1, 8))
    
    if p_message == 'rolld9':
        return str(random.randint(1, 9))
    
    if p_message == 'rolld10':
        return str(random.randint(1, 10))
    
    if p_message == 'rolld11':
        return str(random.randint(1, 11))
    
    if p_message == 'rolld12':
        return str(random.randint(1, 12))
    
    if p_message == 'rolld13':
        return str(random.randint(1, 13))
    
    if p_message == 'rolld14':
        return str(random.randint(1, 14))
    
    if p_message == 'rolld15':
        return str(random.randint(1, 15))
    
    if p_message == 'rolld16':
        return str(random.randint(1, 16))
    
    if p_message == 'rolld17':
        return str(random.randint(1, 17))
    
    if p_message == 'rolld18':
        return str(random.randint(1, 18))
    
    if p_message == 'rolld19':
        return str(random.randint(1, 19))
    
    if p_message == 'rolld20':
        return str(random.randint(1, 20))
    
    if p_message == 'rolld100':
        return str(random.randint(1, 100))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"

         #  return 'Yeah, I don\'t know. Try typing "!help".'
