from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
load_dotenv()

PREFIX = os.environ['PREFIX']
TOKEN = os.environ['TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '이돟님':
        await message.channel.send(as_LeeDonim[random.randrange(0, 4)])

    if message.content == 'ㅎㅇ':
        await message.channel.send('ㅎㅇ')

    if message.content == 'ㅂㅇ':
        await message.channel.send('ㅂㅇ')

    if message.content == '아항':
        await message.channel.send('아항')

    if message.content == '어서오세요':
        await message.channel.send('안녕히가세요')

    if message.content == '하오님':
        await message.channel.send(as_Hao[random.randrange(0, 1)])

#---------------------------------------------------------------------------------------------------

    if message.content.startswith('안녕'):
        await message.channel.send(as_Hi[random.randrange(0, 4)])

    if message.content.startswith('화이팅!'):
        await message.channel.send('ㅎㅇㅌ')

    if message.content.startswith('ㅋㅋ'): 
        await message.channel.send(as_kkk[random.randrange(0, 4)])
        
    if message.content.startswith('ㅠㅠㅠㅠㅠ'): 
        await message.channel.send(as_TT[random.randrange(0, 4)])

    if message.content.startswith('ㅠㅠㅠㅠㅠ'):
        await message.channel.send('뭐요')

    if message.content.startswith('만장님'):
        await message.channel.send('파란만장~~~ 네 인생도 파란만장, 내 인생도 파란만장. 아~ 인생 고달프다아')

    if message.content.startswith('왜'):
        await message.channel.send(as_why[random.randrange(0, 4)])


#---------------------------------------------------------------------------------------------------
as_LeeDonim = ['네에', '네?', '뭐요', '?', '말걸지마세요']
as_Hao = ['뭐!? 하오님이라고!??', '하오님은 언제나 이뻐! 멋져! 귀여워!']
as_Hi = ['안녕하쇼', '안녕하십니끄아아아아아아아아아아아아아아아악', '안녕하냐', '밥은 먹고 다니냐', '카레라이스']
as_kkk = ['ㅋㅋㅋ', '허파에 바람들었어요?', '암흑이론에 대한 설명', 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ', 'ㅋㅋ']
as_TT = ['아 거, 울지 마쇼', '신파극소리나네', '춘자잣 춘잣 춘자자잣', '홍삼을 먹도록 하렴', '쯧...']
as_why = ['본인의 아이큐를 1부터 10중에 표현하자면', 
          '돼지고기 김치찌개 맛내는 비법 진한 국물이 맛있는 돼지고기 김치찌개입니다.'
            +'물 2컵(250ml 기준), 돼지고기 찌개용(or 목살 250g), 신김치 200g, 김칫국물 5큰술',
            '왜', '궁금하다why', '예비군 언제 감?']
#---------------------------------------------------------------------------------------------------


try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
