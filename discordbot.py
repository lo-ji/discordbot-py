from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
from datetime import datetime
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
    
    if message.content == '죽어라':
        await message.channel.send(as_Hao[random.randrange(0, 2)])

    if message.content == '내이름':
        await message.channel.send(message.author.username + '맞죠?') #이거 동작 안 함. 봐야댐

    if message.content == '야':
        await message.channel.send('뭐')

#---------------------------------------------------------------------------------------------------

    if message.content.startswith('안녕'):
        await message.channel.send(as_Hi[random.randrange(0, 4)])

    if message.content.startswith('화이팅!'):
        await message.channel.send('ㅎㅇㅌ')

    if message.content.startswith('ㅋㅋ'): 
        await message.channel.send(as_kkk[random.randrange(0, 4)])
        
    if message.content.startswith('ㅠㅠㅠㅠㅠ'): 
        await message.channel.send(as_TT[random.randrange(0, 4)])

    if message.content.startswith('만장님'):
        await message.channel.send('파란만장~~~ 네 인생도 파란만장, 내 인생도 파란만장. 아~ 인생 고달프다아')

    if message.content.startswith('왜'):
        await message.channel.send(as_why[random.randrange(0, 4)])

    if message.content.startswitch('뭐더라'):
        await message.channel.send('4월 생존신고 진행중입니다~! 디스코드 생존신고 채널에 생존신고 눌러주세요!' +
         '닉네임도 생존신고 기간동안은 단톡방과 되도록 맞춰주세요!')


#---------------------------------------------------------------------------------------------------
as_LeeDonim = ['네에', '네?', '뭐요', '?', '말걸지마세요']
as_Die = ['뒤질래', '님선', 'ㅗ']
as_Hao = ['뭐!? 하오님이라고!??', '하오님은 언제나 이뻐! 멋져! 귀여워!']
as_Hi = ['안녕하쇼', '안녕하십니끄아아아아아아아아아아아아아아아악', '안녕하냐', '밥은 먹고 다니냐', '카레라이스']
as_kkk = ['ㅋㅋㅋ', '허파에 바람들었어요?', '암흑이론에 대한 설명', 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ', 'ㅋㅋ']
as_TT = ['아 거, 울지 마쇼', '신파극소리나네', '춘자잣 춘잣 춘자자잣', '홍삼을 먹도록 하렴', '쯧...']
as_why = ['본인의 아이큐를 1부터 10중에 표현하자면', 
          '돼지고기 김치찌개 맛내는 비법 진한 국물이 맛있는 돼지고기 김치찌개입니다.'
            +'물 2컵(250ml 기준), 돼지고기 찌개용(or 목살 250g), 신김치 200g, 김칫국물 5큰술',
            '왜', '궁금하다why', '예비군 언제 감?']

self_ = ['뀨><',
         '이야기는 끝났다. 박수쳐라',
         ' 다른 사람에게 허용된다고 해서, 너에게도 허용되는건 아니다.​',
         '사랑하는 사람들은 미친 사람이다',
         '4월 생존신고 진행중입니다~! 디스코드 생존신고 채널에 생존신고 눌러주세요!' +
         '닉네임도 생존신고 기간동안은 단톡방과 되도록 맞춰주세요!']
#---------------------------------------------------------------------------------------------------
# 시간
@client.event
async def on_time(message):
    now = datetime.now()

    if now.hour == 4:
        await message.channel.send('점심시간~ 밥은 먹고 그려야죠')
        return
    
    elif now.hour == 15 and now.minute == 13:
        await message.channel.send('점심시간~ 밥은 먹고 그려야죠')





#---------------------------------------------------------------------------------------------------

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
