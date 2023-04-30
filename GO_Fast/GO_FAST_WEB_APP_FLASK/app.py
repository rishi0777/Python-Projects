from re import U
from flask import Flask,render_template,request,redirect,flash

from datetime import date
import random
import secrets

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics


app=Flask(__name__)
app.config['SECRET_KEY'] = "a0e07a5d0eb818d1453f16bac1bf967d"

########################################################################### GLOBAL_VAR
paragraph=["Medieval period is an important period in the history of India because of the developments in the field of art and languages,culture and religion. Beginning of Medieval period is marked by the rise of the Rajput clan. This period is also referred to as Postclassical Era. Medieval period lasted from the 8th to the 18th century CE with early medieval period from the 8th to the 13th century and the late medieval period from the 13th to the 18th century. Early Medieval period witnessed wars among regional kingdoms from north and south India where as late medieval period saw the number of Muslim invasions by Mughals,Afghans and Turks. Some scholars believe that start of Mughal Empire is the end of Medieval period in India.",
           "If UFOs were visiting our world, where were these extraterrestrials? Could they be hidden among us? Comic books and television illustrates how possibility of extraterrestrial visitors reflected anxieties of that era.The fear that there might be alien enemies in our midst resonates with fears of Soviets and communists from the McCarthy era. Ultimately, in this story, the humans are the ones who accost and capture the alien woman.The shift in perspective puts the humans in the position of the monsters.Aside from depictions of UFOs in media, UFOs are also part of American folk culture. Ideas of aliens and flying saucers are a part of the mythology of America.",
            "In the annals of the world history, there have been many kings, but none greater than Ashoka. Popularly known as ‘Devanampriya Priyadarsi’ (He who is the beloved of the Gods and who regards everyone amiably), he reigned over most of India, South Asia and beyond. His story tells us that religion can act as a powerful force for the redemption of a human being. According to Buddhist traditions, Ashoka was born as the son of the Mauryan emperor Bindusara by a relatively lower ranked queen named Dharma. The Avadana texts mention that his mother was queen Subhadrangi. He was the grandson of another great king and the founder of the Mauryan dynasty, Chandragupta Maurya. But defying all odds, young Ashoka excelled in military and academic disciplines.",
           "Chanakya is famous in the history of India as a sage-like person who by his political shrewdness and expediency helped in the establishment of the mighty Mauryan empire. Chanakya was wise, clever, foresighted, determined and deeply read in economics, diplomacy and politics. There is a legend that Chanakya was once invited to the court of the Nanda rulers of Magadha where he was insulted. Chanakya took a vow to cause the downfall of the Nanda dynasty. With the help of a brave and capable general Chandragupta  he succeeded in fulfilling his vow and founded a new Mauryan dynasty in Magadha. He expelled the Greek invaders from India with his help again. Chanakya served as a friend, philosopher and guide to Chandragupta Maurya.",
           "Meditation is the practice of thinking deeply in silence, in order to make the mind calm. Through regular mediation, levels of stress can be reduced as well as managed. Meditation is a relaxation technique like yoga and deep breathing that activates the body’s relaxation response. When meditation is practiced regularly, it leads to decrease in our stress levels in everyday life. Meditation gives a boost in our feelings of happiness and calmness. It increases our ability to stay cool, calm and composed under pressure. Effective meditation is free from any kind of other distraction. Research has shown that meditation has benefits on mental health, including decrease in depression, increase in positive emotional state and increases in the ability to deal with unavoidable stressful conditions in life.",
           "The recently discovered Higgs boson, which helps give particles their mass, could have destroyed the cosmos shortly after it was born, causing the universe to collapse just after the Big Bang. But gravity, the force that keeps planets and stars together, might have kept this from happening. In 2012, the detection of the long-sought Higgs boson, also known by its nickname the God particle, at the Large Hadron Collider (LHC), the most powerful particle accelerator on the planet. This particle helps give mass to all elementary particles that have mass, such as electrons and protons. Elementary particles that do not have mass, such as the photons that make up light, do not get mass from the Higgs boson. The experiments that detected the Higgs boson revealed it had a mass of 125 billion electron-volts, or more than 130 times the mass of the proton.",
           "The Universe contains billions of galaxies, each containing millions or billions of stars. The space between the stars and galaxies is largely empty. However, even places far from stars and planets contain scattered particles of dust or a few hydrogen atoms per cubic centimeter. Space is also filled with radiation (e.g. light and heat), magnetic fields and high energy particles (e.g. cosmic rays).The Universe is incredibly huge. It would take a modern jet fighter more than a million years to reach the nearest star to the Sun. Travelling at the speed of light (300,000 km per second), it would take 100,000 years to cross our Milky Way galaxy alone. No one knows the exact size of the Universe, because we cannot see the edge – if there is one. All we do know is that the visible Universe is at least 93 billion light years across.",
           "Spacecraft, vehicle designed to operate, with or without a crew, in a controlled flight pattern above Earth’s lower atmosphere. Actual vehicles are designed with a variety of shapes depending on the mission. The first spacecraft, the Soviet Union’s Sputnik 1, was launched on October 4, 1957; it weighed 83.6 kg (184 pounds). It was soon followed by other unmanned Soviet and U.S. spacecraft and, within four years (April 12, 1961), by the first manned spacecraft, Vostok 1, which carried the Soviet cosmonaut Yury Gagarin. Since then, numerous other manned and unmanned craft have been launched to increase scientific knowledge, augment national security, or provide important services in areas such as telecommunications and weather forecasting.",
           "The Milky Way is the galaxy that includes our Solar System, with the name describing the galaxy's appearance from Earth: a hazy band of light seen in the night sky formed from stars that cannot be individually distinguished by the naked eye. From Earth, the Milky Way appears as a band because its disk-shaped structure is viewed from within. Galileo Galilei first resolved the band of light into individual stars with his telescope in 1610. Until the early 1920s, most astronomers thought that the Milky Way contained all the stars in the Universe. Following the 1920 Great Debate between the astronomers Harlow Shapley and Heber Curtis, observations by Edwin Hubble showed that the Milky Way is just one of many galaxies. The Milky Way is a barred spiral galaxy with an estimated visible diameter of 100,000–200,000 light-years.",
           "On an average, a supernova will occur about once every 50 years in a galaxy the size of the Milky Way. Put another way, a star explodes every second or so somewhere in the universe, and some of those aren't too far from Earth. About 10 million years ago, a cluster of supernovae created the “Local Bubble,” a 300-light-year long, peanut-shaped bubble of gas in the interstellar medium that surrounds the solar system. Exactly how a star dies depends in part on its mass. Our sun, for example, doesn't have enough mass to explode as a supernova (though the news for Earth still isn't good, because once the sun runs out of its nuclear fuel, perhaps in a couple billion years, it will swell into a red giant that will likely vaporize our world, before gradually cooling into a white dwarf). But with the right amount of mass, a star can burn out in a fiery explosion."
           ]
