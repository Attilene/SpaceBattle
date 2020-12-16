import pygame as pg

from config import Configuration as Conf
from elements.meteor import Meteor
from elements.piece import Piece
from utils.group import Group


class Spawner:
    @staticmethod
    def all_pieces(on_field: bool):
        while len(Group.PIECES) < Conf.Piece.QUANTITY:
            piece = Piece()
            if on_field:
                piece.locate(*Piece.GetCoord().get_on_field())
            else:
                piece.locate(*Piece.GetCoord().get_out_field())
            Group.ALL.add(piece)
            Group.PIECES.add(piece)

    @staticmethod
    def all_meteors():
        """
        Spawn all meteors by time or quantity configurations
        """
        while len(Group.METEORS) < Conf.Meteor.QUANTITY:
            Spawner.meteor()

    @staticmethod
    def meteor():
        """
        Spawn simple meteor on the field
        """
        meteor = Meteor()
        if Conf.Meteor.ON_FIELD:
            meteor.locate(*Meteor.GetCoord().get_on_field())
        else:
            meteor.locate(*Meteor.GetCoord().get_out_field())
        Group.ALL.add(meteor)
        Group.METEORS.add(meteor)
