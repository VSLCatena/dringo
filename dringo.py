#!/usr/bin/env python

#import & globals
import os
import ConfigParser
global rijen_save
global leters_save
#global rijen
#global letters

#team(false) = team 1. Team(true)=team 2
global team
team = False
#global punten


#loading
config = ConfigParser.SafeConfigParser()
config.read('settings.cfg')
os.system('clear')
name = config.get('start', 'name')
letters_save = config.get('save', 'letters')
rijen_save = config.get('save', 'rijen')

#clean datadump
with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[2, 2, '', False, [0, 0]]]]) 

#functions

def menu():
 global punten
 punten =[0,0]
 keuze=0
 os.system('clear')
 print name 
 print 
 print '== Menu =='
 print
 print '1. Nieuw spel (1)'
 print '2. Dringo (2) '
 print '3. Instellingen (3)'
 print '4. Stoppen (4)'
 print
 
 #keuze maken
 while type(keuze)!=int or (int(keuze)<1) or (int(keuze)>4):
  keuze = input_int('Je keuze (#): ')
 if int(keuze) == 1:
  instellingen(raw_input('Instellingen invoeren? ja/nee: '))
  antwoord = nieuw_spel()
  invullen(antwoord)
  antwoord = nieuw_spel()
  invullen(antwoord)
  menu()
 if int(keuze) == 2:
  dringo()
 if int(keuze) == 3:
  instellingen('ja')
  menu()
 if int(keuze) == 4:
  exit()

def nieuw_spel():
 os.system('clear')
 antwoord = ''
 with open("dringo_output.txt", "w") as text_file:
  text_file.write("%s" % [[[letters,rijen,antwoord,team,punten]]]) 
 
 print '== Team '+str(int(team)+1)+' ==       ( '+ str(punten[0]) +" - "+ str(punten[1])+ ' )'
 print 
 print str(letters) +'-letterwoorden met '+str(rijen)+ ' mogelijkheden'
 while (letters_count(antwoord)!=int(letters)):
  antwoord = letters_rmsp(raw_input('Het correcte woord (niet hardop noemen!): '))
 with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen,antwoord,team,punten]]]) 
 print
 return antwoord

def dringo():
 os.system('clear')
 print "Welkom bij Dringo. "
 print

 max_letters=0
 while (type(max_letters)!=int or (max_letters <1)):
  max_letters=int(input_int('Maximum aantal letters (zonder spatie) voor de gehele sessie:'))
  if (int(max_letters) > 9):
   max_letters=input_int("Weet je het zeker? Vul nogmaals in: ")
  
 print
 print "We werken met twee teams van 2 tot "+str(max_letters)+" letters"
 print "De puntentelling: "
 print "1. Per goed woord: 10 + (woordlengte - 2 x (poging - 1))" 
 print "	vb. 8 letterwoord in 2e poging: 10+8-2x(2-1) = 16"
 print "2. Overname door ander team: 10"
 print 
 raw_input('Duw op ENTER om door te gaan')
 i=2
 while i <= max_letters:
  instellingen('ja',i,i)
  #team1
  antwoord=nieuw_spel()
  invullen(antwoord)
  #team2
  antwoord=nieuw_spel()
  invullen(antwoord)
  #we verhogen het aantal letters
  i+=1
  
  
def input_int(message):
  while True:
    try:
       userInput = int(input(message))       
    except (ValueError, NameError, SyntaxError, TypeError) as e:
       print("Geen getal! Voer een getal in.")
       continue	
    else:
       return userInput 
       break   

 

def instellingen(bool, l=None, r=None):
 global letters
 global rijen 

 
#change settings
 if (bool=='ja'):

#manual settings
  if(l == None) or (r == None):
   print
   print "== Instellingen =="
   print 
   letters = input_int('Aantal letters? ('+letters_save+') #:')	
   rijen = input_int('Aantal rijen? ('+rijen_save+') #:')
   if type(letters)!=int:
    letters = letters_save
    if type(rijen)!=int:
     rijen = letters

#predefined settings	
  if (l != None) and (r != None):
   letters = l
   rijen = r	 
  
#opslaan
  if config.has_section('save') ==0:
   config.add_section('save')
  config.set('save', 'rijen', str(rijen))
  config.set('save', 'letters', str(letters))
  with open('settings.cfg', 'wb') as configfile:
   config.write(configfile)

   
 #pakt vorige 
 if bool!='ja':
  letters=letters_save
  rijen=rijen_save
	


def letters_count(word):
 return len(word) - word.count(' ')

def letters_rmsp(word):
 return word.replace(" ","")
  

 
	  
	  
#spelinfo

 
def invullen(antwoord):
 woorden =[]
 for i in xrange(0,int(rijen)+1):
 
#Laatste poging voor huidige team
  if ((i+1)==(rijen)):
   print 
   print "Laatste poging voor het HUIDIGE TEAM"

   
