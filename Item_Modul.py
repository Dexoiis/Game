#------------#
# Item Modul #
#------------#

import random

#-------------------#
# Seltenheitsstufen #
#-------------------#
RARITIES = ["gewöhnlich, selten, episch, legendär, mythisch"],
#------------------------------------------------------------------#
# Gewöhnlich 60%, Selten 25%, Episch 10%, Legendär 4%, Mythisch 1% #
#------------------------------------------------------------------#

DROP_RATE = {
    "gewöhnlich" : 60,
    "selten" : 25,
    "episch" : 10,
    "legendär" : 4,
    "mytisch" : 1,
    
}

#-----------------------------------------#
# Items Sortieren nach Rarität/seltenheit #
#-----------------------------------------#
Items = {
     "gewöhnlich": {
         
# Eifache Monster
        "waffe": {
            "Goblin": ["Altes Messer"],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": ["Rostiges Schwert"],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
#Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "rüstung": {
            "Goblin": ["Zerfetzte Stoffhose"],
            "Kobold": ["Lederkappe"],
            "Rattenkönig": ["Zerkaute Lederrüstung"],
            "Höhlenkrabbler": [],
            "Bandit": ["Lederweste"],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
# Einfache Monster
        "trank": {
            "Goblin": ["Kleiner Heiltrank"],
            "Kobold": ["Kleiner Manatrank"],
            "Rattenkönig": ["Kleiner Heiltrank"],
            "Höhlenkrabbler": ["Kleiner Gifttrank"],
            "Bandit": [],
            "Glühwürmenschwarm": ["Mini-Heiltrank"],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": ["Mittlerer Gifttrank"],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "sonstiges": {
            "Goblin": [],
            "Kobold": ["Kupfermünze"],
            "Rattenkönig": ["Stinkender Fellfetzen"],
            "Höhlenkrabbler": ["Zerbrochene Krallen"],
            "Bandit": ["Kupfermünzen"],
            "Glühwürmenschwarm": ["Käferflügel"],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": ["Wolfspelz"],
            "Morastgeist": [],
            "Steinwurm": ["Wurmzahn","Steinhaut-Salbe"],
            "Blutegelriese": ["Blutegelzahn", "Schleimhaut"],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        }
    },
    
     "selten": {
         
# Eifache Monster
        "waffe": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
#Mittlere Monster
            "Schattenwolf": ["Schattenzahn"],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": ["Knochenschwert"],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "rüstung": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": ["Lederweste"],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": ["Zerbeulte Eisrüstung"],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
# Einfache Monster
        "trank": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": ["Mittlerer Heiltrank"],
            "Morastgeist": ["Schleimtrank"],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": ["Kälteschutz-Trank"],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": ["Großer Feuertrank"],
# Boss Monster
            "Uralter Drache": ["Großer Heiltrank"],
        },
        
# Einfache Monster
        "sonstiges": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": ["Spinnengift"],
            "Bandit": [],
            "Glühwürmenschwarm": ["Leuchtstaub"],
            "Verfluchter Vogel": ["Rabenklaue", "Schwarze Feder"],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": ["Geisteressenz"],
            "Steinwurm": ["Splitterstein"],
            "Blutegelriese": [],
            "Eiswyrmling": ["Eisschuppe", "Frostzahn"],
            "Sandläufer": ["Giftstachel", "Chitinpanzer"],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": ["Kristallfragment"],
            "Schrecken der Tiefen": ["Tiefseeperle"],
            "Drache": ["Drachenschuppe"],
# Boss Monster
            "Uralter Drache": [],
        }
    },
     
     "episch": {
         
# Eifache Monster
        "waffe": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
#Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": ["Glutklinge"],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": ["Tentakelpeitsche"],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "rüstung": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": ["Amulett des Flüsterns"],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": ["Schädelamulet"],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": ["Hitzeschutz-Ring"],
            "Schattenritter": [],
            "Kristallgolem": ["Kristallrüstung"],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
# Einfache Monster
        "trank": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": ["Großer Trank der Dunkelsicht"],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": ["Großer Heiltrank"],
        },
        
# Einfache Monster
        "sonstiges": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": ["Magischer Splitter"],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": ["Sandjuwel"],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": ["Dämonenherz", "Seelenfragment"],
            "Flammen-Golem": ["Feuerkern"],
            "Schattenritter": [],
            "Kristallgolem": ["Leuchtender Kern"],
            "Schrecken der Tiefen": ["Essenz des Ozeans"],
            "Drache": ["Drachenzahn"],
