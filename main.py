from bs4 import BeautifulSoup
import requests
import csv


data = []

links = ['https://www.filmaffinity.com/us/film745443.html', 'https://www.filmaffinity.com/us/film304093.html', 'https://www.filmaffinity.com/us/film982491.html', 'https://www.filmaffinity.com/us/film176709.html', 'https://www.filmaffinity.com/us/film624787.html', 'https://www.filmaffinity.com/us/film379410.html', 'https://www.filmaffinity.com/us/film398662.html', 'https://www.filmaffinity.com/us/film234364.html', 'https://www.filmaffinity.com/us/film588552.html', 'https://www.filmaffinity.com/us/film914339.html', 'https://www.filmaffinity.com/us/film460960.html', 'https://www.filmaffinity.com/us/film589371.html', 'https://www.filmaffinity.com/us/film358086.html', 'https://www.filmaffinity.com/us/film725097.html', 'https://www.filmaffinity.com/us/film377909.html', 'https://www.filmaffinity.com/us/film559484.html', 'https://www.filmaffinity.com/us/film180575.html', 'https://www.filmaffinity.com/us/film265138.html', 'https://www.filmaffinity.com/us/film364808.html', 'https://www.filmaffinity.com/us/film495575.html', 'https://www.filmaffinity.com/us/film439937.html', 'https://www.filmaffinity.com/us/film279751.html', 'https://www.filmaffinity.com/us/film335123.html', 'https://www.filmaffinity.com/us/film173307.html', 'https://www.filmaffinity.com/us/film813182.html', 'https://www.filmaffinity.com/us/film200686.html', 'https://www.filmaffinity.com/us/film459102.html', 'https://www.filmaffinity.com/us/film331571.html', 'https://www.filmaffinity.com/us/film370564.html', 'https://www.filmaffinity.com/us/film736794.html', 'https://www.filmaffinity.com/us/film604873.html', 'https://www.filmaffinity.com/us/film476573.html', 'https://www.filmaffinity.com/us/film218925.html', 'https://www.filmaffinity.com/us/film837457.html', 'https://www.filmaffinity.com/us/film225440.html', 'https://www.filmaffinity.com/us/film746573.html', 'https://www.filmaffinity.com/us/film252839.html', 'https://www.filmaffinity.com/us/film824903.html', 'https://www.filmaffinity.com/us/film259402.html', 'https://www.filmaffinity.com/us/film871605.html', 'https://www.filmaffinity.com/us/film935719.html', 'https://www.filmaffinity.com/us/film387332.html', 'https://www.filmaffinity.com/us/film603775.html', 'https://www.filmaffinity.com/us/film486352.html', 'https://www.filmaffinity.com/us/film522688.html', 'https://www.filmaffinity.com/us/film500429.html', 'https://www.filmaffinity.com/us/film136703.html', 'https://www.filmaffinity.com/us/film683886.html', 'https://www.filmaffinity.com/us/film270512.html', 'https://www.filmaffinity.com/us/film916275.html', 'https://www.filmaffinity.com/us/film136713.html', 'https://www.filmaffinity.com/us/film654834.html', 'https://www.filmaffinity.com/us/film793527.html', 'https://www.filmaffinity.com/us/film226740.html', 'https://www.filmaffinity.com/us/film587109.html', 'https://www.filmaffinity.com/us/film634611.html', 'https://www.filmaffinity.com/us/film187119.html', 'https://www.filmaffinity.com/us/film509422.html', 'https://www.filmaffinity.com/us/film973146.html', 'https://www.filmaffinity.com/us/film356365.html', 'https://www.filmaffinity.com/us/film533524.html', 'https://www.filmaffinity.com/us/film393232.html', 'https://www.filmaffinity.com/us/film738313.html', 'https://www.filmaffinity.com/us/film435937.html', 'https://www.filmaffinity.com/us/film378668.html', 'https://www.filmaffinity.com/us/film200514.html', 'https://www.filmaffinity.com/us/film675299.html', 'https://www.filmaffinity.com/us/film728054.html', 'https://www.filmaffinity.com/us/film382363.html', 'https://www.filmaffinity.com/us/film964656.html', 'https://www.filmaffinity.com/us/film843913.html', 'https://www.filmaffinity.com/us/film127246.html', 'https://www.filmaffinity.com/us/film570709.html', 'https://www.filmaffinity.com/us/film753586.html', 'https://www.filmaffinity.com/us/film697612.html', 'https://www.filmaffinity.com/us/film475857.html', 'https://www.filmaffinity.com/us/film232560.html', 'https://www.filmaffinity.com/us/film685459.html', 'https://www.filmaffinity.com/us/film834231.html', 'https://www.filmaffinity.com/us/film115831.html', 'https://www.filmaffinity.com/us/film579015.html', 'https://www.filmaffinity.com/us/film294982.html', 'https://www.filmaffinity.com/us/film736170.html', 'https://www.filmaffinity.com/us/film423543.html', 'https://www.filmaffinity.com/us/film595978.html', 'https://www.filmaffinity.com/us/film254057.html', 'https://www.filmaffinity.com/us/film380213.html', 'https://www.filmaffinity.com/us/film591287.html', 'https://www.filmaffinity.com/us/film709199.html', 'https://www.filmaffinity.com/us/film778899.html', 'https://www.filmaffinity.com/us/film675332.html', 'https://www.filmaffinity.com/us/film593647.html', 'https://www.filmaffinity.com/us/film101139.html', 'https://www.filmaffinity.com/us/film990974.html', 'https://www.filmaffinity.com/us/film409429.html', 'https://www.filmaffinity.com/us/film667520.html', 'https://www.filmaffinity.com/us/film757860.html', 'https://www.filmaffinity.com/us/film898332.html', 'https://www.filmaffinity.com/us/film414181.html', 'https://www.filmaffinity.com/us/film314857.html','https://www.filmaffinity.com/us/film770208.html', 'https://www.filmaffinity.com/us/film777337.html', 'https://www.filmaffinity.com/us/film726432.html', 'https://www.filmaffinity.com/us/film565097.html', 'https://www.filmaffinity.com/us/film571431.html', 'https://www.filmaffinity.com/us/film758886.html', 'https://www.filmaffinity.com/us/film439658.html', 'https://www.filmaffinity.com/us/film206852.html', 'https://www.filmaffinity.com/us/film715018.html', 'https://www.filmaffinity.com/us/film447506.html', 'https://www.filmaffinity.com/us/film252549.html', 'https://www.filmaffinity.com/us/film326591.html', 'https://www.filmaffinity.com/us/film770107.html', 'https://www.filmaffinity.com/us/film254768.html', 'https://www.filmaffinity.com/us/film113872.html', 'https://www.filmaffinity.com/us/film271374.html', 'https://www.filmaffinity.com/us/film483433.html', 'https://www.filmaffinity.com/us/film843357.html', 'https://www.filmaffinity.com/us/film896579.html', 'https://www.filmaffinity.com/us/film742595.html', 'https://www.filmaffinity.com/us/film934073.html', 'https://www.filmaffinity.com/us/film199955.html', 'https://www.filmaffinity.com/us/film610782.html', 'https://www.filmaffinity.com/us/film814835.html', 'https://www.filmaffinity.com/us/film638967.html', 'https://www.filmaffinity.com/us/film272482.html', 'https://www.filmaffinity.com/us/film105370.html', 'https://www.filmaffinity.com/us/film984700.html', 'https://www.filmaffinity.com/us/film323959.html', 'https://www.filmaffinity.com/us/film544288.html', 'https://www.filmaffinity.com/us/film120015.html', 'https://www.filmaffinity.com/us/film324884.html', 'https://www.filmaffinity.com/us/film562592.html', 'https://www.filmaffinity.com/us/film448681.html', 'https://www.filmaffinity.com/us/film682843.html', 'https://www.filmaffinity.com/us/film481490.html', 'https://www.filmaffinity.com/us/film226980.html', 'https://www.filmaffinity.com/us/film172994.html', 'https://www.filmaffinity.com/us/film306079.html', 'https://www.filmaffinity.com/us/film919284.html', 'https://www.filmaffinity.com/us/film776892.html', 'https://www.filmaffinity.com/us/film705263.html', 'https://www.filmaffinity.com/us/film387330.html', 'https://www.filmaffinity.com/us/film208208.html', 'https://www.filmaffinity.com/us/film198480.html', 'https://www.filmaffinity.com/us/film458068.html', 'https://www.filmaffinity.com/us/film623436.html', 'https://www.filmaffinity.com/us/film604690.html', 'https://www.filmaffinity.com/us/film821075.html', 'https://www.filmaffinity.com/us/film895292.html', 'https://www.filmaffinity.com/us/film136013.html', 'https://www.filmaffinity.com/us/film558250.html', 'https://www.filmaffinity.com/us/film578561.html', 'https://www.filmaffinity.com/us/film388461.html', 'https://www.filmaffinity.com/us/film508916.html', 'https://www.filmaffinity.com/us/film518577.html', 'https://www.filmaffinity.com/us/film837889.html', 'https://www.filmaffinity.com/us/film377275.html', 'https://www.filmaffinity.com/us/film572440.html', 'https://www.filmaffinity.com/us/film612348.html']

