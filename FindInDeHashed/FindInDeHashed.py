# FindInDeHashed.py v1
# @inginformatico 2018
#
# Comprueba sin un email esta en la bbdd de DeHashed.com

import mechanicalsoup
import sys

print ("              #############################################")
print ("                        FindInDeHashed.py v1")
print ("                        @inginformatico 2018")
print ("              #############################################")

br = mechanicalsoup.StatefulBrowser()

if len(sys.argv)>=2 :
 
 objetivo = sys.argv[1];
 
 cont = br.open("http://www.dehashed.com");
 br.select_form('form[action="/search"]');
 br["query"] = objetivo;
 
 response = br.submit_selected();
 page = br.get_current_page()
 
 #Obtener resultados
 resumen = page.find('div', attrs={'class':'tile smaller'})
 
 print(" ")
 print ("Resultado de buscar: ", sys.argv[1], " en DeHashed.com ", resumen.text)
 print (objetivo," ->")
 print(" ")
 for each_div in page.findAll('div',{'class':'row tile'}):
      fila = each_div.find('div', attrs={'class':'small-11 columns'})
      print (fila.find('h6',).text)
 print ("")
else:
 print ("Este script necesita un parametro, url");


