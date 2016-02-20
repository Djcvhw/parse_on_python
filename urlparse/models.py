from django.db import models
from djwebsockets.decorator import Namespace
from djwebsockets.mixins.wsgi import WSGIMixin
from djwebsockets.websocket import BaseWSClass

@Namespace("/parse/")
class ParserServ(WSGIMixin, BaseWSClass):
    clients = []

    @classmethod
    def on_connect(cls, socket, path):
        ParserServ.clients.append(socket)
        msg = "{} has joined room".format(str(socket.id))
        print(msg)

    @classmethod
    def on_message(cls, socket, message):
        for client in ParserServ.clients:
            if socket.id != client.id:
                msg = "--------"+message+'\n'
                print(msg)
                client.send(message)

    @classmethod
    def on_close(cls, socket):
        socket.close()

class Url(models.Model):
    url = models.CharField(max_length=255)
    timeshift = models.TimeField(default='00:00:00')

    def __str__(self):
        return self.url

class Info(models.Model):
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    encoding = models.CharField(max_length=255)
    h1 = models.CharField(max_length=255, null=True)