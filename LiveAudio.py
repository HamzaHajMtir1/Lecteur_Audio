import pyttsx3
import PyPDF3

droid = pyttsx3.init()
droid.say("Hello Hamza , i'm droid from generation 3")
droid.say("Now you can relax and listen quietly")
livre = open('D:\python\AI\Lecteur Audio\A93p183.pdf','rb')
lecture = PyPDF3.PdfFileReader(livre)
page = lecture.numPages
print(page)

debutlecture = lecture.getPage(0)
texte = debutlecture.extractText()
droid.say(texte)
droid.runAndWait()