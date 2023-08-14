class Note:
    sobaka = 100

    def __init__(self, suka):
        self.suka = suka

note1 = Note('bliat')
note2 = Note('beach')
print(note2.sobaka, note1.sobaka)
note1.sobaka = 50
print(note1.sobaka, note2.sobaka)