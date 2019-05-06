#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gtts import gTTS
import os
import time
import pyautogui

part_lst = ["feet", "calves", "thighs", "adbomen", "torso and back", "upper arm", "lower arm", "fist" "neck", "head"]
feet_bone_lst = {"phalanges distales": 5,
                 "phalanges moyennes": 4,
                 "phalanges proximal": 5,
                 "os métatarsien": 5,
                 "os sésamoide": 2,
                 "os cunéiforme médial ": 3,
                 "Naviculaire": 1,
                 "Cuboïde": 1,
                 "Calcanéus": 1,
                 "Talus": 1

                 }

leg_bon_lst = {'Fibula': 1,
               'Tibia': 1,
               'Patella': 1,
               'fémure': 1}

pelvis_bone_lst = {
    'coccyx': 1,
    'sacrum': 1,
    'ossa coxae': 1
}

vertebral_column_lst = {
    'vertebres lombaire': 5,
    'vertebres thoraciques': 12,
    'vertebres cervicales': 7

}

throat_lst = {
    'hyoid': 1
}

throrax_lst = {
    'sternum': 1,
    'cotes': 12
}

crane_facial_lst = {
    'mandibule': 1,
    'maxilla': 2,
    'palatine': 2,
    'zygomatic': 2,
    'nasal': 2,
    'lacrimal': 2,
    'vomer': 1,
    'nasal conchae inférieur': 2
}

crane_cranial_lst = {
    'os frontal': 1,
    'os parietal ': 2,
    'os temporal': 2,
    'os occipital': 2,
    'os sphenoid': 2,
    'os ethmoid': 2
}

middle_ear_lst = {
    'malléus': 2,
    'incus': 2,
    'stapès': 2

}

shoulder_lst = {
    'scapula' : 1,
    'clavicule' : 1
}

arm_lst = {
    'humerus':1,
    'radius':1,
    'ulna':1
}

hand_wrist_lst = {
    'scaphoide':1,
    'lunate':1,
    'triquetrum':1,
    'pisiforme':1,
    'trapeze':1,
    'trapezoide':1,
    'capitatum':1,
    'hamatum':1
}

hand_palm_lst = {
    'os metacarpe' : 5
}

hand_finger_lst = {
    'proximal phalanges': 5,
    'intermediate phalanges':5,
    'distal phalanges':5
}

actions = {"breathe": "clench", "exhale": "release"}

play_list = []


def make_and_play(txt, fname):
    tts = gTTS(text=txt, lang='fr')
    tts.save(fname + "mp3")


def make(txt, pause, file_name=None):
    if not file_name:
        file_name = txt.replace(' ','_') + ".mp3"
    play_list.append((file_name, pause))
    f_path = full_path(file_name)
    if os.path.isfile(f_path):
        return
    tts = gTTS(text=txt, lang='fr')
    tts.save(f_path)

def full_path(f):
    return os.path.join(audio_path, f)


# full_text = ""
# for i in range(len(part_lst)):
#     for action in actions.keys():
#         pause = (len(part_lst) - 1 -i)*0.2
#         make(action , pause )
#         for j in range(i+1):
#             full_text += actions[action] + " " + part_lst[j] + "."
#             make(full_text, pause/2)
#
# for f in play_list:
#     os.system("mpg123 "+ f[0])
#     time.sleep(f[1])

my_training_old = {
    'pied' : feet_bone_lst ,
    'jambe' : leg_bon_lst,
    'bassins' : pelvis_bone_lst,
    'colonne vertebrale' : vertebral_column_lst,
    'thorax' : throrax_lst,
    'gorge' : throat_lst
}

my_training_head = {
        'crane craniale' : crane_cranial_lst,
        'crane facialle': crane_facial_lst,
        'oreille moyenne': middle_ear_lst
}

arm_training = {
        'epaule':shoulder_lst,
        'bras': arm_lst,
        'poignet' : hand_wrist_lst,
        'paume ': hand_palm_lst,
        'doights': hand_finger_lst,

}
def play(pl):
    for i, f in enumerate(pl):
        print(i,f)
        pyautogui.moveRel(-1 if i%2 else 1,0) 
        os.system("mpg123 " + full_path(f[0]))
        time.sleep(f[1])

def allonger_membre(membre, extremity, nb):
    for i in range(nb):
        direction = ['le haut', 'l extérieur', 'l intérieur']
        ppied = 'tendues'   
        if i % 2 == 0 : 
            ppied = 'fléchie'
            direction[1], direction[2] = direction[2], direction[1]
              
        for p in ['droite', 'gauche']:
            for d in direction:
                make("tendez la {0} {1} vers {2} {3} {4}".format(membre,p, d, extremity, ppied), 4)


audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Audio')


today_training = {}
today_training.update(my_training_head)



for name, bones in today_training.items():
    make("pour les " + str(sum(bones.values())) + " os du " + name,
         1,
         'sum_' + name.replace(' ', '_'))
    for i, k in enumerate(bones.keys()):
        for mov in ['inspirez', 'expirez']:
            string = "{0} dans vos {1} {2}".format(mov, bones[k] , k)
            filename = str(i).zfill(3) + "_" + mov[0] + "_"  + k.replace(' ', '') + ".mp3" 
            print(i, k)
            make(string, 4, filename)




make('deplacez vous au sol', 3* 60)
make('deplacez vous au niveau intermédiare', 3*60)
make('deplacez vous debout', 3 *60)

make('repos', 1)
play(play_list)
exit()

make('repos', 30)

it = 5
gainage_t = 15

for action in ['pompes russe', 'relevé de buste', 'squate', 'pompe', 'tractions']:
    for i in range(3):
        make('faites {0} {1}'.format(it, action), 2)
        for j in range(it):
            make(str(j), 2)

        make('gainage', 1)
        for j in range(gainage_t):
            make(str(j), 1)

make('repos', 20)


make('faites 10 mini tractions', 10 * 3) 



