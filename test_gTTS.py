from gtts import gTTS
import os
import time

part_lst = ["feet", "calves", "thighs", "adbomen", "torso and back", "upper arm", "lower arm", "fist" "neck", "head"]
feet_bone_lst = {"phalanges distales": 5,
                 "phalanges moyennes": 4,
                 "phalanges proximal": 5,
                 "os métatarsien": 5,
                 "os sésamoide  latéral": 1,
                 "os sésamoide  médial": 1,
                 "Os cunéiforme Médial": 1,
                 "Os cunéiforme Intermédiaire": 1,
                 "Os cunéiforme Latéral": 1,
                 "Naviculaire": 1,
                 "Cuboïde": 1,
                 "Calcanéus": 1,
                 "Talus": 1

                 }

leg_bon_lst = {'Fibula': 1,
               'Tibia': 1,
               'Patella': 1,
               'Femure': 1}

pelvis_bone_lst = {
    'coccyx': 1,
    'sacrum': 1,
    'ossa coxae': 1
}

vertebral_column_lst = {
    'vertebres lombaire': 5,
    'vertebres thorariques': 12,
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
    'malleus': 2,
    'incus': 2,
    'stapes': 2

}

shoulder_lst = {
    'scapula' : 1,
    'clavicule' : 1
}

arms_lst = {
    'humerus':1,
    'radius':1,
    'ulna':1
}

hand_wrist_lst = {
    'scaphoid':1,
    'lunate':1,
    'triquetral':1,
    'pisiform':1,
    'trapezium':1,
    'trapezoid':1,
    'capitate':1,
    'hamate':1
}

hand_palm_lst = {
    'os metacarpe' : 5
}

hand_finger_lst = {
    'proximal phalanges': 5,
    'intermediate phalanges':5,
    'distal phalanges':5
}

shoulder_lst = {
    'scapula': 1,
    'clavicule': 1
}

actions = {"breathe": "clench", "exhale": "release"}

play_list = []


def make_and_play(txt, fname):
    tts = gTTS(text=txt, lang='fr')
    tts.save(fname + "mp3")


def make(txt, pause, file_name=None):
    play_list.append((file_name, pause))
    if not file_name:
        file_name = "f" + str(len(play_list)) + ".mp3"
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
    'throrax' : throrax_lst,
    'gorge' : throat_lst
}

my_training_short = {
        'crane craniale' : crane_cranial_lst,
        'crane facialle': crane_facial_lst
}

audio_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Audio')

for name, bones in my_training_short.items():
    make("pour les " + str(sum(bones.values())) + " os du " + name,
         1,
         'sum_' + name.replace(' ', '_'))
    for i, k in enumerate(bones.keys()):
        print(i, k)
        make("inspirez dans vos " + k, 4, str(i).zfill(3) + "_i_" + k.replace(' ', '') + ".mp3")
        make("Expirez dans vos " + k, 4, str(i).zfill(3) + "_e_" + k.replace(' ', '') + ".mp3")

for f in play_list:
    print()
    os.system("mpg123 " + full_path(f[0]))
    time.sleep(f[1])
