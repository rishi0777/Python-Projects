import random
from tkinter import *
from PIL import ImageTk,Image
#import pygame
from pygame import mixer

#Global Variables ##############################################################################
paragraph=["Medieval period is an important period in the history of India because of the developments in the field of art and languages,culture and religion. Beginning of Medieval period is marked by the rise of the Rajput clan. This period is also referred to as Postclassical Era. Medieval period lasted from the 8th to the 18th century CE with early medieval period from the 8th to the 13th century and the late medieval period from the 13th to the 18th century. Early Medieval period witnessed wars among regional kingdoms from north and south India where as late medieval period saw the number of Muslim invasions by Mughals,Afghans and Turks. Some scholars believe that start of Mughal Empire is the end of Medieval period in India.",
           "If UFOs were visiting our world, where were these extraterrestrials? Could they be hidden among us? Comic books and television illustrates how possibility of extraterrestrial visitors reflected anxieties of that era.The fear that there might be alien enemies in our midst resonates with fears of Soviets and communists from the McCarthy era. Ultimately, in this story, the humans are the ones who accost and capture the alien woman.The shift in perspective puts the humans in the position of the monsters.Aside from depictions of UFOs in media, UFOs are also part of American folk culture. Ideas of aliens and flying saucers are a part of the mythology of America.",
            "In the annals of the world history, there have been many kings, but none greater than Ashoka. Popularly known as ‘Devanampriya Priyadarsi’ (He who is the beloved of the Gods and who regards everyone amiably), he reigned over most of India, South Asia and beyond. His story tells us that religion can act as a powerful force for the redemption of a human being. According to Buddhist traditions, Ashoka was born as the son of the Mauryan emperor Bindusara by a relatively lower ranked queen named Dharma. The Avadana texts mention that his mother was queen Subhadrangi. He was the grandson of another great king and the founder of the Mauryan dynasty, Chandragupta Maurya. But defying all odds, young Ashoka excelled in military and academic disciplines.",
           "Chanakya is famous in the history of India as a sage-like person who by his political shrewdness and expediency helped in the establishment of the mighty Mauryan empire. Chanakya was wise, clever, foresighted, determined and deeply read in economics, diplomacy and politics. There is a legend that Chanakya was once invited to the court of the Nanda rulers of Magadha where he was insulted. Chanakya took a vow to cause the downfall of the Nanda dynasty. With the help of a brave and capable general Chandragupta  he succeeded in fulfilling his vow and founded a new Mauryan dynasty in Magadha. He expelled the Greek invaders from India with his help again. Chanakya served as a friend, philosopher and guide to Chandragupta Maurya.",
           "Meditation is the practice of thinking deeply in silence, in order to make the mind calm. Through regular mediation, levels of stress can be reduced as well as managed. Meditation is a relaxation technique like yoga and deep breathing that activates the body’s relaxation response. When meditation is practiced regularly, it leads to decrease in our stress levels in everyday life. Meditation gives a boost in our feelings of happiness and calmness. It increases our ability to stay cool, calm and composed under pressure. Effective meditation is free from any kind of other distraction. Research has shown that meditation has benefits on mental health, including decrease in depression, increase in positive emotional state and increases in the ability to deal with unavoidable stressful conditions in life.",
           "The recently discovered Higgs boson, which helps give particles their mass, could have destroyed the cosmos shortly after it was born, causing the universe to collapse just after the Big Bang. But gravity, the force that keeps planets and stars together, might have kept this from happening. In 2012, the detection of the long-sought Higgs boson, also known by its nickname the God particle, at the Large Hadron Collider (LHC), the most powerful particle accelerator on the planet. This particle helps give mass to all elementary particles that have mass, such as electrons and protons. Elementary particles that do not have mass, such as the photons that make up light, do not get mass from the Higgs boson. The experiments that detected the Higgs boson revealed it had a mass of 125 billion electron-volts, or more than 130 times the mass of the proton.",
           "The Universe contains billions of galaxies, each containing millions or billions of stars. The space between the stars and galaxies is largely empty. However, even places far from stars and planets contain scattered particles of dust or a few hydrogen atoms per cubic centimeter. Space is also filled with radiation (e.g. light and heat), magnetic fields and high energy particles (e.g. cosmic rays).The Universe is incredibly huge. It would take a modern jet fighter more than a million years to reach the nearest star to the Sun. Travelling at the speed of light (300,000 km per second), it would take 100,000 years to cross our Milky Way galaxy alone. No one knows the exact size of the Universe, because we cannot see the edge – if there is one. All we do know is that the visible Universe is at least 93 billion light years across.",
           "Spacecraft, vehicle designed to operate, with or without a crew, in a controlled flight pattern above Earth’s lower atmosphere. Actual vehicles are designed with a variety of shapes depending on the mission. The first spacecraft, the Soviet Union’s Sputnik 1, was launched on October 4, 1957; it weighed 83.6 kg (184 pounds). It was soon followed by other unmanned Soviet and U.S. spacecraft and, within four years (April 12, 1961), by the first manned spacecraft, Vostok 1, which carried the Soviet cosmonaut Yury Gagarin. Since then, numerous other manned and unmanned craft have been launched to increase scientific knowledge, augment national security, or provide important services in areas such as telecommunications and weather forecasting.",
           "The Milky Way is the galaxy that includes our Solar System, with the name describing the galaxy's appearance from Earth: a hazy band of light seen in the night sky formed from stars that cannot be individually distinguished by the naked eye. From Earth, the Milky Way appears as a band because its disk-shaped structure is viewed from within. Galileo Galilei first resolved the band of light into individual stars with his telescope in 1610. Until the early 1920s, most astronomers thought that the Milky Way contained all the stars in the Universe. Following the 1920 Great Debate between the astronomers Harlow Shapley and Heber Curtis, observations by Edwin Hubble showed that the Milky Way is just one of many galaxies. The Milky Way is a barred spiral galaxy with an estimated visible diameter of 100,000–200,000 light-years.",
           "On average, a supernova will occur about once every 50 years in a galaxy the size of the Milky Way. Put another way, a star explodes every second or so somewhere in the universe, and some of those aren't too far from Earth. About 10 million years ago, a cluster of supernovae created the “Local Bubble,” a 300-light-year long, peanut-shaped bubble of gas in the interstellar medium that surrounds the solar system. Exactly how a star dies depends in part on its mass. Our sun, for example, doesn't have enough mass to explode as a supernova (though the news for Earth still isn't good, because once the sun runs out of its nuclear fuel, perhaps in a couple billion years, it will swell into a red giant that will likely vaporize our world, before gradually cooling into a white dwarf). But with the right amount of mass, a star can burn out in a fiery explosion."
           ]