# Boss Monster
            "Uralter Drache": [],
        }
    },
     
     "legendär": {
         
# Eifache Monster
        "waffe": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
#Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": ["Verfluchtes Schwert"], 
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "rüstung": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": ["Lederweste"],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": ["Rüstung der Schatten"], 
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
# Einfache Monster
        "trank": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "sonstiges": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": ["Seelenstein"], 
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        }
    },
     
     "mytisch": {
         
# Eifache Monster
        "waffe": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
#Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": ["Drachenzahnklinge"], 
        },
        
# Einfache Monster
        "rüstung": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": ["Drachenschuppenrüstung"], 
        },
# Einfache Monster
        "trank": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        },
        
# Einfache Monster
        "sonstiges": {
            "Goblin": [],
            "Kobold": [],
            "Rattenkönig": [],
            "Höhlenkrabbler": [],
            "Bandit": [],
            "Glühwürmenschwarm": [],
            "Verfluchter Vogel": [],
            
# Mittlere Monster
            "Schattenwolf": [],
            "Morastgeist": [],
            "Steinwurm": [],
            "Blutegelriese": [],
            "Eiswyrmling": [],
            "Sandläufer": [],
            "Knochenkrieger": [],
# Schwere Monster
            "Schattendämon": [],
            "Flammen-Golem": [],
            "Schattenritter": [],
            "Kristallgolem": [],
            "Schrecken der Tiefen": [],
            "Drache": [],
# Boss Monster
            "Uralter Drache": [],
        }
    },
}

