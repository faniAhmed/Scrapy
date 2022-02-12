import time
import json
import requests

with open('C:\\Users\\Roshaan\\Desktop\\table2\\notDone.txt', 'r') as table_link:
    for line in table_link:
        url = line.strip()
        dg = url.split('dog_id=')
        new_dg = dg[1].split('&')
        dogid = new_dg[0]

        try:
            data = requests.get(url)
            dog_details = json.loads(data.content)['results-dog-details']
            dog_header = json.loads(data.content)['results-dog-header']
        except Exception as e:
            print('No Internet.\nWaiting...')
            print(e)
            time.sleep(20)
            with open('notDone.txt', 'a') as err:
                err.write(line)
            continue
        
        for dat in dog_header['dogs']:
            if int(dat['dogId']) == int(dogid):
                name = dat['name']
                print(name)

        for data in dog_details['forms']:
            try:
                dtm = data['raceTime']
                date = dtm.split(' ')
                with open('table.csv', 'a') as csv:
                    csv.write(date[0] + ','+ data['trackShortName'] +',' + data['distMetre'] +'m,['+ data['trapNum'] +'],'+ data['secTimeS'] +','+ data['bndPos'] +','+ data['rOutcomeDesc'] +','+ data['rpDistDesc'] +','+ data['otherDTxt'] +','+ data['remarks'].replace(',',' ') +','+ data['winnersTimeS'] +','+ str(data['goingType']) +','+ data['weight'] +','+ data['oddsDesc'] +','+ data['rGradeCde'] +','+ str(data['calcRTimeS']) + ',' + name +'\n')

            except Exception as e:
                print(e)
                with open('notDone.txt', 'a') as err:
                    err.write(line)
            

            