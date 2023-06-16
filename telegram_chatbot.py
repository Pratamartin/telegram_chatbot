# Import libraries, and enter the Telegram API KEY

import telebot
import emoji
from telebot import types


API_KEY = '5485852352:AAHWemp3rtlCFF0fAP0GmwCN_m4QBOuhbIc'
bot = telebot.TeleBot(API_KEY)


# Creating our dictionaries containing the information that will compose our database

descricao_das_empresas = {
    'Microsoft': 'A Microsoft é uma renomada empresa de tecnologia sediada nos Estados Unidos. Fundada por Bill Gates e Paul Allen, a empresa é líder global no desenvolvimento de software, serviços e soluções tecnológicas. A Microsoft é conhecida por seu sistema operacional Windows, que é amplamente utilizado em computadores pessoais em todo o mundo. Além disso, a empresa oferece uma variedade de produtos e serviços, incluindo o pacote de produtividade Office, soluções em nuvem com o Microsoft Azure e a plataforma de jogos Xbox.',
    'Samsung': 'A Samsung é uma das maiores empresas de tecnologia do mundo, com sede na Coreia do Sul. Ela abrange uma ampla gama de setores, incluindo eletrônicos de consumo, dispositivos móveis, eletrodomésticos, semicondutores e muito mais. A Samsung é conhecida por sua inovação em dispositivos móveis, como smartphones e tablets da linha Galaxy, bem como por suas TVs de alta qualidade e eletrodomésticos avançados. Além disso, a empresa desempenha um papel importante na fabricação de componentes eletrônicos, fornecendo chips e displays para várias indústrias.',
    'Google': 'O Google é uma empresa de tecnologia multinacional sediada nos Estados Unidos, conhecida principalmente por seu mecanismo de busca online líder do mercado. Além disso, o Google oferece uma ampla gama de serviços e produtos, incluindo o sistema operacional móvel Android, o navegador Chrome, o serviço de e-mail Gmail, o armazenamento em nuvem Google Drive e muito mais. A empresa também está envolvida em projetos de pesquisa avançada, como veículos autônomos, inteligência artificial e tecnologias de saúde.',
    'OpenAI': 'A OpenAI é uma empresa de pesquisa e desenvolvimento de inteligência artificial com sede nos Estados Unidos. Seu objetivo é avançar no campo da IA para beneficiar a humanidade como um todo. A OpenAI trabalha em projetos de pesquisa de ponta e desenvolvimento de tecnologias avançadas de IA. A empresa é conhecida por desenvolver modelos de linguagem de grande escala, como o GPT (Generative Pre-trained Transformer), que tem sido amplamente utilizado em várias aplicações, desde assistentes virtuais até geração de texto.',
    'Tesla': 'A Tesla é uma empresa de veículos elétricos sediada nos Estados Unidos, fundada por Elon Musk. Ela é conhecida por sua abordagem inovadora na fabricação de automóveis elétricos de alta qualidade, com ênfase na sustentabilidade e desempenho. A Tesla é pioneira na tecnologia de baterias de longa duração e nos sistemas de condução autônoma. Além dos carros elétricos, a empresa também está envolvida na produção de sistemas de armazenamento de energia e painéis solares, impulsionando o desenvolvimento de soluções energéticas renováveis.'
}

descricao_dos_assuntos = {
    'Inovação e Economia Circular': '....Botar texto...',
    'Ambientes de Inovação': '....Botar texto...',
    'Redes de Inovação': '....Botar texto...',
    'Propriedade Intelectual': 'Propriedade intelectual (PI) é um conjunto de diretrizes elaboradas paradar proteção legal às criações humanas, garantindo ao autor (pessoa física ou jurídica) o direito de utilizá-las para gerar lucro. As invenções com finalidade industrial, marcas, patentes e outros sinais distintivos são protegidos pela propriedade industrial já as criações literárias e artísticas são protegias pelos direitos autorais.',
    'transferência de tecnologia': '....Botar texto...',
    'Spillover de conhecimento': '....Botar texto...'

}

# Defining labels for our buttons

LABEL_LISTAR_EMPRESAS = 'Listar Empresas'
LABEL_LISTAR_ASSUNTOS = 'Listar Assuntos'


# Comands
# ReplyKeyboardMarkup sets the keyboard response type
# KeyboardButton defines the buttons that will appear on the keyboard
# emoji.emojize add emoji to a formatted string

# Displays the initial welcome message to the Bot

def apresentacao(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    botao_empresas = types.KeyboardButton(LABEL_LISTAR_EMPRESAS)
    botao_assuntos = types.KeyboardButton(LABEL_LISTAR_ASSUNTOS)

    markup.row(botao_empresas)
    markup.row(botao_assuntos)

    bot.reply_to(
        message,
        emoji.emojize('Olá, seja bem vindo a nova era :robot:'),
        reply_markup=markup
    )

# Displays companies saved in our dictionary as a list of clickable buttons

def mostrar_empresas(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for key in descricao_das_empresas.keys():
        markup.row(types.KeyboardButton(key))

    bot.reply_to(
        message,
        emoji.emojize('Empresas disponíveis para consulta :office_building:'),
        reply_markup=markup
    )

# Displays the description of the selected company and then returns to the presentation menu

def mostrar_descricoes_das_empresas(message):
    bot.send_message(message.chat.id, descricao_das_empresas[message.text])
    apresentacao(message)

# Displays subjects saved in our dictionary as a list of clickable buttons

def mostrar_assuntos(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)

    for key in descricao_dos_assuntos.keys():
        markup.row(types.KeyboardButton(key))

    bot.reply_to(
        message,
        emoji.emojize('Assuntos :pencil:'),
        reply_markup=markup)

# Displays the description of the selected subject and returns to the presentation menu

def mostrar_descricoes_dos_assuntos(message):
    bot.send_message(message.chat.id, descricao_dos_assuntos[message.text])
    apresentacao(message)

# Creating a special handler to handle our new commands

@bot.message_handler(func=lambda message: True)
def default(message):
    if message.text == LABEL_LISTAR_EMPRESAS:
        mostrar_empresas(message)
    elif message.text == LABEL_LISTAR_ASSUNTOS:
        mostrar_assuntos(message)
    elif message.text in descricao_das_empresas.keys():
        mostrar_descricoes_das_empresas(message)
    elif message.text in descricao_dos_assuntos.keys():
        mostrar_descricoes_dos_assuntos(message)
    else:
        apresentacao(message)

bot.polling()