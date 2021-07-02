from django.shortcuts import render
import pyrebase
import cv2
from PIL import Image

config = {
    'apiKey': "AIzaSyCF9kLyM_JQoDoP1s5BT5F9Y3N-vk-bJx4",
    'authDomain': "scucodeforgood.firebaseapp.com",
    'databaseURL': "https://scucodeforgood-default-rtdb.firebaseio.com",
    'projectId': "scucodeforgood",
    'storageBucket': "scucodeforgood.appspot.com",
    'messagingSenderId': "632464421365",
    'appId': "1:632464421365:web:27bf0c120b8c1c75d670bc",
    'measurementId': "G-32TZ1KM8DL"
}
firebase = pyrebase.initialize_app(config)
store = firebase.storage()
img1 = store.child("ece_pg2_admin/WhatsApp Image 2021-07-02 at 12.20.05 AM (1).jpeg").get_url(None)
img2 = store.child("ece_pg2_admin/WhatsApp Image 2021-07-02 at 12.20.05 AM.jpeg").get_url(None)
img3 = store.child("ece_pg2_admin/WhatsApp Image 2021-07-02 at 1.09.09 AM.jpeg").get_url(None)

def pg2(request):
    if request.method== 'POST':
        name = request.POST['name']
        date = request.POST['doa']
        pic = request.POST['upload']
        #pic.show()
        #store.child('ece_pg2_admin/Achievements/'+name+'_Achievements').put(pic)
        
        return render(request , "Pg2.html", {'eceboys':img1, 'ece2yr':img2, 'ecegirls':img3 })
    else:
        return render(request , "Pg2.html", {'eceboys':img1, 'ece2yr':img2, 'ecegirls':img3 })


