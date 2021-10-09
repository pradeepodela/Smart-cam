import cv2
import numpy as np
import face_recognition
import streamlit as st
import os
from datetime import datetime
import pandas as pd
import smtplib
from email.message import EmailMessage
import imghdr

email = ''
path = './Training_images'
images = []
classNames = []
myList = os.listdir(path)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def email_me(frame,mail,time):
    Sender_Email = "odelapradeep12@gmail.com"
    Reciever_Email = mail
    Password = '@pradeep9246'
    img = frame
    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Accused found !!!!!!!" 
    newMessage['From'] = Sender_Email                   
    newMessage['To'] = Reciever_Email                   
    newMessage.set_content(f'The following accused found at Time {time} at area Hyderabad here is the picture of accused ') 

    with open(img, 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name

    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        
        smtp.login(Sender_Email, Password)              
        smtp.send_message(newMessage)
    print('success msg went')

def markAttendance(name,image,email):
    with open('data.csv', 'r+') as f:
        myDataList = f.readlines()


        nameList = []
        for line in myDataList:
            df = pd.read_csv(r'data.csv')
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M')
                n_input = name
                TIME = df[(df == n_input).any(1)].stack()[lambda x: x != n_input].unique()
                
                if dtString not in list(TIME):
                   
                    f.writelines(f'\n{name},{dtString}')
                    
                    time_now = dtString.replace(':','.')
                    try:
                        cv2.imwrite(f'accused_pics/{time_now}.png',image)
                        email_me(f'accused_pics/{time_now}.png',email,dtString)
                    except :
                        print('could not save image')



encodeListKnown = findEncodings(images)
print('Encoding Completed')

# st.markdown('**Accused detecation started**')
def atn(frame,eml):
    #st.sidebar.text('**Accused detecation started**')
    email = eml
    
    print('accused detecation started')
    
    
    
    imgS = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name,frame,email)
            
    return frame

