array=['nujsua hawj','nyob pobntoosawm','tuaj kawm ntawm nyob hau vieantia']
array.append('lam tuaj kawm xwb tsi paub tias yuav  zooo lsi casas')
array.insert(0,'nousua')
array.remove('nousua') 
print()

quest=['nujsua','hawj','hawj']
if 'nujsua' in quest:
    print('')
max_quest=5
if len(quest) < max_quest:
    quest.append('nousua')
    print()
      



quest=['nujsua','hawj','hawj']
for i in range(len(quest)):
    print( str(i+1) + '.' + quest[i])