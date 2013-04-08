#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade HG on Thu Mar 14 17:01:31 2013

import wx

# begin wxGlade: extracode
# end wxGlade



class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainFrame.__init__
        kwds["style"] = wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.MAXIMIZE | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.RESIZE_BORDER | wx.CLIP_CHILDREN
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        self.realizar_backup = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Realizar Backup", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.realizar_backup)
        self.restaurar_backup = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Restaurar de Backup", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.restaurar_backup)
        self.frame_menubar.Append(wxglade_tmp_menu, "Archivo")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu_sub = wx.Menu()
        self.ver_disponibles = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Disponibles", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_disponibles)
        self.ver_condicionales = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Condicionales", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_condicionales)
        self.ver_vendidas = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Vendidas", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_vendidas)
        wxglade_tmp_menu.AppendMenu(wx.NewId(), "Prendas", wxglade_tmp_menu_sub, "")
        wxglade_tmp_menu_sub = wx.Menu()
        self.ver_al_dia = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Al dia", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_al_dia)
        self.ver_tardios = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Tardios", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_tardios)
        self.ver_morosos = wx.MenuItem(wxglade_tmp_menu_sub, wx.NewId(), "Morosos", "", wx.ITEM_CHECK)
        wxglade_tmp_menu_sub.AppendItem(self.ver_morosos)
        wxglade_tmp_menu.AppendMenu(wx.NewId(), "Clientes", wxglade_tmp_menu_sub, "")
        self.frame_menubar.Append(wxglade_tmp_menu, "Ver")
        wxglade_tmp_menu = wx.Menu()
        self.vaciar_carrito = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Vaciar Carrito", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.vaciar_carrito)
        self.borrar_todo = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Borrar todo ", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.borrar_todo)
        self.frame_menubar.Append(wxglade_tmp_menu, "Herramientas")
        wxglade_tmp_menu = wx.Menu()
        self.informe_lista_correos = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Lista de correos", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_lista_correos)
        self.informe_lista_correos_morosos = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Lista de correos morosos", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_lista_correos_morosos)
        self.informe_lista_telefonos = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Lista de telefonos", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_lista_telefonos)
        self.informe_lista_telefonos_morosos = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Lista de telefonos de morosos", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_lista_telefonos_morosos)
        self.informe_lista_cumpleanios_mes = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), u"Lista de cumpleaños del mes", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_lista_cumpleanios_mes)
        self.informe_totales = wx.MenuItem(wxglade_tmp_menu, wx.NewId(), "Totales de ganancias y deudas", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendItem(self.informe_totales)
        self.frame_menubar.Append(wxglade_tmp_menu, "Informes")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.panel_1 = wx.Panel(self, -1)
        self.boton_solapas_prendas_clientes = wx.Notebook(self.panel_1, -1, style=0)
        self.notebook_1_pane_1 = wx.Panel(self.boton_solapas_prendas_clientes, -1)
        self.texto_buscar_prendas = wx.TextCtrl(self.notebook_1_pane_1, -1, "Buscar...")
        self.radio_box_prendas = wx.RadioBox(self.notebook_1_pane_1, -1, "Buscar por", choices=["Codigo", "Nombre"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.lista_prendas = wx.ListCtrl(self.notebook_1_pane_1, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.boton_detalle_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Detalle")
        self.boton_eliminar_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Eliminar")
        self.boton_nuevo_prendas = wx.Button(self.notebook_1_pane_1, -1, "&Nuevo")
        self.boton_agregar_quitar = wx.Button(self.notebook_1_pane_1, -1, "Agregar")
        self.boton_realizar_venta = wx.Button(self.notebook_1_pane_1, -1, "Realizar &Venta")
        self.notebook_1_pane_2 = wx.Panel(self.boton_solapas_prendas_clientes, -1)
        self.texto_buscar_clientes = wx.TextCtrl(self.notebook_1_pane_2, -1, "Buscar...")
        self.radio_box_clientes = wx.RadioBox(self.notebook_1_pane_2, -1, "Buscar por", choices=["DNI", "Nombre"], majorDimension=0, style=wx.RA_SPECIFY_COLS)
        self.lista_clientes = wx.ListCtrl(self.notebook_1_pane_2, -1, style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        self.boton_detalle_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Detalle")
        self.boton_eliminar_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Eliminar")
        self.boton_nuevo_clientes = wx.Button(self.notebook_1_pane_2, -1, "&Nuevo")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle("Dress")
        self.SetSize((803, 500))
        self.SetFocus()
        self.texto_buscar_prendas.SetMinSize((250, 22))
        self.texto_buscar_prendas.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_box_prendas.SetSelection(0)
        self.lista_prendas.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.boton_detalle_prendas.SetDefault()
        self.boton_realizar_venta.SetMinSize((130, 30))
        self.boton_realizar_venta.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.notebook_1_pane_1.SetFont(wx.Font(8, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.texto_buscar_clientes.SetMinSize((250, 22))
        self.texto_buscar_clientes.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.radio_box_clientes.SetSelection(0)
        self.lista_clientes.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))
        self.boton_detalle_clientes.SetDefault()
        self.boton_solapas_prendas_clientes.SetFont(wx.Font(11, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_3_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_6_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7_copy = wx.BoxSizer(wx.VERTICAL)
        sizer_4_copy = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(self.texto_buscar_prendas, 0, wx.ALL, 10)
        sizer_4.Add(self.radio_box_prendas, 0, 0, 0)
        sizer_3.Add(sizer_4, 0, wx.EXPAND, 0)
        sizer_6.Add(self.lista_prendas, 1, wx.LEFT | wx.RIGHT | wx.EXPAND | wx.ALIGN_RIGHT, 10)
        sizer_7.Add(self.boton_detalle_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_eliminar_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_nuevo_prendas, 0, wx.TOP | wx.BOTTOM, 3)
        sizer_7.Add(self.boton_agregar_quitar, 0, wx.TOP | wx.ALIGN_CENTER_HORIZONTAL, 120)
        sizer_6.Add(sizer_7, 0, wx.RIGHT, 10)
        sizer_3.Add(sizer_6, 1, wx.EXPAND, 0)
        sizer_8.Add(self.boton_realizar_venta, 0, wx.ALL | wx.ALIGN_RIGHT, 10)
        sizer_3.Add(sizer_8, 0, wx.ALIGN_RIGHT, 0)
        self.notebook_1_pane_1.SetSizer(sizer_3)
        sizer_4_copy.Add(self.texto_buscar_clientes, 0, wx.ALL, 10)
        sizer_4_copy.Add(self.radio_box_clientes, 0, 0, 0)
        sizer_3_copy.Add(sizer_4_copy, 0, wx.EXPAND, 0)
        sizer_6_copy.Add(self.lista_clientes, 1, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND | wx.ALIGN_RIGHT, 10)
        sizer_7_copy.Add(self.boton_detalle_clientes, 0, wx.ALL, 3)
        sizer_7_copy.Add(self.boton_eliminar_clientes, 0, wx.ALL, 3)
        sizer_7_copy.Add(self.boton_nuevo_clientes, 0, wx.ALL, 3)
        sizer_6_copy.Add(sizer_7_copy, 0, wx.RIGHT, 10)
        sizer_3_copy.Add(sizer_6_copy, 1, wx.EXPAND, 0)
        self.notebook_1_pane_2.SetSizer(sizer_3_copy)
        self.boton_solapas_prendas_clientes.AddPage(self.notebook_1_pane_1, "Prendas")
        self.boton_solapas_prendas_clientes.AddPage(self.notebook_1_pane_2, "Clientes")
        sizer_2.Add(self.boton_solapas_prendas_clientes, 1, wx.EXPAND, 0)
        self.panel_1.SetSizer(sizer_2)
        sizer_1.Add(self.panel_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

# end of class MainFrame


if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_1 = MainFrame(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()
