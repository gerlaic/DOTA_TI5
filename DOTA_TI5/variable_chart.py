#INPUT PARAMETERS
#############################################################
team_name ='c9'
folder_name = 'C:/Users/DafashiTuzi/Desktop/TI5/'

#############################################################
#VARIABLES THAT WE DONT REALLY WANT TO CHANGE EVERYTIME
#############################################################

#team
#############################################################
ti_team = ['VG','EG','SECRET','IG','LGD','C9','EMPIRE','VP','COL','NEWBEE','FNATIC','EHOME','NAVI','MVPH']

#hero
#############################################################
all_hero = ['AA','ABA','ALCHE','AM','AXE','BANE','BAT','BB','BH','BM','BREW','BROOD','BS','CENT','CHEN','CK','CLINKZ','CLOCK','CM','DAZZLE','DISRUPT','DOOM','DP','DRAGON','DROW','DS','DUSA','EMBER','ENCH','ENIGMA','ES','ESPIRIT','ET','GYRO','HUSKA','IO','JAKI','JUGG','KOTL','KUNKKA','LC','LD','LESH','LICH','LINA','LION','LS','LUNA','LYCAN','MAG','MEEPO','MIRANA','MORPH','MYX','NAGA','NECRO','NP','NS','OD','OGRE','OMNI','PA','PHOE','PL','PUCK','PUDGE','PUGNA','QOP','RAZOR','RIKI','RUBICK','SB','SD','SF','SHAMAN','SILENCE','SK','SKY','SLARD','SLARK','SNIPER','SPEC','SS','SVEN','TA','TB','TECHIE','TIDE','TIMBER','TINKER','TINY','TREANT','TROLL','TUSK','UD','URSA','VENO','VIP','VIS','VOID','VOKER','VS','WARLOCK','WD','WEAVER','WK','WR','WW','ZEUS']
#position analyzer
farming_hero = ['ALCHE','AM','DROW','DUSA','GYRO','JUGG','LD']
ganking_hero = ['AXE','BAT','BB','BREW','BROOD','BS','CK','CLINKZ','CLOCK','DOOM','DP','DRAGON','DS','EMBER','ES','ET','HUSKA','JAKI','KUNKKA','LESH']
team_control_hero = ['AXE','CENT','EMBER','ENIGMA','ES','ET','JAKI','KUNKKA']
solo_control_hero = ['BANE','BAT','BREW','CK','CLOCK','CM','DISRUPT','DOOM','DRAGON','ENCH','KUNKKA','LC']
jungle_hero = ['CHEN','CM','ENCH','ENIGMA','SK']
support_hero = ['AA','ABA','BANE','BH','CHEN','CM','DAZZLE','DISRUPT','ENCH','ENIGMA','ES','ET','IO','KOTL']
#end at lesh

#combo analyzer
used_hero = []
oppo_used_hero = []

#bp
#############################################################
general_bp = []
