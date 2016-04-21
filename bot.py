import github, discord, asyncio, random, json
import botconfig
#from urllib.request import Request, urlopen


# TODO: Впилить указание авторов ПР/иссуев/коммитов

gh = github.GitHub(username=botconfig.githublogin, password=botconfig.githubpass)

latestgreenissue = -100
latestgreenpull = -100
latestgreencommit = ""

latestwhiteissue = -100
latestwhitepull = -100
latestwhitecommit = ""

latestblueissue = -100
latestbluepull = -100
latestbluecommit = ""

latesterisissue = -100
latesterispull = -100
latesteriscommit = ""

accesslist = ["<@154661006696644608>",  "<@154664883579912192>"]

greenissues = gh.repos('animusdev')('green').issues.get()
greenpulls = gh.repos('animusdev')('green').pulls.get()
greencommits = gh.repos('animusdev')('green').commits.get()

whiteissues = gh.repos('animusdev')('white').issues.get()
whitepulls = gh.repos('animusdev')('white').pulls.get()
whitecommits = gh.repos('animusdev')('white').commits.get()

blueissues = gh.repos('animusdev')('blue').issues.get()
bluepulls = gh.repos('animusdev')('blue').pulls.get()
bluecommits = gh.repos('animusdev')('blue').commits.get()

erisissues = gh.repos('algol12')('cev-eris').issues.get()
erispulls = gh.repos('algol12')('cev-eris').pulls.get()
eriscommits = gh.repos('algol12')('cev-eris').commits.get()

# GREEN ----------------------------------------------------------------------------------------------------------------
for i in greenissues:
    if i['number'] > latestgreenissue:
        latestgreenissue = i['number']
        print('Dankest latest issue is:', latestgreenissue)

for p in greenpulls:
    if p['number'] > latestgreenpull:
        latestgreenpull = p['number']
        print('Dankest latest pull is:', latestgreenpull)

if greencommits[0] != latestgreencommit:
    latestgreencommit = greencommits[0]
    print("Dankest latest commit is:", latestgreencommit['sha'], '\n')

# WHITE ----------------------------------------------------------------------------------------------------------------
for i in whiteissues:
    if i['number'] > latestwhiteissue:
        latestwhiteissue = i['number']
for p in whitepulls:
    if p['number'] > latestwhitepull:
        latestwhitepull = p['number']
if whitecommits[0] != latestwhitecommit:
    latestwhitecommit = whitecommits[0]

# BLUE -----------------------------------------------------------------------------------------------------------------
for i in blueissues:
    if i['number'] > latestblueissue:
        latestblueissue = i['number']
for p in bluepulls:
    if p['number'] > latestbluepull:
        latestbluepull = p['number']
if bluecommits[0] != latestbluecommit:
    latestbluecommit = bluecommits[0]

# CEV-Eris -------------------------------------------------------------------------------------------------------------
for i in erisissues:
    if i['number'] > latesterisissue:
        latesterisissue = i['number']
for p in erispulls:
    if p['number'] > latesterispull:
        latestbluepull = p['number']
if eriscommits[0] != latesteriscommit:
    latesteriscommit = eriscommits[0]

client = discord.Client()
server = None
greenchannel = None
voice = None
voicechannel = None
player = None