str_para=""
accuracy=0
type_speed=0

unique_addr_test=secrets.token_hex(20)
unique_addr_submit=secrets.token_hex(20)
unique_addr_cert=secrets.token_hex(15)
main_flag_test=0
###################################################################################### FLASK_FORM_CLASS
class speed_test_form(FlaskForm):
    entry=StringField('Text',widget=TextArea(),validators=[DataRequired()])

class result_cert_form(FlaskForm):
    user_name=StringField('NAME',validators=[DataRequired(), Length(min=3,max=100)])
    user_email=StringField('EMAIL',validators=[DataRequired(), Length(min=5,max=200)])
    user_college=StringField('COLLEGE',validators=[DataRequired(), Length(min=5,max=200)])
    result_submit= SubmitField('GENERATE CERTIFICATE')

####################################################################################### REQ_FUNC
def random_para():
    global str_para,total_words
    random.shuffle(paragraph)
    str_para=paragraph[0]    

def check(user_has_written):
    global hit,miss,str_para,total_words,accuracy,type_speed
    list_para=str_para.split()
    total_words=len(list_para)
    hit=0
    miss=0
    written=user_has_written
    words=written.split()
    actual_words=str_para.split()
    i=0
    while (i<len(words)):
        if(words[i]==actual_words[i]):
            hit+=1
        else:
            miss+=1
            #print(actual_words[i],words[i])
        i+=1
    if(hit==0 and miss==0):
            accuracy = round((0) * 100, 2)
            type_speed = round(((hit / total_words)/2) * 100, 2)
    else:
       accuracy= round((hit/(miss+hit))*100,2) 
       type_speed = round((((hit+(miss*0.3))/total_words)/2)*100,2)

    #print(written)
    #print(hit,miss,total_words)
    #print(accuracy,type_speed)

