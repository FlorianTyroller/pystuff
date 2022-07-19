import random
from collections import defaultdict

us = ["1.	Welche Umweltschutzbereiche kennen Sie","2.	Was ist nachsorgender US + Techniken", "3.	Was ist kompensatorischer Us + Techniken", "4.	Was ist vorsorgender Us +Techs", "5.	Was ist umweltbeobachtung + Techs", "6.	Was ist DPSIR + beispiele für umweltindikatoren", "Schwerpunkte ökologischer Herausforderungen", "8.gesetzliche maßnahmen zur umsetzung umweltpolitischer ziele", "welche gesetzte gelten für unterschiedliche umweltmedien", "kriterien zur bestimmung des standes der technik"]
nachhaltig = ["1.	Einflüsse, risiken und chancen des umweltschutzes auf unternehmen", "2.	Nutzungspotenziale von umweltmanagementsystemen extern/intern", "3.	Ziele nachhaltiges wirtschaften + bsps", "4.	Einteilung von rohstoffen"]
schadstoffe = ["1.	Allgemeine schadstoffquellen", "2.	Messeinheiten im strahlenschutz", "3.	Einfluss baumaterialien auf strahlenexposition","4.	Mittlere strahlenexposition in d","5.	Aus welchen strahlenquellen", "6.	Humantoxikologische wirkung von organischen schadstoffen", "7.	Was ist adi-wert und ptwi-wert + bestimmung"]
klimaenergie = ["1.	Spurengase in der atmosphäre + quellen", "2.	Was ist entkarbonisierung", "3.	Arten und nutzungsformen erneuerbarer energien", "4.	Umweltbeeinträchtigungen durch erneuerbare energien", "5.	Möglischkeiten zur wasserstofferzeugung"]
imission = ["1.	Was ist emission/imsission:", "2.	Spurengase in der troposphäre + wirkung :", "3.	Was ist feinstaub + entstehung", "4.	Techniken ur reinignun von feinstaub","5.	Physiologische und psychologische reaktionen von lärm"]
abwasser = ["Parameter bei den anforderungen an das abwasser für einleitungsstellen kommunaler kläranlagen", "2.	Hauptelemente einer kommunalen kläranlage:", "3.	Varianten der biologischen reinigung:", "4.	Wo verläuft biologische stickstoffeliminierung", "5.	Warum schlamm faulen", "6.	Wie wird stickstoff und phosphor gerippt"]
trinkwasser = ["1.	Anforderungen für trinkwasser", "2.	Verfahren zur künstlichen grundwasseranreicherung und uferfiltration", "3.	Vorteile künstlicher gwassergewinnung gegenüber uferfiltration", "4.	Allgemeine methoden der trinkwasserraufbereitung", "5.	Warum eisen oder mangan aus trinkwasser entfernen", "6.	Zonen und vorschriften von wasserschutzgebieten", "7.	Methoden der trinkwasserdesinfektion, mit vor und nachteilen"]
bodenschutz = ["umweltprobleme durch landwirtschaft: ", "sanierungsziele bei der bodensanierung"]
abfall = ["1.	Fünfstufige hierarchie bei abfallwirtschaft","ziele der müllverbrennung", "wesentliche teile einer müllverbrennung", "wie kann deponiesickerwasser aufbereitet werden", "welche vor und nachteile beinhaltet deponiegas"]
kresilaufwirtschaft = ["typische anwendungsbereiche beim recycling von kunststoffe", "anforderungen an recyclingprodukte", "was umfasst produktverantwortung im kreislaufwirtschafts gesetz", "urban mining"]

topics = [us,nachhaltig,schadstoffe,klimaenergie,imission,abwasser,trinkwasser,bodenschutz,abfall,kresilaufwirtschaft]

qs = sum(len(t) for t in topics)

e = defaultdict(int)
for i in range(118203):
    e[random.choices([random.choice(t) for t in topics], weights=[len(t) for t in topics])] += 1
print(e.keys())



h = ["Schwerpunkte ökologischer Herausforderungen","Techniken ur reinignun von feinstaub","gesetzliche maßnahmen zur umsetzung umweltpolitischer ziele"]