main_label_count=0
beg_counter_i=0
time_left=3
str_para=""
head_char=""
total_words=0

#FUNCTIONS ###########################################################################################
def music_start():
    mixer.music.load("./res/game.mp3")
    mixer.music.play(loops=1000)

def headslider():

    global main_label_count, head_char
    text="GO FAST"
    if(main_label_count>=len(text)):
        main_label_count=0
        head_char=""
    head_char+=text[main_label_count]
    main_label_count+=1
    head_label.configure(text=head_char)
    head_label.after(250,headslider)

def random_para():
    global str_para,main_label_count,head_char,total_words,hit,miss,time_left
    time_left=120
    main_label_count=0
    total_words=0
    head_char=""
    hit=0
    miss=0

    count=0
    n_str=""
    random.shuffle(paragraph)
    str_para=paragraph[0]
    list_para=str_para.split()
    for ch in str_para:
        if count>=120 and count<=135:
            if ch==" ":
                n_str+="\n"
                count=0
        count+=1
        n_str += ch
    for word in list_para:
        total_words+=1

    start_button.destroy()
    timer_label.place(x=m_width - 100, y=60)
    para_label.configure(text=n_str)
    para_label.place(x=0, y=140)
    para_entry.place(x=40, y=380)
    para_entry.focus_set()

    timer()

    

def beg_counter():
    def counter():
        global beg_counter_i
        if(beg_counter_i<3):
            counter_label.configure(text=arr[beg_counter_i])
            beg_counter_i+=1
            counter_label.after(1000, counter)
        else:
            random_para()
            counter_label.place_forget()

    counter_label = Label(root, text="", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 30,"bold"))
    arr = ["    3    ", "    2    ", "    1    "]
    start_button.destroy()
    counter_label.place(x=(m_width / 2) - 75, y=(m_height / 2) - 60)
    counter()

def start_game():
    beg_counter()
def retry_game():
    score_label.place_forget()
    timer_label.configure(fg="#FFFFFF")
    time_over_label.place_forget()
    retry_button.place_forget()
    para_entry.delete("1.0",END)
    beg_counter()
