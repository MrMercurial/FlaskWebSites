#encoding:utf-8
import urllib,urllib2,json

facecompareURL='http://api.youtu.qq.com/youtu/api/facecompare'
appid='10101862'
secretID='AKIDafccgc3xMiIwT3pewVIF0d9dOCSau0zP'
secretKEY='PgnxGoNNbpIEDEoQ5g5YVYWUVHYyXhor'

def facecompare(imageA,imageB):
    postdata={}
    postdata['app_id']=appid
    postdata['imageA']=imageA
    postdata['imageB']=imageB
    data=urllib.urlencode(postdata)
    result=urllib2.urlopen(facecompareURL,data)
    return result.read()

facecompare('121','2323')