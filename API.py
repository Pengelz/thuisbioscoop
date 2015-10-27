import datetime
import requests
import xmltodict

def ophalenFilms(invoer):
    if invoer == "Vandaag":
        datum = (datetime.date.today()).strftime("%d-%m-%Y")
    else:
        datum = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
    url = "http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=rilqhtllly1ugzm552twhnzv7c6x50xl&dag="+ datum +"&sorteer=0"

    request = requests.get(url)

    inhoud = xmltodict.parse(request.text)

    return inhoud

def ophalenInfo(titel, dag):

    dictionary = ophalenFilms(dag)
    films = dictionary['filmsoptv']['film']
    for film in films:
        if film['titel'] == titel:
            return film
    return None