def quit_game():
    root.destroy()

def check():
    global str_para
    hit1=0
    miss1=0
    written=para_entry.get("1.0",END)
    words=written.split()
    actual_words=str_para.split()
    i=0
    while (i<len(words)):
        if(words[i]==actual_words[i]):
            hit1+=1
        else:
            miss1+=1
        i+=1

    return hit1,miss1

def timer():
    global time_left,total_words
    if(time_left>1):
        if (time_left == 10):
            timer_label.configure(fg="red")
        time_left-=1
        timer_label.configure(text=time_left)
        timer_label.after(1000,timer)
    else:
        hit,miss=check()
        check_accuracy=0
        type_speed=0

        if(hit==0 and miss==0):
            check_accuracy = round((0) * 100, 2)
            type_speed = round((hit / 60) * 100, 2)
        else:
            check_accuracy= round((hit/(miss+hit))*100,2) 
            type_speed = round(((hit/total_words)/2)*100,2)
        
        
        score_label.configure(text=" ACCURACY {}  ||  SPEED {} ".format(check_accuracy,type_speed))
        score_label.place(x=(m_width / 2) - 190, y=(m_height / 2)-120)
        
        time_over_label.place(x=(m_width / 2) - 90, y=(m_height / 2)-60)
        retry_button.place(x=(m_width / 2)-45, y=(m_height / 2) +20)
        quit_button.place(x=(m_width / 2)-45, y=(m_height / 2) +95)

        para_label.place_forget()
        para_entry.place_forget()
        timer_label.place_forget()





#Root Container ##############################################################################
root=Tk()
m_width=root.winfo_screenwidth()
m_height=root.winfo_screenheight()
root.attributes('-fullscreen', True)
root.bind('<Escape>', lambda event: root.destroy())
root.title("GO FAST")
root.configure(bg="#2b2a33")
root.iconbitmap('./res/icon.ico')


#MAIN Button ##############################################################################
head_label=Label(root, text="", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 30, "bold"),width=8)
head_label.place(x=(m_width/2)-90,y=10)

start_button=Button(root, text="START", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 30, "bold"),width=8,command=start_game)
start_button.place(x=(m_width/2)-75,y=(m_height/2)-60)

retry_button=Button(root, text="RETRY", bg="#1e1d27", fg="#FFFFFF", font=("Comic Sans MS", 20, "bold"),width=8,command=retry_game)
quit_button=Button(root, text="QUIT", bg="#1e1d27", fg="#FFFFFF", font=("Comic Sans MS", 20, "bold"),width=8,command=quit_game)

#Label  #############################################################################
timer_label=Label(root,text="", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 30))
para_label=Label(root,bg="#2b2a33",fg="#FFFFFF", text="",font=("Comic Sans MS", 17, ""),height=7,width=108)
para_entry=Text(root,fg="#2b2a33",font=("Comic Sans MS",18,""),bd=8,height=10,width=95)
score_label=Label(root, text="{}", bg="#1e1d27", fg="#FFFFFF", font=("Comic Sans MS", 20, "bold"))
time_over_label=Label(root, text="TIME OVER ", bg="#1e1d27", fg="#FFFFFF", font=("Comic Sans MS", 30, "bold"))

footer_label=Label(root,text="DEVELOPED BY ", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 15))
footer_label_name=Label(root,text="RISHI MISHRA", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 15))
footer_label_close=Label(root,text="PRESS ESC KEY TO CLOSE", bg="#2b2a33", fg="#FFFFFF", font=("Comic Sans MS", 15))

header_img_logo=ImageTk.PhotoImage(Image.open('./res/gofast_logo.png'))
header_img_logo_label=Label(root,bg="#2b2a33",image=header_img_logo)
footer_img_logo=ImageTk.PhotoImage(Image.open('./res/logo_rm.png'))
footer_img_logo_label=Label(root,bg="#2b2a33",image=footer_img_logo)

header_img_logo_label.place(x=(m_width/2)-170,y=10)

footer_label_close.place(x=20,y=m_height-65)
footer_label.place(x=m_width/2+360,y=m_height-65)
footer_img_logo_label.place(x=m_width/2+515,y=m_height-80)
footer_label_name.place(x=m_width/2+585,y=m_height-65)


#main_working #######################################################################################
mixer.init()
music_start()
headslider()
root.mainloop()
