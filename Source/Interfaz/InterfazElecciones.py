#!/usr/bin/env python
# coding=utf-8
# @Author: Joan Andrés
# @Date: -*- -*- -*-
# @Email: andres6936@gmail.com
# @Email: andres6936@live.com

import wx

from Source.Mundo.Urna import Urna
from Source.Interfaz.PanelUrna import PanelUrna
from Source.Interfaz.PanelImage import PanelImagen
from Source.Interfaz.PanelCandidato import PanelCandidato
from Source.Interfaz.PanelExtension import PanelExtension

class InterfazElecciones(wx.Frame):

    # ---------------------------------
    # Constructor
    # ---------------------------------

    def __init__(self, *args, **kw):

        # Enviamos todos los parametros a la clase padre.
        super().__init__(*args, **kw)

        self.SetBackgroundColour('White')

        # Creamos la clase principal.
        self.urna = Urna()

        # Construye la forma.
        self.SetTitle('Elecciones Python')
        self.SetSize(wx.Size(800, 600))
        self.SetMaxSize(wx.Size(800, 600))
        self.SetMinSize(wx.Size(800, 600))
        self.Show(True)

        # Creación de los paneles aquí.

        # Panel Imagen
        self.panelImagen = PanelImagen(self, -1)

        # Construye los paneles de los tres candidatos
        self.panelCandidato1 = PanelCandidato(self, -1, nNumeroCandidato=1)
        self.panelCandidato2 = PanelCandidato(self, -1, nNumeroCandidato=2)
        self.panelCandidato3 = PanelCandidato(self, -1, nNumeroCandidato=3)

        # Panel Urna
        self.panelUrna = PanelUrna(self, -1)

        # Panel Extensión
        self.panelExtension = PanelExtension(self, -1)

        # Construye la posición de los paneles con forme al frame
        sizerLayoutRoot = wx.BoxSizer(wx.VERTICAL)
        sizerLayoutImagen = wx.BoxSizer(wx.VERTICAL)
        sizerLayoutCandidatos = wx.BoxSizer(wx.HORIZONTAL)
        sizerLayoutCandidato1 = wx.StaticBoxSizer(wx.VERTICAL, self, 'Candidato 1')
        sizerLayoutCandidato2 = wx.StaticBoxSizer(wx.VERTICAL, self, 'Candidato 2')
        sizerLayoutCandidato3 = wx.StaticBoxSizer(wx.VERTICAL, self, 'Candidato 3')
        sizerLayoutUrna = wx.StaticBoxSizer(wx.VERTICAL, self, 'Urna')
        sizerLayoutOpciones = wx.StaticBoxSizer(wx.VERTICAL, self, 'Opciones')

        sizerLayoutImagen.Add(self.panelImagen, 1, wx.EXPAND)
        sizerLayoutCandidato1.Add(self.panelCandidato1, 1, wx.EXPAND)
        sizerLayoutCandidato2.Add(self.panelCandidato2, 1, wx.EXPAND)
        sizerLayoutCandidato3.Add(self.panelCandidato3, 1, wx.EXPAND)
        sizerLayoutCandidatos.Add(sizerLayoutCandidato1, 1, wx.EXPAND)
        sizerLayoutCandidatos.Add(sizerLayoutCandidato2, 1, wx.EXPAND)
        sizerLayoutCandidatos.Add(sizerLayoutCandidato3, 1, wx.EXPAND)
        sizerLayoutUrna.Add(self.panelUrna, 1, wx.EXPAND)
        sizerLayoutOpciones.Add(self.panelExtension, 1, wx.EXPAND)

        sizerLayoutRoot.Add(sizerLayoutImagen, 1, wx.EXPAND)
        sizerLayoutRoot.Add(sizerLayoutCandidatos, 2, wx.EXPAND)
        sizerLayoutRoot.Add(sizerLayoutUrna, 1, wx.EXPAND)
        sizerLayoutRoot.Add(sizerLayoutOpciones, 0, wx.EXPAND)

        self.SetSizer(sizerLayoutRoot)
        self.Layout()
        self.Fit()

        self.Actualizar()

    # ---------------------------------
    # Métodos
    # ---------------------------------


    def AdicionarVotoCandidato(self, numCandidato):
        pass

    def VaciarUrna(self) -> None:
        """
        Restaura la urna.
        """
        self.urna.VaciarUrna()
        self.Actualizar()

    def MostrarDialogoPorcentajeVotos(self, numCandidato):
        pass

    def GetTotalVotosUrna(self):
        pass

    def Actualizar(self) -> None:
        """
        Actualiza la visualización de la interfaz.
        @postcondition: Se actualiza la visualización.
        """
        self.panelCandidato1.Actualizar( self.urna.GetCandidato1() )
        self.panelCandidato2.Actualizar( self.urna.GetCandidato2() )
        self.panelCandidato3.Actualizar( self.urna.GetCandidato3() )
        self.panelUrna.Actualizar( self.urna )

    def FormatearValorReal(self):
        pass

    def reqFuncOpcion1(self):
        pass

    def reqFuncOpcion2(self):
        pass