for index,link in enumerate(links):
    info = {}
    try:
        html_text_2 = requests.get(link).text
        soup2 = BeautifulSoup(html_text_2, 'lxml')
        left_column = soup2.find(id="left-column")
        description = left_column.find(itemprop="description").text
        dd = left_column.find_all('dd')
        cast = left_column.find(class_="card-cast").text
        right_column = soup2.find(id="movie-rat-avg").text.replace(' ', '')
        genres = left_column.find(class_="card-genres").text

        name = dd[0].text
        name = name.strip()
        year = dd[1].text
        year = year.strip()
        running_time = dd[2].text.strip('.')
        country = dd[3].text.strip()

        actor = cast
        actor = actor[0: actor.find(',')].strip()

        genre = genres
        genre = genre.replace('|', '.')
        find_val = genre.find('.')+1
        genre = genre[find_val:genre.find('.', find_val)].strip()

        seasons = description
        seasons = seasons[seasons.find('Season') - 3 : seasons.find('Season')].strip()

        episodes = description
        episodes = episodes[episodes.find('Episode') - 4 : episodes.find('Episode')].strip()
        episodes = episodes.strip('.')
        bol = any(char.isdigit() for char in episodes)
        if(bol != True):
            episodes = -1
        
        bol = any(char.isdigit() for char in seasons)
        if(bol != True):
            seasons = -1

        print(str(index+1)+'/'+ name + '/'+running_time+'/'+country+'/'+actor+'/'+str(year)+'/'+genre +"/"+ str(episodes) + "/"+str(seasons))
        print("-------------------------------------------------------------")
        info['id'] = index + 1
        info['name'] = name
        info['country'] = country
        info['running_time_min'] = running_time
        info['year'] = year
        info['actor'] = actor
        info['genre'] = genre
        info['seasons'] = seasons
        info['episodes'] = episodes
        info['rating'] = right_column.strip('\"')
        data.append(info)

    except requests.exceptions.Timeout:
        print("Timeout occurred")
    
    except AttributeError:
        print('No such attribute')



filename = 'films.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['id','name','country','running_time_min','year','actor', 'genre','seasons', 'episodes', 'rating'])
    w.writeheader()
    for info in data:
        w.writerow(info)
