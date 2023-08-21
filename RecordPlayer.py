from DataStruts import Queue

## Discs come as a one entry dictionary {name_of_album:list_of_songs}

## This function circles around the values of a queue

def HotPot(num, queue):

    while num > 0:

        queue.enqueue(queue.dequeue())

        num = num - 1

    return queue

## A class for jukebox with a surrogate RecordPlayer class.

class JukeBox:

    def __init__(self):

        self.records = Queue()

        self.current_disc = RecordPlayer()

    def add_disc(self, disc):

        self.records.enqueue(disc)

        print("Adding Disc: " + str(disc) + "\n")

    def load(self):

        print("Loading Disc: " + str(self.records.peek_top()))


        self.current_disc.upload_album(self.records.peek_top())

    def get_topDisk(self):

        print("This is the current disc in the album queue: " +

              str(self.records.peek_top()) + "\n")

    def get_current(self):

        print("This is the current disc on the record player: \n" +

              str(self.current_disc.view_album()) + "\n")

##        return self.current_disc.view_album()


    def play_current(self):

        return self.current_disc.play()

    def next_album(self):

        self.records = HotPot(1, self.records)

        print("This is the current disc in the album queue: "

              + str(self.records.peek_top()) + "\n")



    def next_song(self):

        return self.current_disc.play_next()

        

    def previous_song(self):

        return self.current_disc.play_previous()

##    def start_again(self):    


class RecordPlayer:

    def __init__(self):

        self.album_tracks = Queue()

        self.album_name = ""

    def view_album(self):

        return self.album_name

    def view_song(self):

        return self.album_tracks.peek_top()


    def upload_album(self, disc):

        self.album_tracks = Queue()

        for item in disc:

            self.album_name = item

            for song in disc[item]:

                self.album_tracks.enqueue(song)


    def is_empty(self):

        return self.album_name


    def play(self):

        print("Currently playing: " + str(self.album_tracks.peek_top()) + "\n")

        return self.album_tracks.peek_top()


    def play_next(self):

        HotPot(1, self.album_tracks)

        self.play()

    def play_previous(self):

        HotPot(self.album_tracks.check_length()-1, self.album_tracks)

        self.play()

    

        
Juky = JukeBox()
ElvisPresely = {"How Great Thou Art": ["How Great Thou Art",

                                       "Somebody Bigger Then You", "Stand By Me",

                                       "So High"]}

LittleRichard = {"Here's Little Richard": ["Tutti Frutti", "Baby",

                                           "Long Tall Sally"]}

Juky.add_disc(ElvisPresely)

Juky.add_disc(LittleRichard)

Juky.load()

Juky.get_current()

Juky.next_album()

Juky.get_current()


Juky.play_current()

Juky.next_song()

Juky.previous_song()

Juky.next_song()

Juky.next_song()

Juky.get_topDisk()

Juky.load()

Juky.play_current()




