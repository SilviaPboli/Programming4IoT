import json
import datetime
import cherrypy

class WebService:
    exposed=True
    
    def GET(self,*uri,**params):
        pass
    
    def PUT(*uri,**params):
        pass






class Discography:
    #exposed=True
    
    def __init__(self,text):
        
        file_name='ex_1.3.json'
        in_file=open(file_name,'r')
        text=in_file.read()
        in_file.close()
        text=json.loads(text)
    
        self.data=text #data è un dizionario
        self.last_update=self.data['last_update']
        self.now=datetime.datetime.now()
               
    def search_artist(self,artist):
       
        ans=[]
        for album in self.data['album_list']:
            if (album["artist"]==artist):
                ans.append(album)
        if ans==[]:
            return 'not found'
        else:
            return ans
        
    def search_title(self,title):
        ans=[]
        for album in self.data['album_list']:
            if (album["title"]==title):
               ans.append(album)
        if ans==[]:
            return 'not found'
        else:
            return ans
               
    def search_year(self,year):
        ans=[]
        for album in self.data['album_list']:
            if (album["publication_year"]==int(year)):
               ans.append(album)
        if ans==[]:
            return 'not found'
        else:
            return ans
               
    def search_tot_tracks(self,tot_track):
        ans=[]
        for album in self.data['album_list']:
            if (album["total_tracks"]==int(tot_track)):
               ans.append(album)
        if ans==[]:
            return 'not found'
        else:
            return ans
               
    def insert_artist(self,insert_album):
        for album in self.data['album_list']:
            if (album["title"]==insert_album):
               print('Album already in the list')
               update=input('do you want to update it? [y] [n]')
               if update!='y':
                   return self.data['last_update']
               else:
                   album['artist']=input('Enter artist: ')
                   album['publication_year']=input('Enter publication year: ')
                   album['total_tracks']=input('Enter total traks: ')
                   self.data['last_update']=self.now.strftime('%Y-%m-%d %H:%M')
                   return self.data['last_update']
        
        insert={}
        insert['artist']=input('Enter artist: ')
        insert['title']=insert_album
        insert['publication_year']=input('Enter publication year: ')
        insert['total_tracks']=input('Enter total traks: ')
        self.data['album_list'].append(insert)
        self.data['last_update']=self.now.strftime('%Y-%m-%d %H:%M')
        return self.data['last_update']
        
        
    def print_all(self):
        print(self.data)      
        return 
    
    def save_all(self,file_name):
        out_file=open(file_name,'w')
        out_file.write(json.dumps(self.data))
        out_file.close()
        return self.data['last_update']




if __name__=='__main__':
    
    cherrypy.config.update({'server.socket_host': '0.0.0.0'})
    cherrypy.config.update({'server.socket_port': 8080})
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            #'tools.session.on': True,
            }
        }
    cherrypy.tree.mount(WebService(),'/', conf)
    cherrypy.engine.start()
    cherrypy.engine.block()



    
#    file_name='PIOT1_3.json'
#    in_file=open(file_name,'r')
#    text=in_file.read()
#    in_file.close()
#    text=json.loads(text)
#    disc=Discography(text)
#    choice='c'
#    while choice!='E':
#        print('Select a choice:')
#        print('search by [A]rtist')
#        print('search by [T]itle')
#        print('search by publication [Y]ear')
#        print('search by [t]otal tracks')
#        print('[I]nsert new disc')
#        print('[P]rint all')
#        print('[E]xit')
#        choice=input()
#        
#        if choice=='A':
#            artist=input('Insert artist name:')
#            print(disc.search_artist(artist))
#            print('\n')
#        elif choice=='T':
#            title=input('Insert title:')
#            print(disc.search_title(title))
#            print('\n')
#        elif choice=='Y':
#            year=input('Insert an year:')
#            print(disc.search_year(year))
#            print('\n')
#        elif choice=='t':
#            tot_tracks=input('Insert total tracks:')
#            print(disc.search_tot_tracks(tot_tracks))
#            print('\n')
#        elif choice=='I':
#            insert_album=input('write the album you want to insert:')
#            print('Last update: %r '% disc.insert_artist(insert_album))
#            print('\n')
#        elif choice=='P':
#            disc.print_all()
#            print('\n')
#        else: 
#            print('Last update: %r '% disc.save_all(file_name))
#            print('\n')
#            break
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
  