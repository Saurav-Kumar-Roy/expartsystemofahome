from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.

def home(request):
    return render(request,'index.html')

def expart(request,sec):
    questions={
        "W":{'ques':"Is it Day or night","url1":"WD","b1":"day","url2":"WN","b2":"night",'heading':'Weather Expart'},
        "WD":{'ques':"Is it raining","url1":"WDR","b1":"Yes","url2":"WDNR","b2":"No",'heading':'Weather Expart'},
        "WDR":{'ques':"Is it there Storm?","url1":"WDRSDec","b1":"Yes","url2":"WDRDec","b2":"No",'heading':'Weather Expart'},
        "WDNR":{'ques':"Is it Sunny or Cloudy","url1":"WDS","b1":"Sunny","url2":"WDCDec","b2":"Cloudy",'heading':'Weather Expart'},
        "WDS":{'ques':"Is There Wind","url1":"WDSWDec","b1":"Yes","url2":"WDSDec","b2":"No",'heading':'Weather Expart'},
        "WN":{'ques':"Is it raining or clear sky?","url1":"WNRDec","b1":"Rain","url2":"WNFDec","b2":"FullMoon",'heading':'Weather Expart'},

        "0":{'ques':"Nothing special is happening.",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision'},
        "WDRDec":{'ques':"closs the window. Turn off AC",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WDRSDec":{'ques':"close all the window.Ready standby Power",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WDSDec":{'ques':"close the window to prevent sun ray. Turn on AC.",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WDSWDec":{'ques':"open the window. Turn off AC",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WDCDec":{'ques':"take precautions for rain, Turn On the lights.",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WNRDec":{'ques':"close the doors and windows",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},
        "WNFDec":{'ques':"open the window.",'url1':'#','b1':'','url2':'#','b2':'','heading':'Decision of Expart'},

        "S":{'ques':"Is there any person around or in the hosue?","url1":"Y","b1":"yes","url2":"NDec","b2":"no",'heading':'Security Expart'},
        "Y":{'ques':"Is the person Known or Unkown?","url1":"SU","b1":"Unknown","url2":"SK","b2":"Kown",'heading':'Security Expart'},
        "SU":{'ques':"Is the person inside or outSide","url1":"SUIDec",'b1':'Inside','url2':'SUO','b2':'OutSide','heading':'Security Expart'},
        "SUO":{"ques":"Is the person in the gate or wondering around","url1":"SUOG","b1":"gate","url2":"SUOW",'heading':'Security Expart'},
        "SUOG":{"ques":"Is calling the bell or trying to break in?","url1":"SUOGBDec","b1":"Pressing Bell","url2":"SUOGBiDec","b2":"Breaking in",'heading':'Security Expart'},
        "SK":{"ques":"Is the person is inside or outside","url1":"SKI","b1":"inside","url2":"SKO","b2":"outside",'heading':'Security Expart'},
        "SKI":{"ques":"Is the person is doing anything violent or in Trouble","url1":"SKIDec","b1":"Violance","url2":"SKIDec","b2":"In Trouble",'heading':'Security Expart'},
        "SKO":{"ques":"Is the person in the door?","url1":"SKOGDec","b1":"Yes","url2":"N","b2":"No",'heading':'Security Expart'},

        "SUIDec":{"ques":"Notifying Owner.","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "SUOGBDec":{"ques":"Notifying Owner.","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "SUOGBiDec":{"ques":"Call the police","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "SKGDec":{"ques":"Opend the Gate.","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "SKIDec":{"ques":"Call the Police","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "SKOGDec":{"ques":"Open the door","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "N":{"ques":"Do Nothing","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},

        "U":{"ques":"Is anyone Home?","url1":"UNDec","b1":"No","url2":"UY","b2":"Yes",'heading':'Utility Expart'},
        "UY":{"ques":"Is there Over power consumpsiton","url1":"UYPDec","b1":"Yes","url2":"UYNP","b2":"No",'heading':'Utility Expart'},
        "UYNP":{"ques":"Is there any room with no pepople","url1":"UYNPRDec","b1":"Yes","url2":"","b2":"No",'heading':'Utility Expart'},

        "UNDec":{"ques":"Go to power saving mode.","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "UYPDec":{"ques":"Find the Cause and stop Wastage","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},
        "UYNPRDec":{"ques":"Turn off power of that room","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},

        "O":{"ques":"Is there any extra fire or smoke?","url1":"OFDec","b1":"Yes","url2":"N","b2":"No",'heading':'Others'},

        "OFDec":{"ques":"Sound alarm and call FireService","url1":"#","b1":"","url2":"#","b2":"",'heading':'Decision of Expart'},

    }
    context = {'data':questions[sec]}
    return render(request,'expart.html',context)

