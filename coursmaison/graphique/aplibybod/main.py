"""ce programme contient l api de notre soft"""
import vlc
import utils as utl 
def playsoud():
    player = vlc.MediaPlayer("/media/ensdia-algalon.wav")
    player.play()
    
playsoud()