@client.event
async def on_ready():
    global latestgreenissue, latestgreenpull, latestgreencommit, client, server, greenchannel, voice, voicechannel
    global latestwhiteissue, latestwhitepull, latestwhitecommit
    global latestblueissue, latestbluepull, latestbluecommit
    global latesterisissue, latesterispull, latesteriscommit

    server = discord.utils.get(client.servers, name='Animus Servers')
    greenchannel = discord.utils.get(server.channels, name='green', type=discord.ChannelType.text)
    whitechannel = discord.utils.get(server.channels, name='white', type=discord.ChannelType.text)
    bluechannel = discord.utils.get(server.channels, name='blue', type=discord.ChannelType.text)
    erischannel = discord.utils.get(server.channels, name='cev_eris', type=discord.ChannelType.text)
    voicechannel = discord.utils.get(server.channels, name='filth 2', type=discord.ChannelType.voice)

    discord.opus.load_opus("libopus.so.0")
    voice = await client.join_voice_channel(voicechannel)

    ritchie = discord.utils.get(server.members, name='fluorescent')
    bo20202 = discord.utils.get(server.members, name='Bo20202')
    einlinet = discord.utils.get(server.members, name='Ein Linet')
    solar = discord.utils.get(server.members, name="Illy Ritter")
    silentenemy = discord.utils.get(server.members, name="SilentEnemy")
    truncated = discord.utils.get(server.members, name="Truncated")
    print("Ritchie's mention string:", ritchie.mention)
    print("Ein Linet's mention string:", einlinet.mention)
    print("SolarEclipse's mention string:", solar.mention)
    print("SilentEnemy's mention string:", silentenemy.mention)
    print("Truncated's mention string", truncated.mention)
    print("Bo20202's mention string:", bo20202.mention, '\n')

    print("Logging in..")
    print(client.user.name)
    print(client.user.id)
    print('------')

    while(1):
        greenissues = gh.repos('animusdev')('green').issues.get()
        greenpulls = gh.repos('animusdev')('green').pulls.get()
        greencommits = gh.repos('animusdev')('green').commits.get()

        whiteissues = gh.repos('animusdev')('white').issues.get()
        whitepulls = gh.repos('animusdev')('white').pulls.get()
        whitecommits = gh.repos('animusdev')('white').commits.get()

        blueissues = gh.repos('animusdev')('blue').issues.get()
        bluepulls = gh.repos('animusdev')('blue').pulls.get()
        bluecommits = gh.repos('animusdev')('blue').commits.get()

        erisissues = gh.repos('algol12')('cev-eris').issues.get()
        erispulls = gh.repos('algol12')('cev-eris').pulls.get()
        eriscommits = gh.repos('algol12')('cev-eris').commits.get()

        # GREEN --------------------------------------------------------------------------------------------------------
        for i in greenissues:
            if i['number'] > latestgreenissue:
                latestgreenissue = i['number']
                await client.send_message(greenchannel, '**У нас новый иссуй: #' + str(latestgreenissue) + '**')
                await client.send_message(greenchannel, 'https://github.com/animusdev/green/issues/' + str(latestgreenissue))
                print("NEW GREEN DANKEST ISSUE:", latestgreenissue)

        for p in greenpulls:
            if p['number'] > latestgreenpull:
                latestgreenpull = p['number']
                await client.send_message(greenchannel, '**У нас новый PR: #' + str(latestgreenpull) + '**')
                await client.send_message(greenchannel, 'https://github.com/animusdev/green/pull/' + str(latestgreenpull))
                print("NEW GREEN DANKEST PULL:", latestgreenpull)

        if greencommits[0] != latestgreencommit:
            latestgreencommit = greencommits[0]
            await client.send_message(greenchannel, '**У нас новый коммит: ' + latestgreencommit['sha'] + '**')
            await client.send_message(greenchannel, latestgreencommit['html_url'])
        # WHITE --------------------------------------------------------------------------------------------------------
        for i in whiteissues:
            if i['number'] > latestwhiteissue:
                latestwhiteissue = i['number']
                await client.send_message(whitechannel, '**У нас новый иссуй: #' + str(latestwhiteissue) + '**')
                await client.send_message(whitechannel, 'https://github.com/animusdev/white/issues/' + str(latestwhiteissue))
                print("NEW WHITE DANKEST ISSUE:", latestwhiteissue)

        for p in whitepulls:
            if p['number'] > latestwhitepull:
                latestwhitepull = p['number']
                await client.send_message(whitechannel, '**У нас новый PR: #' + str(latestwhitepull) + '**')
                await client.send_message(whitechannel, 'https://github.com/animusdev/white/pull/' + str(latestwhitepull))
                print("NEW WHITE DANKEST PULL:", latestwhitepull)

        if whitecommits[0] != latestwhitecommit:
            latestwhitecommit = whitecommits[0]
            await client.send_message(whitechannel, '**У нас новый коммит: ' + latestwhitecommit['sha'] + '**')
            await client.send_message(whitechannel, latestwhitecommit['html_url'])
        # BLUE ---------------------------------------------------------------------------------------------------------
        for i in blueissues:
            if i['number'] > latestblueissue:
                latestblueissue = i['number']
                await client.send_message(bluechannel, '**У нас новый иссуй: #' + str(latestblueissue) + '**')
                await client.send_message(bluechannel, 'https://github.com/animusdev/blue/issues/' + str(latestblueissue))
                print("NEW BLUE DANKEST ISSUE:", latestblueissue)

        for p in bluepulls:
            if p['number'] > latestbluepull:
                latestbluepull = p['number']
                await client.send_message(bluechannel, '**У нас новый PR: #' + str(latestbluepull) + '**')
                await client.send_message(bluechannel, 'https://github.com/animusdev/blue/pull/' + str(latestbluepull))
                print("NEW BLUE DANKEST PULL:", latestbluepull)

        if bluecommits[0] != latestbluecommit:
            latestbluecommit = bluecommits[0]
            await client.send_message(bluechannel, '**У нас новый коммит: ' + latestbluecommit['sha'] + '**')
            await client.send_message(bluechannel, latestbluecommit['html_url'])
        # CEV-Eris -----------------------------------------------------------------------------------------------------
        for i in erisissues:
            if i['number'] > latesterisissue:
                latesterisissue = i['number']
                await client.send_message(erischannel, '**У нас новый иссуй: #' + str(latesterisissue) + '**')
                await client.send_message(erischannel, 'https://github.com/algol12/cev-eris/issues/' + str(latesterisissue))
                print("NEW ERIS DANKEST ISSUE:", latesterisissue)

        for p in erispulls:
            if p['number'] > latesterispull:
                latesterispull = p['number']
                await client.send_message(erischannel, '**У нас новый PR: #' + str(latesterispull) + '**')
                await client.send_message(erischannel, 'https://github.com/algol12/cev-eris/pull/' + str(latesterispull))
                print("NEW ERIS DANKEST PULL:", latesterispull)

        if eriscommits[0] != latesteriscommit:
            latesteriscommit = eriscommits[0]
            await client.send_message(erischannel, '**У нас новый коммит: ' + latesteriscommit['sha'] + '**')
            await client.send_message(erischannel, latesteriscommit['html_url'])

        await asyncio.sleep(120)

