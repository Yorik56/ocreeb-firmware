# KB2040

### Initialisation

Pour entrer initialiser la carte KB2040, **appuyez longuement sur BOOT, puis appuyez sur RST** . (Ensuite, vous pouvez libérer les deux.) Glisser [ce fichier](https://circuitpython.org/board/adafruit_kb2040/) sur la carte (RPI-RP2), elle se redémarre, avec 3 fichiers et 1 dossier.
Puis Téléchargez [KMK](https://github.com/KMKfw/kmk_firmware/archive/refs/heads/master.zip), décompressez et copiez le répertoire **KMK** et le fichier **boot.py** à la racine de CIRCUITPY

### **Entrer en mode sans échec**

Vous souhaitez éditer votre **code.py** ou modifier les fichiers sur votre lecteur **CIRCUITPY** , mais constatez que vous ne pouvez pas. Peut-être que votre carte est devenue dans un état où **CIRCUITPY** est en lecture seule.
Appuyer une fois sur reset, puis pendant la led jaune ou sinon double clic long. Si c’est réussi, la led va clignoté trois fois, environ toute les 10 sec.

### Réinitialiser en profondeur

Remettre la carte à l’état inittiale, avec Boot maintenue puis btn reset. On se retrouve avec une carte nommé RPI-RP2, mettre [ce fichier](https://cdn-learn.adafruit.com/assets/assets/000/101/659/original/flash_nuke.uf2?1618945856) sur la carte va tout nettoyer.

### Signification de la led (côté btn rst)

| Couleur | Signification |
| --- | --- |
| animation arc-en-ciel | Exemple de code Arduino par défaut sur la carte (état d'usine sans CircuitPython installé) |
| un éclat de flash jaune | Démarrage. Démarrage avec le code CircuitPython (et pas par exemple Arduino qui démarre immédiatement). En appuyant sur réinitialiser pendant cette période de 1 000 ms, vous pouvez passer en mode sans échec pour essayer de réparer un KB2040 autrement maçonné. |
| deux flashs rouges répétés toutes les 5 secondes | erreur dans votre code (code.py ou alias comme code.txt, main.py, main.txt). Déboguer avec MU ou un autre outil. |
| flash vert répété toutes les 5 secondes | pas de code.py |
| blanc continu | Mode REPL (lecture-évaluation-impression-boucle). Un mode de communication série par exemple en MU. |
| rien (mais la LED verte power est allumée) | tout va bien |

### Nommer votre fichier programme

CircuitPython recherche un fichier de code sur la carte à exécuter. Il existe quatre options : **code.txt** , **code.py** , **main.txt** et **main.py** . CircuitPython recherche ces fichiers, dans cet ordre, puis exécute le premier qu'il trouve.