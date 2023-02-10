num = input()

print(True if num.isdigit() else False) #- теренарный оператор, в нем живет if else,-
    #если          #посередине     #иначе                           -только в строку
    #истина        #условие        #лож


num = input() 

num = int(num) if num.isdigit() else num #- работа с присваиванием int или str
print(type(num))