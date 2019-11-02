#!/usr/bin/python3

# Imports 
import os, sys, random, requests, concurrent.futures

# Colors
if 'win' not in sys.platform:
    R = '\033[1;31m'
    T = '\033[1;33m'
    B = '\033[1;34m'
    G = '\033[1;32m'
    W = '\033[1;37m'
    N = '\033[0m'
else:
    R = T = B = G = W = N = str()

    
# Start 
class GETTHEUSER:
    WEBSITES = [
        'github.com/Y', 
        'www.instagram.com/Y',
        'www.facebook.com/Y',
        'www.twitter.com/Y',
        'www.youtube.com/Y',
        'Y.blogspot.com',
        'plus.google.com/Y/posts',
        'www.reddit.com/user/Y',
        'Y.wordpress.com',
        'www.pinterest.com/Y',
        'Y.tumblr.com',
        'www.flickr.com/people/Y',
        'steamcommunity.com/id/Y',
        'vimeo.com/Y',
        'soundcloud.com/Y',
        'disqus.com/Y',
        'medium.com/@Y',
        'Y.deviantart.com',
        'vk.com/Y',
        'about.me/Y',
        'imgur.com/user/Y',
        'flipboard.com/@Y',
        'slideshare.net/Y',
        'fotolog.com/Y',
        'open.spotify.com/user/Y',
        'www.mixcloud.com/Y',
        'www.scribd.com/Y',
        'www.badoo.com/en/Y',
        'www.patreon.com/Y',
        'bitbucket.org/Y',
        'www.dailymotion.com/Y',
        'www.etsy.com/shop/Y',
        'cash.me/Y',
        'www.behance.net/Y',
        'www.goodreads.com/Y',
        'www.instructables.com/member/Y',
        'keybase.io/Y',
        'kongregate.com/accounts/Y',
        'Y.livejournal.com'
        'angel.co/Y',
        'last.fm/user/Y',
        'dribbble.com/Y',
        'www.codecademy.com/Y',
        'en.gravatar.com/Y',
        'pastebin.com/u/Y',
        'foursquare.com/Y',
        'www.roblox.com/user.aspx?username=Y',
        'www.gumroad.com/Y',
        'Y.newgrounds.com',
        'www.wattpad.com/user/Y', 
        'www.canva.com/Y', 
        'creativemarket.com/Y', 
        'www.trakt.tv/users/Y', 
        '500px.com/Y', 
        'buzzfeed.com/Y', 
        'tripadvisor.com/members/Y', 
        'Y.hubpages.com', 
        'Y.contently.com',
        'houzz.com/user/Y', 
        'blip.fm/Y', 
        'www.wikipedia.org/wiki/User:Y', 
        'news.ycombinator.com/user?id=Y', 
        'www.codementor.io/Y', 
        'www.reverbnation.com/Y', 
        'www.designspiration.ne/Yt', 
        'www.bandcamp.com/Y', 
        'www.colourlovers.com/Y', 
        'www.ifttt.com/love/Y', 
        'www.ebay.com/p/Y',
        'Y.slack.com', 
        'www.okcupid.com/profile/Y', 
        'www.trip.skyscanner.com/user/Y', 
        'ello.co/Y', 
        'tracky.com/Y', 
        'www.tripit.com/people/Y#/profile/basic-info', 
        'Y.basecamphq.com/login'
    ]
    SaveU  = []


    def __init__(self, target, save):
        self.target = target
        self.Save   = save 
        self.URL    = []
        self.SIS    = requests.Session()
        self.INT    = int()
   
    def SAVE(self, DATA):[open(self.Save, 'a').write(f'{i}\n') for i in DATA]
        
    def GET_RUN_INDEX(self):
    
        print(f"{W}{'-'*50}{N}\n[ {B}+{N} ] Target  : \
{self.target}\n[ {B}+{N} ] Checking: {len(self.WEBSITES)}\n[ {B}+{N} ] SaveFile: \
{self.Save}\n[{B}==>{N}] Plaes Wite....\n{W}{'-'*50}{N}")

        input(f"\033[7m{B}------ Enter To (Start) ------{N}")
        
        print(f"\n\n\n[ {T}+{N} ] GET USER:{B}\n\t|\n\t|\n\t|{N}")

    def GET_URL_TARGET(self, MYINT): 
        ''' The User-Agent request header contains a characteristic 
          string that allows the network protocol peers to identify 
          the application type.'''
              
        self.SIS.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko" 
        try:
            GET = self.SIS.get(f"https://{MYINT.replace('Y', self.target)}").status_code # 200 or 404 etc...

        except requests.exceptions.ConnectionError:
            return f"{B}\t|{W}-{N}[{R}{'ERROR'}{N}]{W}-> {R}!!!{N} Connection {G}Error{N}"

        if GET == 200:
        
            self.SaveU.append(MYINT.replace('Y', self.target))
            return f"{B}\t|{R}-{N}[ {T}{GET}{N} ]{T}->{N} Found! {W}https://{MYINT.replace('Y', G+self.target+N)}"
             
        else:
            
            return f"{B}\t|{R}-{N}[ {R}{GET}{N} ]{R}->{N}  Not Found {W}https://{MYINT.replace('Y', G+self.target+N)}"
        
        
   
    def GET_THE_URL(self):
        self.GET_RUN_INDEX()

        while True:
            y = True

            m = random.sample(self.WEBSITES, True)
            
            if m[0] not in self.URL:
                
                self.URL.append(m[0])
                
                if len(self.URL) == len(self.WEBSITES):y = False
                
                with concurrent.futures.ThreadPoolExecutor() as EX:
                    rDATA = EX.submit(self.GET_URL_TARGET, m[0])
                    
                    print(rDATA.result())

            if y == False: break

        self.SAVE(self.SaveU)



if __name__ == "__main__":
    try:s, *user  = sys.argv
        
    except:pass
    
    if user == []:
        user  = input(f"[ {R}!{N} ] Enter User Target: ")
        user = [user, 'url.txt']
        
    if user[0] == '-h' or user[0] == '--help':
            print(f"EX:\npython {s} <User-Target> <File-Output>")
            exit()
    
    root = GETTHEUSER(user[0],user[1] if len(user) > 1 else "url.txt")
    root.GET_THE_URL()

    input(f"\n\n\n\033[7m{R}------ Enter To (Exit) ------{N}")