#na 'rijen' pogingen(i+1) nog niet goed, dan team 2 met laatste poging +extra rij
  if ((i)==(rijen)) and (woorden[-1][0]!=antwoord):
   global team
   team^=True
   print 
   print "Laatste poging voor het ANDERE TEAM"
   print "== Team "+ str(int(team)+1)+ " =="
   raw_input("Kies ENTER voor teamwissel op scherm plus extra rij")   
   rijen_scherm=i+1
   with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden]) 
   

 
  nieuw_aantal=0
  while nieuw_aantal==0:
   print  
   nieuw_input = raw_input(str(i+1)+"e woord/"+str(rijen)+": ")
   a=raw_input("Kies ENTER om te bevestigen. Voor opnieuw invoeren, vul iets anders in: ")
   nieuw_aantal = letters_count(nieuw_input)
  nieuw_afkap = letters_rmsp(nieuw_input)[0:int(letters)]
  nieuw_afkap_aantal = letters_count(nieuw_afkap)
  
  if (nieuw_aantal<int(letters)): 
   print('te kort. Faal -'),
  if (nieuw_aantal>int(letters)):
   print('te lang. Faal -'),
  
  woorden.append([])
  woorden[i].append(nieuw_afkap)   
 
  
  #controle woord&antwoord
  letters_goed =['_']*(nieuw_afkap_aantal)
  letters_bijna=['']*(nieuw_afkap_aantal)
  for u in xrange(0, len(antwoord)):
   for v in xrange(0, nieuw_afkap_aantal):
    if (antwoord[u]==nieuw_afkap[v]) and (u-v==0):
    #correcte letter op correcte positie
     letters_goed[v]=(nieuw_afkap[v])
    if (antwoord[u]==nieuw_afkap[v]) and (u-v!=0):
    #correcte letter op verkeerde positie
     letters_bijna[v]=(nieuw_afkap[v])
  
  #verschil tussen 'penis'-'peren'= bijnagoed(en) & bijnagoed(n) correctie voor letter die al in antwoord_goed zit.
  #letters_bijna=list(set(letters_bijna)-set(letters_goed))
  woorden[i].append(''.join(letters_goed))
  woorden[i].append(''.join(letters_bijna))
  print woorden
  



  
 

  
  # #normale hoeveelheid rijen
  # if ((i+1)<rijen) :
   # with open("dringo_output.txt", "w") as text_file:
    # text_file.write("%s" % [[[letters,rijen,antwoord,team,punten]]+woorden]) 
  # #Huidig team heeft laatste fout - extra rij voor ander team
  # if ((i+1)>=rijen)and woorden[-1][0]!=antwoord:
   # with open("dringo_output.txt", "w") as text_file:
    # text_file.write("%s" % [[[letters,rijen+1,antwoord,team,punten]]+woorden]) 	
  # #Huidig team heeft laatste goed
  # if ((i+1)>=rijen)and woorden[-1][0]==antwoord:
   # with open("dringo_output.txt", "w") as text_file:
    # text_file.write("%s" % [[[letters,rijen,antwoord,team,punten]]+woorden]) 		
  # #ANDERE team heeft het goed (rij+1)
  # if (i==rijen)and woorden[-1][0]==antwoord:
   # with open("dringo_output.txt", "w") as text_file:
    # text_file.write("%s" % [[[letters,rijen+1,antwoord,team,punten]]+woorden]) 	
   
#is het laatste antwoord NIET goed
  if woorden[-1][0]!=antwoord:
   
	#huidig team mag nog een keer
   if (i<int(rijen)-1):
	rijen_scherm=rijen
	 
    #ander team mag
   if (i==int(rijen)-1):
    rijen_scherm=i+1
   with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden])  
   
	#antwoord wordt weergegeven(niemand goed)
   if (i==int(rijen)):
    rijen_scherm=i+2
    print  
    raw_input("Kies ENTER om het antwoord weer te geven op het scherm")
    print "helaas, het goede antwoord was: "+antwoord
    print  
    woorden.append([antwoord,"",""])
    with open("dringo_output.txt", "w") as text_file:
     text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden])  
    raw_input("Kies ENTER om door te gaan")    
    break 
   with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden])  
 

#is het laatste antwoord GOED en 	 
  if woorden[-1][0]==antwoord:
   
   #huidige TEAM
   if (i<int(rijen)):
    rijen_scherm=rijen
	
   #Ander team 
   if (i==int(rijen)):
    rijen_scherm=i+1	
	
   global punten
   global team
   print   
   print "gefeliciteerd"
   rondepunt=int(10+max(0,(int(letters)-2*i)))
   punten[team]+=rondepunt
   print "Team "+str(int(team)+1) + " heeft "+ str(rondepunt)+ " behaald. Totaal: "+str(punten)
   #teamwissel als huidig team het goed geraden heeft

   with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden]) 
   print  
   raw_input("Kies ENTER om door te gaan")
   if i<(rijen):
    team^=True
   with open("dringo_output.txt", "w") as text_file:
    text_file.write("%s" % [[[letters,rijen_scherm,antwoord,team,punten]]+woorden]) 
   break
	





  

   
   
   


menu()
  

  
