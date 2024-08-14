import discord
from discord.ext import commands
import random
from pydub import AudioSegment
from pydub.playback import play
import os
import asyncio

PREFIX = '!'
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
intents.guilds = True
intents.voice_states = True
AUDIO_FILE = 'video.mp3'

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

ydl_opts = {
    'format': 'bestaudio/best',
}

VIDEO_URL = 'https://www.youtube.com/watch?v=IBw5DC2x-ho' 

adjectives = {
    'мужской': ['анальный', 'оральный', 'вагинальный', 'уретральный', 'подноктевой', 'кишечный', 'подпяточный', 'подмышечный',
                'свинной', 'вонючий', 'гнойный', 'отвратительный', 'навальный', 'картвый', 'уебищный', 'уродливый', 'жировой',
                'подскладочный', 'богомерзкий', 'отчаяный', 'желчный', 'картавый', 'опущенный', 'шепелявый', 'блевотный',
                'интимный', 'подзалупный', 'дрыщавый', 'прыщавый', 'узбекский', 'ущербный', 'адский', 'азартный', 'астрономический',
                'бездонный', 'газированный', 'безумный', 'беспощадный', 'беспрекословный', 'буйный', 'вопиющий', 'гигантский',
                'грандиозный', 'гробовой', 'законченный', 'изувеченный', 'каменный', 'матерый', 'неистовый', 'немой', 'ослинный',
                'отчаянный', 'ошеломляющий', 'первоклассный', 'потный', 'прирожденный', 'пронзительный', 'пьянящий', 'радикальный',
                'седой', 'сказочный', 'сногсшибательный', 'солидный', 'страстный', 'сумасшедший', 'суровый', 'умопомрачительный',
                'фанатичный', 'яростный'],
    'женский': ['анальная', 'оральная', 'вагинальная', 'уретральная', 'подноктевая', 'кишечная', 'подпяточная', 'подмышечная',
                'свинья', 'вонючая', 'гнойная', 'отвратительная', 'навальная', 'картавая', 'уебищная', 'уродливая', 'жировая',
                'подскладочная', 'богомерзкая', 'отчаянная', 'желчная', 'картавая', 'опущенная', 'шепелявая', 'блевотная',
                'интимная', 'подзалупная', 'дрыщевая', 'прыщевая', 'узбекская', 'ущербная', 'адская', 'азартная', 'астрономическая',
                'бездонная', 'газированная', 'безумная', 'беспощадная', 'беспрекословная', 'буйная', 'вопиющая', 'гигантская',
                'грандиозная', 'гробовая', 'законченнная', 'изувеченная', 'каменная', 'матеря', 'неистовая', 'немая', 'ослиная',
                'отчаянная', 'ошеломляющая', 'первоклассная', 'потная', 'прирожденная', 'пронзительная', 'пьянящая', 'радикальная',
                'седая', 'сказочная', 'сногсшибательная', 'солидная', 'страстная', 'сумасшедшая', 'суровая', 'умопомрачительная',
                'фанатичная', 'яростная'],
    'средний': ['анальное', 'оральное', 'вагинальное', 'уретральное', 'подноктевое', 'кишечное', 'подпяточное', 'подмышечное',
                'свинное', 'вонючее', 'гнойное', 'отвратительное', 'навальное', 'картавая', 'уебищное', 'уродливое', 'жировое',
                'подскладочное', 'богомерзкое', 'отчаянное', 'желчное', 'картавая', 'опущенное', 'шепелявое', 'блевотное',
                'интимное', 'подзалупное', 'дрыщавое', 'прыщавое', 'узбекское', 'ущербное', 'адское', 'азартное', 'астрономическое',
                'бездонное', 'газированное', 'безумное', 'беспощадное', 'беспрекословное', 'буйное', 'вопищее', 'гигантское',
                'грандиозное', 'гробовое', 'законченное', 'изувеченное', 'каменное', 'матерое', 'неистовое', 'немое', 'ослиное',
                'отчаянное', 'ошеломляющее', 'первоклассное', 'потное', 'прирожденное', 'пронзительное', 'пьянящее', 'радикальное',
                'седое', 'сказочное', 'сногсшибательное', 'солидное', 'страстное', 'сумасшедшее', 'суровое', 'умопомрачительное',
                'фанатичное', 'яростное']
}

nouns = ['пробка', 'альтруист', 'сперма', 'чен', 'прыщ', 'индус', 'очко', 'залупа', 'влагалище',
         'пердун', 'дрочила', 'пидор', 'пизда', 'малафья', 'гомик', 'мудила', 'пилотка', 'манда', 'анус',
         'вагина', 'путана', 'пидрила', 'мошонка', 'елда', 'абортыш', 'негроид', 'терпилоид', 'хрящ',
         'таракан', 'ишак', 'плесень', 'упырь', 'гомодрилл', 'шайтан', 'окурок', 'носок', 'выкидыш',
         'мандавошка', 'глист', 'вымя', 'бабуин', 'карасик', 'нюхач', 'чиркаш']

actions = ['испражнения', 'аборт', 'насильник', 'пробовал', 'тянка', 'давалка', 'орангутанг', 'Игорь',
           'Сиськи', 'жака фреско', 'кремлебота', 'бабы яги', 'кадырова', 'алкаша', 'бомжа', 'насильника',
           'наркомана', 'саня', 'габен']

def choose_adjective_suffix(adjective, noun):
    if noun in ['прыщ', 'индус', 'пердун', 'дрочила', 'пидор', 'пизда', 'малафья', 'гомик', 'мудила', 'пилотка', 'манда', 'анус', 'чиркаш']:
        noun_gender = 'мужской'
    elif noun in ['вагина', 'путана', 'пидрила', 'мошонка', 'елда']:
        noun_gender = 'женский'
    else:
        noun_gender = 'средний'

    suffix = {
        'мужской': '',
        'женский': '',
        'средний': ''
    }[noun_gender]

    if adjective.endswith('н'):
        return adjective + suffix
    return adjective + suffix

def generate_nickname():
    adjective = random.choice(adjectives['мужской'])
    noun = random.choice(nouns)
    action = random.choice(actions)

    final_adjective = choose_adjective_suffix(adjective, noun)
    if action == 'пробовал':
        nickname = f'{final_adjective} {noun}'
    else:
        nickname = f'{final_adjective} {noun} {action}'

    return nickname

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    try:
        nickname = generate_nickname()
        await member.edit(nick=nickname)
        print(f'Changed nickname of {member} to {nickname}')
    except discord.Forbidden:
        print('Bot does not have permission to change nicknames.')
    except discord.HTTPException as e:
        print(f'Failed to change nickname: {e}')

@bot.command(name='change_all_nicknames')
@commands.has_permissions(administrator=True)
async def change_all_nicknames(ctx):
    for member in ctx.guild.members:
        if member.bot:
            continue
        try:
            nickname = generate_nickname()
            await member.edit(nick=nickname)
            print(f'Changed nickname of {member} to {nickname}')
        except discord.Forbidden:
            print(f'Bot does not have permission to change nickname for {member}.')
        except discord.HTTPException as e:
            print(f'Failed to change nickname for {member}: {e}')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if not member.bot:
            vc = await after.channel.connect()
            audio = AudioSegment.from_mp3(AUDIO_FILE)
            audio.export("temp.wav", format="wav")
            source = discord.FFmpegPCMAudio("temp.wav")
            vc.play(source, after=lambda e: print('Done playing'))
            while vc.is_playing():
                await asyncio.sleep(1)
            await vc.disconnect()

bot.run('TOKENWEEWOOWEEWOO')