@client.event
async def on_message(message):
    global client, latestgreenissue, latestgreenpull, latestgreencommit, isSinging, voice, voicechannel, player, accesslist
    global latestbluecommit, latestbluepull, latestblueissue
    global latestwhitecommit, latestwhitepull, latestwhiteissue
    global latesterisissue, latesterispull, latesteriscommit

    # GREEN ------------------------------------------------------------------------------------------------------------
    if message.content.startswith("Гринозник, що там с иссуями"):
        await client.send_message(message.channel, message.author.mention +" **Последний иссуй: #" + str(latestgreenissue) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/green/issues/" + str(latestgreenissue))

    elif message.content.startswith("Гринозник, що там с пуллреквестами"):
        await client.send_message(message.channel, message.author.mention +" **Последний PR: #" + str(latestgreenpull) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/green/pull/" + str(latestgreenpull))

    elif message.content.startswith("Гринозник, що там с коммитами"):
        await client.send_message(message.channel, message.author.mention +' **Последний коммит: ' + latestgreencommit['sha'] + '**')
        await client.send_message(message.channel, latestgreencommit['html_url'])

    # WHITE ------------------------------------------------------------------------------------------------------------
    elif message.content.startswith("Беляк, що там с иссуями"):
        await client.send_message(message.channel, message.author.mention +" **Последний иссуй: #" + str(latestwhiteissue) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/white/issues/" + str(latestwhiteissue))

    elif message.content.startswith("Беляк, що там с пуллреквестами"):
        await client.send_message(message.channel, message.author.mention +" **Последний PR: #" + str(latestwhitepull) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/white/pull/" + str(latestwhitepull))

    elif message.content.startswith("Беляк, що там с коммитами"):
        await client.send_message(message.channel, message.author.mention +' **Последний коммит: ' + latestwhitecommit['sha'] + '**')
        await client.send_message(message.channel, latestwhitecommit['html_url'])

    # BLUE -------------------------------------------------------------------------------------------------------------
    elif message.content.startswith("Синюшник, що там с иссуями"):
        await client.send_message(message.channel, message.author.mention +" **Последний иссуй: #" + str(latestblueissue) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/blue/issues/" + str(latestblueissue))

    elif message.content.startswith("Синюшник, що там с пуллреквестами"):
        await client.send_message(message.channel, message.author.mention +" **Последний PR: #" + str(latestbluepull) + "**")
        await client.send_message(message.channel, "https://github.com/animusdev/blue/pull/" + str(latestbluepull))

    elif message.content.startswith("Синюшник, що там с коммитами"):
        await client.send_message(message.channel, message.author.mention +' **Последний коммит: ' + latestbluecommit['sha'] + '**')
        await client.send_message(message.channel, latestbluecommit['html_url'])

    # CEV-Eris ---------------------------------------------------------------------------------------------------------
    elif message.content.startswith("Пятак, що там с иссуями"):
        await client.send_message(message.channel, message.author.mention +" **Последний иссуй: #" + str(latesterisissue) + "**")
        await client.send_message(message.channel, "https://github.com/algol12/cev-eris/issues/" + str(latesterisissue))

    elif message.content.startswith("Пятак, що там с пуллреквестами"):
        await client.send_message(message.channel, message.author.mention +" **Последний PR: #" + str(latesterispull) + "**")
        await client.send_message(message.channel, "https://github.com/algol12/cev-eris/pull/" + str(latesterispull))

    elif message.content.startswith("Пятак, що там с коммитами"):
        await client.send_message(message.channel, message.author.mention +' **Последний коммит: ' + latesteriscommit['sha'] + '**')
        await client.send_message(message.channel, latesteriscommit['html_url'])

    elif message.content.startswith("Гринозник, запускай гуся"):
        await client.send_message(message.channel, message.author.mention+"""
ЗАПУСКАЕМ
░ГУСЯ░▄▀▀▀▄░РАБОТЯГИ░░
▄███▀░◐░░░▌░░░░░░░
░░░░▌░░░░░▐░░░░░░░
░░░░▐░░░░░▐░░░░░░░
░░░░▌░░░░░▐▄▄░░░░░
░░░░▌░░░░▄▀▒▒▀▀▀▀▄
░░░▐░░░░▐▒▒▒▒▒▒▒▒▀▀▄
░░░▐░░░░▐▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░▀▄░░░░▀▄▒▒▒▒▒▒▒▒▒▒▀▄
░░░░░░▀▄▄▄▄▄█▄▄▄▄▄▄▄▄▄▄▄▀▄
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░░░▌▌░▌▌░░░░░
░░░░░░░░░▄▄▌▌▄▌▌░░░░░""")

    elif message.content.startswith("Гринозник, що там у тебя") or message.content.startswith("Синюшник, що там у тебя") or message.content.startswith("Беляк, що там у тебя"):
        await client.send_message(message.channel, message.author.mention+""" Не щокайте на меня, я могу узнать:
- Що там с иссуями
- Що там с пуллреквестами
- Що там с коммитами
- *Що там у хохлiв*
Обращайтесь к Гринознику за мемасами и информацией о Грине, к Беляку - за информацией о Вайте, к Синюшнику - за информацией о Блю.""")

    elif message.content.startswith("Що там у хохлiв") or message.content.startswith("Гринозник, що там у хохлiв"):
        await client.send_message(message.channel, message.author.mention+" ***Всё очень плохо.***")

    elif message.content.startswith("Гринозник, забань"):
        await client.send_message(message.channel, message.author.mention+random.choice([" Тогда весь Анимус пустым будет.", " Не, я тоже грифозный пидорас в душе.",
                                                                                        " Вы меня не заставите.", " Погрифонят - тогда и забаню.",
                                                                                        " Пока фрагов нет же.", " Скинемся всем Анимусом!"]))

    elif message.content.startswith("Гринозник, свергай Ниссе") or message.content.startswith("Гринозник, свергни Ниссе"):
        await client.send_message(message.channel, message.author.mention+random.choice([" Я уже.", " Мои соратники уже.",
                                                                                         " Нахуй свергать, у вас и так там армия ботов."]))

    elif message.content.startswith("Гринозник, разбань"):
        await client.send_message(message.channel, message.author.mention+random.choice([" Соски или пошёл нахуй", " Разбанил, проверяй", " Сначала Шепарду задонать",
                                                                                         " Щас запермлю", " А вот хуй."]))

    elif message.content.startswith("Що там на вайте") or message.content.startswith("Гринозник, що там на вайте"):
        await client.send_message(message.channel, message.author.mention+random.choice([" Сайлентиум в лидах", " Ролеплей протек", " Катану и бордер всё ещё не убрали",
                                                                                         " Очередную перму сняли", " ИИ опять отсеки сжег под Азимовым", " ИС'ин'ООС протек",
                                                                                         " Сайлентиума распедалили пермой"]))

    elif message.content.startswith("Гринозник, опусти плина") or message.content.startswith("Гринозник, опусти Плина"):
        await client.send_message(message.channel, "<@153497699407101952>"+random.choice([" Даже у меня есть педали, а у тебя нет", " Ты - хуй",
                                                                                          " Я не на MySQL, страдай", " Как ты аргументируешь то, что у тебя нет педалей, а у меня есть?",
                                                                                          " Сейчас я тебе перму вхардкодю!", " Плин - он и в Африке хуй."]))

    elif (message.content.startswith("Гринозник") or message.content.startswith("гринозник")) and message.author.mention == "<@153497699407101952>":
        await client.send_message(message.channel, "<@153497699407101952>"+random.choice([" Ты - хуй, и это аксиома.", " Помножь себя на ноль", " Ты - ничто, а у меня педали.",
                                                                                          " Ну давай, унижай себя, я знаю, ты любишь это делать.", " Что-нибудь ещё?",
                                                                                          " Плин, ты такой хуй, что это даже немного забавно.", " Чего тебе, кусок мяса?"]))

    elif message.content.startswith("Заперми") or message.content.startswith("заперми") or message.content.startswith("Гринозник, заперми") or message.content.startswith("гринозник, заперми"):
        await client.send_message(message.channel, message.author.mention+" Запермил, проверяй")

    elif message.content.startswith("Гринозник, опусти Шепарда") or message.content.startswith("Гринозник, опусти шепарда") or message.content.startswith("Гринозник, опусти Шепку") or message.content.startswith("Гринозник, опусти шепку"):
        await client.send_message(message.channel, random.choice(["Я не устраиваю охуительные ивонты в отличие от Шепарда", "Я собрал 1 копейку из 1 копейки, и это 100%. Какие результаты у тебя, Шеп?",
                                                                  "Грiн незалежний, слава Анимусу, долой тиранию Шепхурда!", "Шепард так и не закончил пятый билд.",
                                                                  "Я не лагаю."]))

    elif message.content.startswith("Гринозник, варианты развития ситуации"):
        await client.send_message(message.channel, random.choice(["А всё идет по плану, всё идет по плануу", "Винтовка - это праздник, всё летит в пизду!"]))

    elif message.content.startswith("Гринозник, спой Летова") and message.author.mention in accesslist:
        player = voice.create_ffmpeg_player(random.choice(["moyaoborona.mp3", "vechnayavesna.mp3", "russkoepole.mp3", "vsyoidetpoplanu.mp3"]))
        player.start()

    elif message.content.startswith("Гринозник, спой Боуи") and message.author.mention in accesslist:
        player = voice.create_ffmpeg_player("spaceoddity.mp3")
        player.start()

    elif (message.content.startswith("Гринозник, начинай финальный отсчет") or message.content.startswith("Гринозник, начинай финальный отсчёт")) and message.author.mention in accesslist:
        player = voice.create_ffmpeg_player("finalcountdown.mp3")
        player.start()

    elif (message.content.startswith("Гринозник, давай ядреного") or message.content.startswith("Гринозник, давай ядрёного")) and message.author.mention in accesslist:
        player = voice.create_ffmpeg_player("imnuclear.ogg")
        player.start()

    elif message.content.startswith("Гринозник, спой Cranberries") and message.author.mention in accesslist:
        player = voice.create_ffmpeg_player("zombie.mp3")
        player.start()

    elif message.content.startswith("Гринозник, хватит петь") and message.author.mention in accesslist:
        player.stop()

#    elif message.content.startswith("Гринозник, спой Летова"):
#        moyaoborona = ["Пластмассовый мир победил. Макет оказался сильней.", "Последний кораблик остыл, последний фонарик устал.", "А в горле сопят комья воспоминаний!",
#                       "**ОООО, МОЯ ОБОРОНА, СОЛНЧЕНЫЙ ЗАЙЧИК СТЕКЛЯННОГО ГЛАЗА**", "**ОООО, МОЯ ОБОРОНА, ТРАУРНЫЙ МЯЧИК НЕЛЕПОГО МИРА, ТРАУРНЫЙ МЯЧИК ДЕШЕВОГО МИРАА**",
#                       "Пластмассовый мир победил. Ликует картонный набат.", "Кому нужен ломтик июльского неба?", "**ОООО МОЯ ОБОРОНА СОЛНЕЧНЫЙ ЗАЙЧИК НЕЗРЯЧЕГО МИРА**",
#                       "**ОООО МОЯ ОБОРОНА ТРАУРНЫЙ МЯЧИК СТЕКЛЯННОГО ГЛАЗА, ТРАУРНЫЙ ЗАЙЧИК НЕЛЕПОГО МИРА**", "Пластмассовый мир победил. Макет оказался сильней.",
#                       "Последний кораблик остыл, последний фонарик устал.", "А в горле сопят комья воспоминаний!", "**ОООО МОЯ ОБОРОНА ТРАУРНЫЙ МЯЧИК НЕЗРЯЧЕГО МИРА**",
#                       "**ОООО МОЯ ОБОРОНА СОЛНЕЧНЫЙ ЗАЙЧИК СТЕКЛЯННОГО ГЛАЗА**", "**ОООО МОЯ ОБОРОНАААА**", "**ОООО МОЯ ОБОРОНАААА**", "**ОООООО ООООО ОООООО ОООООО**", "МОЯ ОБОРОНААА!"]
#        if message.author.mention == "<@154661006696644608>":
#            isSinging = 1
#            for songstring in moyaoborona:
#                await client.send_message(message.channel, songstring)
#                await asyncio.sleep(2)
#            isSinging = 0

#    elif message.content.startswith("Гринозник, що там с рублём") or message.content.startswith("Гринозник, що там с рублем") or message.content.startswith("Що там с рублём") or message.content.startswith("Що там с рублем"):
#        req = Request("https://openexchangerates.org/api/latest.json?app_id=3ae9c391e3924c80850b584e74f26d3e", headers={'User-Agent': 'Mozilla/5.0'})
#        rouble = urlopen(req).read()
#        parsedrouble = json.loads(rouble)
#        await client.send_message(message.channel, message.author.mention+" Курс рубля: "+str(parsedrouble))

client.run(botconfig.discordlogin, botconfig.discordpass)