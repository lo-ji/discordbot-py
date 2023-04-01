from cmath import log
from distutils.sysconfig import PREFIX
import discord
from dotenv import load_dotenv
import os
import random
from discord.ext import tasks # 반복 작업을 위한 패키지
import datetime # 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
import time # 중복 전송을 방지하기 위해 사용할 패키지
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
        await message.channel.send(message.author.name + '맞죠?')

    if message.content == '야':
        await message.channel.send('뭐')
    
    if message.content == '@이돟':
        await message.channel.send('부르지마라.')

    if message.content == '?':
        await message.channel.send('?????')
   
#---------------------------------------------------------------------------------------------------

    if message.content.startswith('안녕하'):
        await message.channel.send(as_Hi[random.randrange(0, 4)])

    if message.content.startswith('화이팅!'):
        await message.channel.send('ㅎㅇㅌ')

    if message.content.startswith('ㅋㅋ'): 
        await message.channel.send(as_kkk[random.randrange(0, 4)])
        
    if message.content.startswith('ㅠㅠㅠ'): 
        await message.channel.send(as_TT[random.randrange(0, 4)])

    if message.content.startswith('만장님'):
        await message.channel.send('파란만장~~~ 네 인생도 파란만장, 내 인생도 파란만장. 아~ 인생 고달프다아')

    if message.content.startswith('왜'):
        await message.channel.send(as_why[random.randrange(0, 4)])

    if message.content.startswitch('뭐더라'):
        await message.channel.send('4월 생존신고 진행중입니다~! 디스코드 생존신고 채널에 생존신고 눌러주세요!' +
         '닉네임도 생존신고 기간동안은 단톡방과 되도록 맞춰주세요!')
    
    if message.content.startswith('@이돟'):
        await message.channel.send(summons_leedoh[random.randrange(0, 7)])

    if message.content.startswith('이돟vs차은우'):
        await message.channel.send('치명적인 오류가 발생되어 뇌를(을) 종료합니다.')

    if message.content.startswith('피카'):
        await message.channel.send('피카피카!')
    
#---------------------------------------------------------------------------------------------------
# 이돟전용

    if str(message.author) == 'HODO#5363' and message.content.startswith('어나더 에고'):
        await message.channel.send('조용히해')
        await message.channel.send('또다른나')
        await message.channel.send('네 힘은 필요없다고 했을텐데')

    if str(message.author) == 'HODO#5363' and message.content.startswith('@이돟'):
        await message.channel.send('또다른나. 반갑군.')
        await message.channel.send('무슨일로 나를 부른것이지?')
        await message.channel.send('이돟vs차은우 이딴거 물어보면 아주 그냥;')

    if str(message.author) == 'HODO#5363' and message.content.startswith('이돟'):
        await message.channel.send(summons_leedoh[random.randrange(0, 7)])

    if str(message.author) == 'HODO#5363' and message.content.startswith('돈내놔'):
        await message.channel.send('2000만원이면 돼.')

    if str(message.author) == '콘티#1106':
        await message.channel.send('왔는가 오리여.')
#---------------------------------------------------------------------------------------------------
# 새로운 함수 선언
# @tasks.loop(seconds=1)
# async def every_hour_notice(self):
#     if datetime.datetime.now().minute == 17: # and datetime.datetime.now().second == 0:
#         await on_message('Debug')
#         await client.get_guild("815850415131590676").get_channel("815850415131590680").send("현재 {}시 {}분 입니다.".format(datetime.datetime.now().hour, datetime.datetime.now().minute))

#         # 1초 sleep하여 중복 전송 방지. 1분에 한 번은 minutes=1, 2시간에 한 번은 hours=2로 설정하면 되겠습니다.
#         time.sleep(1)


#---------------------------------------------------------------------------------------------------
as_LeeDonim = ['네에', '네?', '뭐요', '?', '말걸지마세요']
as_Die = ['뒤질래', '님선', 'ㅗ']
as_Hao = ['뭐!? 하오님이라고!??', '하오님은 언제나 이뻐! 멋져! 귀여워!']
as_Hi = ['안녕하쇼', '안녕하냐', '밥은 먹고 다니냐', '카레라이스']
as_kkk = ['ㅋㅋㅋ', '허파에 바람들었어요?', 'ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ', 'ㅋㅋ']
as_TT = ['아 거, 울지 마쇼', '신파극소리나네', '춘자잣 춘잣 춘자자잣', '홍삼을 먹도록 하렴', '쯧...']
as_why = ['본인의 아이큐를 1부터 10중에 표현하자면', 
          '돼지고기 김치찌개 맛내는 비법 진한 국물이 맛있는 돼지고기 김치찌개입니다.'
            +'물 2컵(250ml 기준), 돼지고기 찌개용(or 목살 250g), 신김치 200g, 김칫국물 5큰술',
            '왜', '궁금하다why', '예비군 언제 감?']

self_ = ['뀨><',
         '이야기는 끝났다. 박수쳐라',
         ' 다른 사람에게 허용된다고 해서, 너에게도 허용되는건 아니다.',
         '사랑하는 사람들은 미친 사람이다',
         '4월 생존신고 진행중입니다~! 디스코드 생존신고 채널에 생존신고 눌러주세요!' +
         '닉네임도 생존신고 기간동안은 단톡방과 되도록 맞춰주세요!',
         '방장의 특별권한데스',
         '나는 이돟의 또다른 자아다.']


summons_leedoh = ['나를 부른 이유는?', '조용히 해.', '귀찮군.', '또 다른 나는 어디에 있지?',
                  '할 일이 하나 늘었군.', '미미쨩 다이스키다욧 >_<//', '어둠속에서 깨어났다. 나를 깨운자여 죽어라.', self_[random.randrange(0, 7)]]
#---------------------------------------------------------------------------------------------------
        
    



#---------------------------------------------------------------------------------------------------

try:
    client.run(TOKEN)
except discord.errors.LoginFailure as e:
    print("Improper token has been passed.")
