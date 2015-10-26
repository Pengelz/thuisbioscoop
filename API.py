import datetime
import requests
import xmltodict

def ophalenFilms(invoer):
    if invoer == "Vandaag":
        datum = datetime.strftime("%d-%m-%Y")
    else:
        datum = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%d-%m-%Y")
        print(datum)
    url = "http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=rilqhtllly1ugzm552twhnzv7c6x50xl&dag="+ datum +"&sorteer=0"

    request = requests.get(url)

    inhoud = xmltodict.parse(request.text)

    return inhoud
