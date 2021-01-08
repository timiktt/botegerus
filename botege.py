import vk_api
import random
import time
import datetime


from vk_api.keyboard import VkKeyboard, VkKeyboardColor

def ex(a):
    b='ex'+str(a)+'.'
    return b



def kol(a):
    if a==4:
        return "25"
    elif a==5:
        return "25"
    elif a==6:
        return "25"
    elif a==7:
        return "25"
    elif a==8:
        return "25"
    elif a==9:
        return "26"
    elif a==10:
        return "25"
    elif a==11:
        return "25"
    elif a==12:
        return "25"
    elif a==13:
        return "25"
    elif a==14:
        return "26"
    elif a==15:
        return "24"
    elif a==16:
        return "25"
    elif a==17:
        return "25"
    elif a==18:
        return "26"
    elif a==19:
        return "24"
    elif a==20:
        return "25"
    elif a==21:
        return "25"





def proverka(a,b):
    if b==4:
        i=0
        while i!=a:
            i+=1
        if i==26:
            return 0
        else:
            return i
    elif b==5:
        i = 25
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 51:
            return 0
        else:
            return n
    elif b==6:
        i = 50
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 76:
            return 0
        else:
            return n
    elif b==7:
        i = 75
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 101:
            return 0
        else:
            return n
    elif b==8:
        i = 100
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 126:
            return 0
        else:
            return n
    elif b==9:
        i = 125
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 152:
            return 0
        else:
            return n
    elif b==9:
        i = 125
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 152:
            return 0
        else:
            return n
    elif b==10:
        i = 151
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 177:
            return 0
        else:
            return n
    elif b==11:
        i = 176
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 201:
            return 0
        else:
            return n
    elif b==12:
        i = 200
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 226:
            return 0
        else:
            return n
    elif b==13:
        i = 225
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 251:
            return 0
        else:
            return n
    elif b==14:
        i = 250
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 277:
            return 0
        else:
            return n
    elif b==15:
        i = 276
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 301:
            return 0
        else:
            return n
    elif b==16:
        i = 300
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 326:
            return 0
        else:
            return n
    elif b==17:
        i = 325
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 351:
            return 0
        else:
            return n
    elif b==18:
        i = 350
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 377:
            return 0
        else:
            return n
    elif b==19:
        i = 376
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 401:
            return 0
        else:
            return n
    elif b==20:
        i = 400
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 426:
            return 0
        else:
            return n
    elif b==21:
        i = 425
        n=0
        while i != a:
            i += 1
            n+=1
        if i == 451:
            return 0
        else:
            return n

mass_id = [0]
count_id=[0]
number_active_zad=[0]
mass_fg=[0]
kolvo_zad=[[0]]
token = '20a4b540f7364fbab1dbf47c0c84377974304f0faa4b02d35c548db95f4b4814bf5b69e0678d229bc8898'
vstup = 'Добро пожаловать😊\n Это твой персональный помощник в подготовке к ЕГЭ по Русскому языку✨\n Первый БОТ - тренажер🤖 во ВКонтакте\n\n📚Чтобы начать работу, нажми «решать».\n📚Выбери номер задания, который хочешь проработать.\n❗Все ответы пиши слитно (приветпока)❗ иначе наш бот не поймет тебя😢\nИменно так нужно записывать ответ в бланк на экзамене, готовься к этому заранее😌\n\n📌Если ты хочешь закончить подготовку на сегодня, то нажми «закончить».\n\n📊Если хочешь узнать, как продвигается твоя подготовка, то в меню можно найти кнопку «моя статистика», нажав на которую ты узнаешь свои успехи.'
vkontakte = vk_api.VkApi(token=token)
vkontakte._auth_token()

