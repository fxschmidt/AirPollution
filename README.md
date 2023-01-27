# Air Pollution Data-Science Projekt

Abgabe für den Kurs Data-Science mit Python im WS 22  
von Felix Schmidt, Matrikelnr: 5448377

Dieses Repository beinhaltet alle für die Abgabe nötigen Datein:  
 - Jupyter Notebooks (als .ipynb und .html)
 - einige Hintergrund-Informationen (z.B. Paper zum Thema) im Ordner *Dokumentation*
 - die aus der API erhaltenen Daten in den Ordnern *Pollution_Data* und *Predictor_Data* 
 - Die Environment erstell mit anaconda auf Linux, siehe dazu *environment.yml*

## Einleitung
Da Luftverschmutzung in Städten ist aus vielen Perspektiven ein wichtiges Thema: 
- gesundheitlich: 240.000 vorzeitige Todesfälle durch Feinstaub in der EU (Quelle [Tagesschau](https://www.tagesschau.de/ausland/europa/tote-luftverschmutzung-101.html#:~:text=Die%20Luftqualit%C3%A4t%20in%20der%20EU,Luft%20etwa%20240.000%20Menschen%20vorzeitig.))
- wirtschaftlich: Unsicherheit über die Zukunft des Verbrennungsmotors
- ...
  
Es wurde Los Angeles gewählt, da diese Stadt eine hohe Luftverschmutzung aufweist. Außerdem dacht ich das in Amerika mehr Daten im Internet frei zur Verfügung stehen (nach dem Projekt bin ich mir dessen nicht mehr sicher).

## Schadstoffe
Mehr Infos über die einzelnen Schadstoffe sind bei der [EPA](https://www.epa.gov/criteria-air-pollutants) oder auf den jeweiligen Wikipedia-Artikeln zu finden.   
In Kurzform:
- **O3 Ozon**: Bodennahes Ozon wird in radikalischen Reaktion aus Stickoxiden und Sauerstoffradikalen gebildet, dafür ist UV-Strahlung nötig.
- **NOx Stickoxide**: Hauptsächlich thermisches NOx, dies entsteht bei Verbrennungsprozessen mit sehr hohen Temperaturen wie es z.B. im Straßenverkehr der Fall ist.
- **SO2 Schwefeldioxid**: Durch schwefelhaltige Brennstoffe bei Verbrennungsprozessen verursacht. Durch Rauchgasentschwefelung und Grenzwerte für Schwefel in den Kraftstoffen, nur noch im Schiffsverkehr problematisch. 
- **PM2.5 bzw. PM10 Feinstaub**: Mit einer Größe von weniger als 2.5 / 10 Mikrometer. Entsteht ebenfalls bei Verbrennungsprozessen, aber auch Reifen-/Bremsenabrieb und  je nach Größe kann dieser bis in die Lunge/Blutkreislauf eindringen. 

## Übersicht und Ziele der Notebooks

### get_prepare_data.ipynb
In diesem Notebook werden die Daten der Schadstoffe und der Predictoren dafür aus den unterschiedlichen Quellen (API, selbst heruntergeladene .csv Datein oder selbst erstellte Daten) zusammengefügt und für eine Datenanalyse vorbereitet werden. 

### exploratory_data_analysis.ipynb

Explorative Datenanalyse um mögliche Zusammenhänge zwischen den Schadstoffkonzentrationen und den weiteren Daten zu ermitteln. Diese könnten wichtig sein um gezielt Gegenmaßnahmen zu treffen oder auch um z.B. beim machine learning bessere Entscheidungentreffen zu können (Welche Features kann ich weglassen um mehr Daten behalten zu können?).

### machine_learning.ipynb
In diesem Notebook werden verschiedenen ML-Modelle getestet.  
**Ziel ist dabei: mit den Daten eines Tages die Konzentration oder AQI-Wert eines Schadstoffes vorhersagen**
Sinnvolle Szenarien für eine Anwendung sind dabei:
- Die Messung eines bestimmten Schadstoffes fällt z.B. wegen eines technischen Defekts aus. Dennoch ist es weiterhin wichtig den Schadstoff zu erfassen um bei hoher Belastung Gegenmaßnahmen zu ergreifen.
- Anwendung in Staaten mit geringem Vertrauen in die kommunale/staatlichen Organe, da diese möglicherweiße die Konzentrationen eines problematischen Schadstoffes fälschen könnten. 
- In kleineren Städten könnte nach einer Lernphase (Zeit in die Stadt z.B. eine Ozon-Messstadion besitzt) auch auf lange Sicht (falls also kein Sensor mehr vorhanden ist) trotzdem noch Werte für den Schadstoff berechnet werden und so auch Verhaltensempehlungen an die Bevölkerung bei einer hohen Schadstoffbelastung abgegeben werden. Dabei ist jedoch die Vorhersagekraft des Modells genau zu überprüfen. 

### neural_network.ipynb
In disem Notebook soll ein neuronales Netz getestet werden um die Tageswerte von NO2 vorherzusagen. Es wird dabei mit Tensorflow.Keras gearbeitet. 

## Resultate

Insgesamt sind die erstellten Modell zur Vorhersage der tagesaktuellen Schadstoffwerte nicht gänzlich zufriedenstellend. Zur weiteren Verbesserung der Modelle sollten daher noch mehr Features aufgenommen werden, dazu gehört z.B. eine Verkehrszählung (diese habe ich jedoch nicht finden können) oder weitere Precursor Schadstoffe wie VOC (flüchtige Kohlenwasserstoffe bilden die Vorläufer für die Sauerstoffradikale bei der Ozon Entstehung).   
Als weiteren Anwendungszweck für die hier erstellten Modelle könnte ich mir auch vorstellen, das durch die Vorhersage die Funktionsfähigkeit der Messstadionen geprüft werden könnte.