def pdf_c(name,c_name,u_accuracy,u_speed):
 
    packet = io.BytesIO()
    # create a new PDF with Reportlab
    can = canvas.Canvas(packet, pagesize=letter)
    pdfmetrics.registerFont(TTFont('name_font', 'static/font/extra_bold.ttf'))#giving the source of font
    pdfmetrics.registerFont(TTFont('date_font', 'static/font/semi_bold.ttf'))
    can.setFillColorRGB(0.66,0.48,0.20) #font colour for name and everything
    can.setFont('name_font', 37) #font type and font size for name
    #drawing string on that canvas
    name=name.upper()
    can.drawString(320, 287, name)
    can.setFillColorRGB(0.48,0.47,0.49)
    can.setFont('date_font', 12) #font type type for date and everything
    if c_name=="AMITY UNIVERSITY" or c_name==" AMITY UNIVERSITY " or c_name=="AMITY UNIVERSITY ":
        c_name="AMITY UNIVERSITY"
    elif len(c_name)>14:
	    c_name=c_name[0:14]+'. '
    else: 
	    c_name=c_name
    c_name=c_name.upper()
    can.drawString(172, 251, c_name)
    accuracy_new=str(u_accuracy)
    speed_new=str(u_speed)
    can.drawString(246, 234, accuracy_new)
    can.drawString(429, 234, speed_new)

    can.setFont('date_font', 13)
    today=date.today()
    today=today.strftime("%d/%m/%Y")
    can.drawString(260, 148, today)
    can.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)#passing the created canvas in new_pdf
    existing_pdf = PdfFileReader(open("static/certificate/cert.pdf", "rb")) # reading existing PDF
    merged_pdf = PdfFileWriter() #creating a new pdf file on which we will place both new_pdf and existing_pdf
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    merged_pdf.addPage(page)
    
    # finally, write "output" to a real file
    outputStream = open("static/certificate/created/GO FAST.pdf", "wb")#destination
    merged_pdf.write(outputStream) 
    outputStream.close()

####################################################################################### ROUTES
#HOME PAGE
@app.route("/",methods=['GET','POST'])
def index():
    global main_flag_test
    main_flag_test=1
    return render_template("index.html",main_flag_test=main_flag_test) 

#REGISTER
@app.route("/register")
def register():
    return render_template("register.html",main_flag_test=main_flag_test) 

#TEST
@app.route('/speed')
def speed_test():
    global main_flag_test
    random_para()
    form=speed_test_form() #object passed here is irrelevant
    main_flag_test=1
    return render_template("speed.html",str_para=str_para,form=form,main_flag_test=main_flag_test) 

#RESULT (result button of speed will redirect to this url)
@app.route("/submit/<int:flag_t>",methods=['GET','POST'])
def submit(flag_t):
    global main_flag_test
    form=speed_test_form()
    if  flag_t==1:
        if request.method=="POST":
            form_cert=result_cert_form()
            user_wrote=form.entry.data
            check(user_wrote)
            form.entry.data=""
            return render_template("result.html",accuracy=accuracy,speed=type_speed,main_flag_test=main_flag_test,
            cform=form_cert) 
        else:
            return render_template("default.html") 
    return render_template("default.html") 

#CERTIFICATE
@app.route('/submit/<int:flag_t>/cerificate/',methods=['GET','POST'])
def cert(flag_t):
    addr='/submit/'+str(flag_t)+'/cerificate/'
    if(flag_t==1):
        main_flag_test=0
        cform=result_cert_form()
        if request.method=="POST":
            if cform.validate_on_submit():
                u_name=cform.user_name.data
                u_email= cform.user_email.data
                u_college = cform.user_college.data
                pdf_c(u_name,u_college,accuracy,type_speed)
                return render_template("show_certificate.html")
            else:   
                return render_template("certificate.html",cform=cform,addr=addr)
        else:
            return render_template("certificate.html",cform=cform,addr=addr)
    else:
        return render_template("default.html")

######################################################################## MAIN APP RUN
if __name__=="__main__":
    app.run(debug=True,port=8000)
