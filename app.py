from flask import Flask, render_template, redirect, url_for, send_file
from myCondicaoTempo import myCondicaoTempo
from myRele import MyRele
import datetime
import time
import pprint
from dateutil import parser
import matplotlib
from matplotlib import pyplot
from cStringIO import StringIO
from myStepper import myStepper
from myUltrasonic import myUltrasonic

app = Flask(__name__)


@app.route('/')
def index():
    m = myCondicaoTempo()
    humidade = m.getHumidade()
    temperatura = m.getTemperatura()
    chuva = m.getChuva()
    dataHora = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    rele1 = MyRele(14)
    checkLuz = rele1.check()
    if checkLuz :
        rele1Link = '/luz/on'
        rele1Tittle = 'Ligar Luz'
    else:
        rele1Link = '/luz/off'
        rele1Tittle = 'Desligar Luz'
#    rele2 = MyRele(15)
#    checkMotor = rele2.check()
#    if checkMotor :
#        rele2Link = '/motor/on'
#        rele2Tittle = 'Ligar motor'
#    else:
#        rele2Link = '/motor/off'
#        rele2Tittle = 'Desligar Motor'
#    ultrasonic = myUltrasonic(9,10)
#    distancia = ultrasonic.medir()
#    temcomida = 40 - distancia
#    porcentagem = ( ( distancia * ( 100 / 40 ) ) - 100 ) * (+1)
    templateData = {
            'humidade':  humidade,
            'temperatura': temperatura,
            'chuva': chuva,
            'date': dataHora,
            'rele1Link': rele1Link,
            'rele1Tittle': rele1Tittle,

#           'rele2Link': rele2Link,
#            'rele2Tittle': rele2Tittle,
#            'qtdePote': temcomida,
#            'porcentagemPote':porcentagem
            }
    return render_template('humidade.html', **templateData)

@app.route('/humidade')
def humidade():
    m = myCondicaoTempo()
    humidade = m.getHumidade()
    return render_template('humidade.html', humidade=humidade)

def grafico(image):
   m = myCondicaoTempo()
   temperaturas = m.getTemperaturas()
   datas = m.getTimes()
   print(len(datas))
   print(len(temperaturas))
   pyplot.plot(datas,temperaturas)
   #ipyplot.ylabel('Temperatura')
   #plt.xlabel('Data')
   pylot.savefig(image, format='png')

@app.route('/image.png')
def image_png():
    image = StringIO()
    grafico(image)
    image.seek(0)
    return send_file(image, attachment_filename="image.png", as_attachment=True)

@app.route('/graf')
def graf():
    return '<img src="image.png">'

@app.route('/luz/<action>')
def luz(action):
    c = MyRele(14)
    if action == "on":
        c.on()
    else:
        c.off()
    return redirect('/')

@app.route('/motor/<action>')
def motor(action):
    c = MyRele(15)
    if action == "on":
        c.on()
    else:
        c.off()
    return redirect('/')


@app.route('/passo/<action>/<voltas>')
def passo(action,voltas):
    passo = myStepper()
    if action == "go":
        passo.go(voltas)
    else:
        passo.back(voltas)
    return redirect('/')

@app.route('/alimentar')
def alimentar():
    passo = myStepper()
    passo.back(2)
    time.sleep(5)
    passo.go(2)
    return redirect('/')

@app.route('/subir')
def subir():
    passo = myStepper()
    passo.go(1)

@app.route('/descer')
def descer():
    passo = myStepper()
    passo.back(1)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
