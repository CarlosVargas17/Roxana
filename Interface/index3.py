import spotipy as sp
from spotipy.oauth2 import SpotifyOAuth
from tkinter import *
class pruebas():
    def inicial(self):
        cid = 'bc86bcbfd2ff4001a247c0c5525a1c6f'
        secret = '54701e1d88764ec086dbbbb8ff5fc1dd'
        redirecturi= 'https://open.spotify.com/'
        scope='user-read-private user-read-playback-state user-modify-playback-state user-read-private'
        username='None'
        device_name="None"

        # Connecting to the Spotify account
        auth_manager = SpotifyOAuth(
            client_id=cid,
            client_secret=secret,
            redirect_uri=redirecturi,
            scope=scope,
            username=username,
            show_dialog="True")
        splogin = sp.Spotify(auth_manager=auth_manager)
        self.devices = splogin.devices()
        print(self.devices)

        # Selecting device to play from


        deviceID = None
        for d in self.devices['devices']:
            d['name'] = d['name'].replace('’', '\'')
            if d['name'] == device_name:
                deviceID = d['id']
                break
        command = "play Miénteme Camilo Séptimo"
        name = "Camilo Séptimo Mix"
        print(command)
        if "play" in command:
            uri = self.get_track_uri(splogin, name)
            self.play_album(splogin, deviceID, uri)
        if "next" in command:
            splogin.next_track()
    def get_track_uri(self, Spotify, name):
        """
        :param spotify: Spotify object to make the search from
        :param name: track name
        :return: Spotify uri of the desired track
        """

        # Replace all spaces in name with '+'
        original = name
        name = name.replace(' ', '+')

        results = Spotify.search(q=name, limit=1, type='playlist')
        album_uri = results['playlist']['items'][0]['uri']
        return album_uri


    def play_track(self, spotify, device_id, uri):
        spotify.start_playback(device_id=device_id, uris=[uri])

    def play_album(self,spotify=None, device_id=None, uri=None):
        spotify.start_playback(device_id=device_id, context_uri=uri)


a=pruebas()
a.inicial()