keyboard = VkKeyboard(one_time=True)
keyboard.add_button("4", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("5", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("6", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("7", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("8", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("9", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("10", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("11", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("12", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("13", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("14", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("15", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("16", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("17", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("18", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("19", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("20", color=VkKeyboardColor.POSITIVE)
keyboard.add_button("21", color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_button("Вернуться в меню", color=VkKeyboardColor.NEGATIVE)


keyboard1=VkKeyboard(one_time=True)
keyboard1.add_button("Узнать ответ", color=VkKeyboardColor.POSITIVE)
keyboard1.add_line()
keyboard1.add_button("Закончить", color=VkKeyboardColor.NEGATIVE)

keyboard2=VkKeyboard(one_time=True)
keyboard2.add_button("Дальше", color=VkKeyboardColor.POSITIVE)

keyboard3=VkKeyboard(one_time=True)
keyboard3.add_button("Решать", color=VkKeyboardColor.POSITIVE)
keyboard3.add_line()
keyboard3.add_button("Моя статистика", color=VkKeyboardColor.POSITIVE)

k=0

fg_rus=False
check=False
otvet=''
slov0=''
ot=open('otv.txt','r',encoding="utf-8")
kod=open('prob.txt','r',encoding="utf-8")
for i in kod:
    slov0+=(str(i))
for i in ot:
    otvet+=(str(i))


zad=[0]
otv=[0]
number=1
while number!=451:
    otv.append(otvet[otvet.find(ex(number)):otvet.rfind(ex(number + 1))])
    zad.append(slov0[slov0.find(ex(number)):slov0.rfind(ex(number + 1))])
    number+=1



print("Started!!! GLHF")
while True:
    try:
        messages = vkontakte.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if not fg_rus:
            if messages["count"] >= 1:
                print(mass_id)
                id = messages["items"][0]["last_message"]["from_id"]
                if id not in mass_id:
                    mass_id.append(id)
                    count_id.append(1)
                    number_active_zad.append(1)
                    kolvo_zad+=[[0,0,0,0,1,26,51,76,101,126,152,177,201,226,251,277,301,326,351,377,401,426]]
                    mass_fg.append(False)
                body = messages["items"][0]["last_message"]["text"]
                if not mass_fg[mass_id.index(id)]:
                    if body.lower() == 'привет':
                        vkontakte.method("messages.send",
                                         {"peer_id": id, "message": 'Привет, друг!✌🏻',
                                          "random_id": random.randint(1, 124323125345),
                                          "keyboard": keyboard3.get_keyboard()})

                    elif body.lower() == 'начать':
                        vkontakte.method("messages.send",
                                         {"peer_id": id, "message": vstup,
                                          "random_id": random.randint(1, 124323125345),
                                          "keyboard": keyboard3.get_keyboard()})
                    elif body.lower() == 'вернуться в меню':
                        vkontakte.method("messages.send",
                                         {"peer_id": id, "message": 'Вы в главном меню📲',
                                          "random_id": random.randint(1, 124323125345),
                                          "keyboard": keyboard3.get_keyboard()})
                    elif body.lower() == 'решать':
                        vkontakte.method("messages.send",
                                         {"peer_id": id, "message": 'Пора начать!🚀\nМы верим, что ты справишься.♥',
                                          "random_id": random.randint(1, 124323125345),
                                          "keyboard": keyboard.get_keyboard()})
                    elif body.lower() == '4':
                        number_active_zad[mass_id.index(id)]=4
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)])==0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard3.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message":'Задание  '+ str(proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)]))+ '/' + kol(number_active_zad[mass_id.index(id)])+ '\n' + zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]].find('.')+1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)]=True
                    elif body.lower() == '5':
                        number_active_zad[mass_id.index(id)] = 5
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard3.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '6':

                        number_active_zad[mass_id.index(id)] = 6
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '7':

                        number_active_zad[mass_id.index(id)] = 7
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '8':

                        number_active_zad[mass_id.index(id)] = 8
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '9':

                        number_active_zad[mass_id.index(id)] = 9
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '10':

                        number_active_zad[mass_id.index(id)] = 10
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '11':

                        number_active_zad[mass_id.index(id)] = 11
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '12':

                        number_active_zad[mass_id.index(id)] = 12
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '13':

                        number_active_zad[mass_id.index(id)] = 13
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '14':

                        number_active_zad[mass_id.index(id)] = 14
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '15':

                        number_active_zad[mass_id.index(id)] = 15
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '16':

                        number_active_zad[mass_id.index(id)] = 16
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '17':

                        number_active_zad[mass_id.index(id)] = 17
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '18':

                        number_active_zad[mass_id.index(id)] = 18
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '19':

                        number_active_zad[mass_id.index(id)] = 19
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '20':

                        number_active_zad[mass_id.index(id)] = 20
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True
                    elif body.lower() == '21':

                        number_active_zad[mass_id.index(id)] = 21
                        if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                    number_active_zad[mass_id.index(id)]) == 0:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": "Вы выполнили все задания из данного блока🥺✅",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                        else:

                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Задание  ' + str(proverka(
                                                 kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                                 number_active_zad[mass_id.index(id)])) + '/' + kol(
                                                 number_active_zad[mass_id.index(id)]) + '\n' + zad[kolvo_zad[
                                                 mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[
                                                                                                               kolvo_zad[
                                                                                                                   mass_id.index(
                                                                                                                       id)][
                                                                                                                   number_active_zad[
                                                                                                                       mass_id.index(
                                                                                                                           id)]]].find(
                                                 '.') + 1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            mass_fg[mass_id.index(id)] = True

                    elif body.lower() == 'моя статистика':
                        stat=''
                        i=4
                        while i!=22:
                            number_active_zad[mass_id.index(id)]=i
                            stat+='Задание № '
                            stat+=str(i)
                            stat+=' '
                            if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                        number_active_zad[mass_id.index(id)]) == 0:
                                stat+='Пройдено'
                            else:
                                stat+=str(proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],
                                        number_active_zad[mass_id.index(id)]))
                                stat+='/'
                                stat+=kol(number_active_zad[mass_id.index(id)])
                            stat+='\n\n'
                            i+=1

                        vkontakte.method("messages.send",
                                         {"peer_id": id, "message": stat,
                                          "random_id": random.randint(1, 124323125345),
                                          "keyboard": keyboard3.get_keyboard()})


                    else:
                        if id==502570115:
                            st=body
                            i=1
                            while i!=(len(mass_id)):
                                vkontakte.method("messages.send",
                                                 {"peer_id": mass_id[i],
                                                  "message": st,
                                                  "random_id": random.randint(1, 124323125345),
                                                  "keyboard": keyboard.get_keyboard()})
                                i+=1
                        else:
                            vkontakte.method("messages.send",
                                             {"peer_id": id,
                                              "message": "Извини, БОТ еще не может понять данную команду😥",
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard.get_keyboard()})
                if mass_fg[mass_id.index(id)]:
                    messages = vkontakte.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
                    if messages["count"] >= 1:
                        print(mass_id)
                        print(count_id)

                        id = messages["items"][0]["last_message"]["from_id"]
                        body = messages["items"][0]["last_message"]["text"]
                        if body.lower() == 'закончить':
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Надеюсь ты нарешался, возвращайся!✨❤',
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard3.get_keyboard()})
                            mass_fg[mass_id.index(id)]=False
                        elif body.lower() in otv[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]]:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Верно, вот следующее задание✨✅',
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})
                            kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]+=1
                            if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)]) == 0:
                                vkontakte.method("messages.send",
                                                 {"peer_id": id, "message": "Поздравляем, вы выполнили все задания из данного блока🥳✅",
                                                  "random_id": random.randint(1, 124323125345),
                                                  "keyboard": keyboard3.get_keyboard()})
                                mass_fg[mass_id.index(id)] = False
                            else:
                                vkontakte.method("messages.send",
                                                 {"peer_id": id, "message": 'Задание  '+ str(proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)]))+ '/' + kol(number_active_zad[mass_id.index(id)])+ '\n' + zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]].find('.')+1::],
                                                  "random_id": random.randint(1, 124323125345),
                                                  "keyboard": keyboard1.get_keyboard()})

                        elif body.lower()=='узнать ответ':
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Ответ на это задание:'+otv[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]][otv[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]].find('.')+1::],
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard2.get_keyboard()})
                        elif body.lower()=='дальше':
                            kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]+=1
                            if proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)]) == 0:
                                vkontakte.method("messages.send",
                                                 {"peer_id": id, "message": "Поздравляем, выполнили все задания из данного блока",
                                                  "random_id": random.randint(1, 124323125345),
                                                  "keyboard": keyboard3.get_keyboard()})
                                mass_fg[mass_id.index(id)] = False
                            else:
                                vkontakte.method("messages.send",
                                                 {"peer_id": id,
                                                  "message": "Держи следующеее📃\n" + 'Задание  '+ str(proverka(kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]],number_active_zad[mass_id.index(id)]))+ '/' + kol(number_active_zad[mass_id.index(id)])+ '\n' + zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]][zad[kolvo_zad[mass_id.index(id)][number_active_zad[mass_id.index(id)]]].find('.')+1::],
                                                  "random_id": random.randint(1, 124323125345),
                                                  "keyboard": keyboard1.get_keyboard()})

                        else:
                            vkontakte.method("messages.send",
                                             {"peer_id": id, "message": 'Ответ неверный',
                                              "random_id": random.randint(1, 124323125345),
                                              "keyboard": keyboard1.get_keyboard()})

    except Exception as E:
        print("Except")
        time.sleep(1)




