Titel: Illegale Preisabsprache

Beschreibung: Ein Webscraper in Python welcher die Preisabsprache zwischen zwei grossen Unternehmen beweisen soll.

Wichtiges: BeautifulSoup und Conda sind essenziell für den fehlerfreien Betrieb des Programmes. 
	Dazu empfehle ich den Download der Distribution Anaconda: https://www.anaconda.com/
	Anaconda beinhaltet BeautifulSoup und Conda.

	Geschrieben und getestet wurde das Programm mit VS Code. Wichtig ist hierbei noch die 
	korrekte festlegung des Interpreters. Dieser kann mithilfe der Tastenkombination Shift+Ctrl+P erfolgen
	oder man startet VS Code direkt aus der Anaconda Distribution heraus. Bei der Tastenkombination
	sucht man nach Interpreter und wählt unter Python den Anaconda Interpreter.

Die gesamte Anleitung wurde nur mit Windows getestet, kann es unter Linux abweichungen geben.

Das Programm kann sofort gestartet werden. Möchte man die Zeitabstände zwischen den Scrapings verändern,
muss man die Zeile hier anpassen  
	time.sleep(5.0 - ((time.time() - starttime) % 5.0))
		    ^				      ^

Momentan ist der Zeitabstand auf 5 Sekunden festgelegt.
(Im main.py ist der Zeitabstand gerade auf 20 Sekunden eingestellt)