#-------------------#
# Raritäten Tabelle #
#-------------------#
Drop_tables = {

#------------------#
# Einfache Monster #
#------------------#
    "Goblin": [
        {"rarity": "gewöhnlich", "category": "waffe", "item": "Altes Messer", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "rüstung", "item": "Zerfetzte Stoffhose", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "trank", "item": "Kleiner Heiltrank", "chance": 0.6},
    ],
    
    "Kobold": [
        {"rarity": "gewöhnlich", "category": "rüstung", "item": "Lederkappe", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "trank", "item": "Kleiner Manatrank", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Kupfermünze", "chance": 0.6},
    ],
    
    "Rattenkönig": [
        {"rarity": "gewöhnlich", "category": "rüstung", "item": "Zerkaute Lederrüstung", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Stinkender Fellfetzen", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "trank", "item": "Kleiner Heiltrank", "chance": 0.6},
    ],
    
    "Höhlenkrabbler": [
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Zerbrochene Krallen", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "trank", "item": "Kleiner Gifttrank", "chance": 0.6},
        {"rarity": "selten", "category": "sonstiges", "item": "Spinnengift", "chance": 0.25},
    ],
    
    "Bandit": [
        {"rarity": "gewöhnlich", "category": "waffe", "item": "Rostiges Schwert", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "rüstung", "item": "Lederweste", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Kupfermünzen", "chance": 0.6},
    ],
    
    "Glühwürmenschwarm": [
        {"rarity": "gewöhnlich", "category": "trank", "item": "Mini-Heiltrank", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Käferflügel", "chance": 0.6},
        {"rarity": "selten", "category": "sonstiges", "item": "Leuchtstaub", "chance": 0.25},
    ],
    
    "Verfluchter Vogel": [
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Rabenklaue", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Schwarze Feder", "chance": 0.6},
        {"rarity": "episch", "category": "rüstung", "item": "Amulett des Flüsterns", "chance": 0.1},
    ],

#------------------#
# Mittlere Monster #
#------------------#
    "Schattenwolf": [
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Wolfspelz", "chance": 0.6},
        {"rarity": "selten", "category": "waffe", "item": "Schattenzahn", "chance": 0.25},
        {"rarity": "selten", "category": "trank", "item": "Mittlerer Heiltrank", "chance": 0.25},
    ],
    
    "Morastgeist": [
        {"rarity": "selten", "category": "sonstiges", "item": "Geisteressenz", "chance": 0.25},
        {"rarity": "selten", "category": "trank", "item": "Schleimtrank", "chance": 0.25},
        {"rarity": "episch", "category": "sonstiges", "item": "Magischer Splitter", "chance": 0.1},
    ],
    
    "Steinwurm": [
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Wurmzahn", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Steinhaut-Salbe", "chance": 0.6},
        {"rarity": "selten", "category": "sonstiges", "item": "Splitterstein", "chance": 0.25},
    ],
    
    "Blutegelriese": [
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Blutegelzahn", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "sonstiges", "item": "Schleimhaut", "chance": 0.6},
        {"rarity": "gewöhnlich", "category": "trank", "item": "Mittlerer Gifttrank", "chance": 0.6},
    ],
    
    "Eiswyrmling": [
        {"rarity": "selten", "category": "sonstiges", "item": "Eisschuppe", "chance": 0.25},
        {"rarity": "selten", "category": "sonstiges", "item": "Frostzahn", "chance": 0.25},
        {"rarity": "selten", "category": "trank", "item": "Kälteschutz-Trank", "chance": 0.25},
    ],
    
    "Sandläufer": [
        {"rarity": "selten", "category": "sonstiges", "item": "Giftstachel", "chance": 0.25},
        {"rarity": "selten", "category": "sonstiges", "item": "Chitinpanzer", "chance": 0.25},
        {"rarity": "episch", "category": "sonstiges", "item": "Sandjuwel", "chance": 0.1},
    ],
    
    "Knochenkrieger": [
        {"rarity": "selten", "category": "waffe", "item": "Knochenschwert", "chance": 0.25},
        {"rarity": "selten", "category": "rüstung", "item": "Zerbeulte Eisrüstung", "chance": 0.25},
        {"rarity": "episch", "category": "sonstiges", "item": "Schädelamulet", "chance": 0.1},
    ],
  
#-----------------#
# Schwere Monster #
#-----------------#
    "Schattendämon": [
        {"rarity": "episch", "category": "sonstiges", "item": "Dämonenherz", "chance": 0.1},
        {"rarity": "episch", "category": "sonstiges", "item": "Seelenfragment", "chance": 0.1},
        {"rarity": "episch", "category": "trank", "item": "Großer Trank der Dunkelsicht", "chance": 0.1},
    ],
    
    "Flammen-Golem": [
        {"rarity": "episch", "category": "waffe", "item": "Glutklinge", "chance": 0.1},
        {"rarity": "episch", "category": "rüstung", "item": "Hitzeschutz-Ring", "chance": 0.1},
        {"rarity": "episch", "category": "sonstiges", "item": "Feuerkern", "chance": 0.1},
    ],
    
    "Schattenritter": [
        {"rarity": "legendär", "category": "waffe", "item": "Verfluchtes Schwert", "chance": 0.04},
        {"rarity": "legendär", "category": "rüstung", "item": "Rüstung der Schatten", "chance": 0.04},
        {"rarity": "legendär", "category": "sonstiges", "item": "Seelenstein", "chance": 0.04},
    ],
    
    "Kristallgolem": [
        {"rarity": "selten", "category": "sonstiges", "item": "Kristallfragment", "chance": 0.25},
        {"rarity": "episch", "category": "rüstung", "item": "Kristallrüstung", "chance": 0.1},
        {"rarity": "episch", "category": "sonstiges", "item": "Leuchtender Kern", "chance": 0.1},
    ],
    
    "Schrecken der Tiefen": [
        {"rarity": "selten", "category": "sonstiges", "item": "Tiefseeperle", "chance": 0.25},
        {"rarity": "episch", "category": "waffe", "item": "Tentakelpeitsche", "chance": 0.1},
        {"rarity": "episch", "category": "sonstiges", "item": "Essenz des Ozeans", "chance": 0.1},
    ],
    
    "Drache": [
        {"rarity": "selten", "category": "sonstiges", "item": "Drachenschuppe", "chance": 0.25},
        {"rarity": "episch", "category": "waffe", "item": "Drachenzahn", "chance": 0.1},
        {"rarity": "selten", "category": "trank", "item": "Großer Feuertrank", "chance": 0.25},
    ],

#-------------#
# Bossmonster #
#-------------#
    "Uralter Drache": [
        {"rarity": "mytisch", "category": "waffe", "item": "Drachenzahnklinge", "chance": 0.01},
        {"rarity": "mytisch", "category": "rüstung", "item": "Drachenschuppenrüstung", "chance": 0.01},
        {"rarity": "selten", "category": "trank", "item": "Großer Heiltrank", "chance": 0.25},
    ]
}

#----------------------------------#
# Rarität Wählen auf die Drop Rate #
#----------------------------------#

def roll_rarity():
    """Wählt eine Rarität basierend auf den DROP_RATES."""
    roll = random.randint(1, 100)
    cumulative = 0
    for rarity, chance in DROP_RATES.items():
        cumulative += chance
        if roll <= cumulative:
            return rarity
    return "gewöhnlich"  # Fallback

def get_monster_drop(monster_type):
    """Bestimmt ein Item basierend auf Monster-Drops und Rarität."""
    if monster_type not in MONSTER_DROPS:
        return None
    
    rarity = roll_rarity()
    categories = list(MONSTER_DROPS[monster_type].keys())
    category = random.choice(categories)  # zufällige Kategorie
    items = MONSTER_DROPS[monster_type][category][rarity]
    
    if not items:
        return None
    
    item = random.choice(items)
    return f"{item} ({rarity})"