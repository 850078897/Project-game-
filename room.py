import pygame
#list of tupples (image,[text list],( (choice1 text,choice num),(choice1 text,choice num))
rooms=[ ("space.jpg",["I wake up in a dim light...","Remember before you went to hospital, you fainted from overwork, and now...No one has.","You slowly get up and change your clothes and get out of the rest room.","Seems to hear a bit of human breathing?"],
        (("1. Chasing after",1),("2. Leave right away, down the stairs",100))),
        ("space2.jpg",[ "You find your voice in the corridor. Then you walk past.","You ran to the building and found a little boy in the corner,","a thirteen-year-old boy, who saw you and suddenly", "raised an old handgun and buckled the board...","Bang!","Your left arm was bruised, though you were flashing.","You're angry, you're not easy to recover, and you're hurt again.Facing the boy, you're ready to..."],
        (("1. Show kindenss to the boy, but keep a certain distance", 3), ("2. He has a gun, and you don't have anything, go downstairs!", 9)))
          ]


class Room:
    """represents a room with, number, image, question list, choices"""
    def __init__(self,num,display):
        """create a room with, number, image, question list, choices"""
        self.num = num
        self.image=rooms[num][0]
        self.text=rooms[num][1]
        self.choices=rooms[num][2]
        self.display = display

    def showimg(self):
       room_img = pygame.image.load(self.image)
       self.display.blit(room_img, (0, 0))

    def showtext(self):
        for i in self.text:
            break