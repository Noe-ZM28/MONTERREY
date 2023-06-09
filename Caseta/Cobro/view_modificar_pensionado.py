from tkinter import messagebox as mb
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, IntVar

from datetime import datetime

from queries import pensionados
import traceback


from dateutil.relativedelta import relativedelta

class View_modificar_pensionados():

	def __init__(self, datos_pensionado):
		self.query = pensionados()
		self.datos_pensionado = datos_pensionado

		# Crea la ventana principal
		self.panel_crud = tk.Toplevel()

		# Se elimina la funcionalidad del botón de cerrar
		self.panel_crud.protocol("WM_DELETE_WINDOW", lambda: self.desconectar())

		# Deshabilita los botones de minimizar y maximizar
		# self.panel_crud.attributes('-toolwindow', True)

		self.panel_crud.title(f'Modificar pensionado')

		# Configura la columna principal del panel para que use todo el espacio disponible
		self.panel_crud.columnconfigure(0, weight=1)


		self.variable_numero_tarjeta = StringVar()
		self.variable_numero_tarjeta.set(datos_pensionado[0][0])
		
		self.variable_nombre = StringVar()
		self.variable_nombre.set(datos_pensionado[0][1])

		self.variable_apellido_1 = StringVar()
		self.variable_apellido_1.set(datos_pensionado[0][2])

		self.variable_apellido_2 = StringVar()
		self.variable_apellido_2.set(datos_pensionado[0][3])


		self.variable_telefono_1 = StringVar()
		self.variable_telefono_1.set(datos_pensionado[0][4])

		self.variable_telefono_2 = StringVar()
		self.variable_telefono_2.set(datos_pensionado[0][5])

		self.variable_ciudad = StringVar()
		self.variable_ciudad.set(datos_pensionado[0][6])

		self.variable_colonia = StringVar()
		self.variable_colonia.set(datos_pensionado[0][7])

		self.variable_cp = StringVar()
		self.variable_cp.set(datos_pensionado[0][8])

		self.variable_numero_calle = StringVar()
		self.variable_numero_calle.set(datos_pensionado[0][9])

		self.variable_placas = StringVar()
		self.variable_placas.set(datos_pensionado[0][10])

		self.variable_auto_modelo = StringVar()
		self.variable_auto_modelo.set(datos_pensionado[0][11])

		self.variable_auto_color = StringVar()
		self.variable_auto_color.set(datos_pensionado[0][12])

		self.variable_monto = StringVar()
		self.variable_monto.set(datos_pensionado[0][13])

		self.variable_cortesia = StringVar()
		self.variable_cortesia.set(datos_pensionado[0][14])

		self.variable_tolerancia = StringVar()
		self.variable_tolerancia.set("5")

		self.variable_vigencia = StringVar()
		self.variable_vigencia.set(datos_pensionado[0][16])

		self.registros = None

		# Llama a la función interface() que configura la interfaz gráfica
		self.interface()


		# # Calcula la posición de la ventana en la pantalla
		# pos_x = int(self.seccion_tabla.winfo_screenwidth() / 2)
		# pos_y = int(self.seccion_tabla.winfo_screenheight() / 2)

		# # Establece la geometría de la ventana con su posición y tamaño
		# self.panel_crud.geometry(f"+{pos_x}+{pos_y}")
		self.panel_crud.resizable(False, False)

		# Inicia el loop principal de la ventana
		self.panel_crud.mainloop()

	def interface(self):
		"""
		Crea toda la interface para cambiar de conexion

		:param None: 

		:raises None: 

		:return:
			- None
		"""
		# Se crea un Label Frame principal para la sección superior
		seccion_superior = tk.LabelFrame(self.panel_crud, text='')
		seccion_superior.columnconfigure(1, weight=1)
		seccion_superior.propagate(True)
		seccion_superior.grid(row=0, column=0, sticky=tk.NSEW)

		##########################################################################################################

		# Se crea un Label Frame para la sección de la conexión
		etiqueta_user = tk.Label(seccion_superior, text=f'Bienvenido/a')
		etiqueta_user.grid(row=0, column=0, padx=5, pady=5)

		seccion_datos_pensionado = ttk.LabelFrame(seccion_superior, text="\t\t\tIngresa los datos del pensionado a registrar")
		seccion_datos_pensionado.grid(row=1, column=0,padx=5, pady=5, sticky=tk.NW)


		seccion_datos_personales_pensionado = tk.LabelFrame(seccion_datos_pensionado, text="Datos personales del pensionado")
		seccion_datos_personales_pensionado.grid(row=2, column=0,padx=5, pady=5, sticky=tk.NW)


		etiqueta_numero_tarjeta = ttk.Label(seccion_datos_personales_pensionado, text='Número de tarjeta: ')
		etiqueta_numero_tarjeta.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
		self.campo_numero_tarjeta = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_numero_tarjeta, state="disabled")
		self.campo_numero_tarjeta.grid(row=0, column=1, padx=5, pady=5)

		etiqueta_nombre_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Nombre: ')
		etiqueta_nombre_pensionado.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_nombre_pensinado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_nombre)
		campo_nombre_pensinado.grid(row=1, column=1, padx=5, pady=5)

		etiqueta_apellido_1_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Primer apellido: ')
		etiqueta_apellido_1_pensionado.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_apellido_1_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_apellido_1)
		campo_apellido_1_pensionado.grid(row=2, column=1, padx=5, pady=5)

		etiqueta_apellido_2_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Segundo apellido: ')
		etiqueta_apellido_2_pensionado.grid(row=3, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_apellido_2_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_apellido_2)
		campo_apellido_2_pensionado.grid(row=3, column=1, padx=5, pady=5)

		etiqueta_telefono_1_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Telefono 1: ')
		etiqueta_telefono_1_pensionado.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_telefono_1_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_telefono_1)
		campo_telefono_1_pensionado.grid(row=4, column=1, padx=5, pady=5)

		etiqueta_telefono_2_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Telefono 2: ')
		etiqueta_telefono_2_pensionado.grid(row=5, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_telefono_2_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_telefono_2)
		campo_telefono_2_pensionado.grid(row=5, column=1, padx=5, pady=5)

		etiqueta_ciudad_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Ciudad: ')
		etiqueta_ciudad_pensionado.grid(row=7, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_ciudad_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_ciudad)
		campo_ciudad_pensionado.grid(row=7, column=1, padx=5, pady=5)

		etiqueta_colonia_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Colonia: ')
		etiqueta_colonia_pensionado.grid(row=8, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_colonia_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_colonia)
		campo_colonia_pensionado.grid(row=8, column=1, padx=5, pady=5)

		etiqueta_CP_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='CP: ')
		etiqueta_CP_pensionado.grid(row=9, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_CP_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_cp)
		campo_CP_pensionado.grid(row=9, column=1, padx=5, pady=5)

		etiqueta_numero_calle_pensionado = ttk.Label(seccion_datos_personales_pensionado, text='Numero de calle: ')
		etiqueta_numero_calle_pensionado.grid(row=10, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_numero_calle_pensionado = ttk.Entry(seccion_datos_personales_pensionado, textvariable=self.variable_numero_calle)
		campo_numero_calle_pensionado.grid(row=10, column=1, padx=5, pady=5)




		seccion_derecha = ttk.Frame(seccion_datos_pensionado)
		seccion_derecha.grid(row=2, column=1,padx=5, pady=5, sticky=tk.NW)

		seccion_datos_auto_pensionado = tk.LabelFrame(seccion_derecha, text="Datos del auto del pensionado")
		seccion_datos_auto_pensionado.grid(row=0, column=0,padx=5, pady=5, sticky=tk.NW)


		etiqueta_placa_auto_pensionado = ttk.Label(seccion_datos_auto_pensionado, text='Placa: ')
		etiqueta_placa_auto_pensionado.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_placa_auto_pensionado = ttk.Entry(seccion_datos_auto_pensionado, textvariable=self.variable_placas)
		campo_placa_auto_pensionado.grid(row=0, column=1, padx=5, pady=5)

		etiqueta_modelo_auto_pensionado = ttk.Label(seccion_datos_auto_pensionado, text='Modelo: ')
		etiqueta_modelo_auto_pensionado.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_placa_modelo_pensionado = ttk.Entry(seccion_datos_auto_pensionado, textvariable=self.variable_auto_modelo)
		campo_placa_modelo_pensionado.grid(row=1, column=1, padx=5, pady=5)

		etiqueta_color_auto_pensionado = ttk.Label(seccion_datos_auto_pensionado, text='Color: ')
		etiqueta_color_auto_pensionado.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_color_auto_pensionado = ttk.Entry(seccion_datos_auto_pensionado, textvariable=self.variable_auto_color)
		campo_color_auto_pensionado.grid(row=2, column=1, padx=5, pady=5)



		seccion_datos_pension = tk.LabelFrame(seccion_derecha, text="Datos de la pension")
		seccion_datos_pension.grid(row=1, column=0,padx=5, pady=5, sticky=tk.NW)


		etiqueta_monto_dato_pension = ttk.Label(seccion_datos_pension, text='Monto X Mes: ')
		etiqueta_monto_dato_pension.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_monto_dato_pension = ttk.Entry(seccion_datos_pension, textvariable=self.variable_monto)
		campo_monto_dato_pension.grid(row=0, column=1, padx=5, pady=5)

		etiqueta_cortesia_dato_pension = ttk.Label(seccion_datos_pension, text='Cortesia: ')
		etiqueta_cortesia_dato_pension.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NW)

		campo_cortesia_dato_pension = ttk.Combobox(seccion_datos_pension, width=5, state="readonly", textvariable=self.variable_cortesia)
		campo_cortesia_dato_pension["values"] = ["Si", "No"]

		campo_cortesia_dato_pension.grid(row=1, column=1, padx=1, pady=1, sticky=tk.NW)

		etiqueta_color_auto_pensionado = ttk.Label(seccion_datos_pension, text='Tolerancia: ')
		etiqueta_color_auto_pensionado.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NW)
		campo_color_auto_pensionado = ttk.Entry(seccion_datos_pension, textvariable=self.variable_tolerancia)
		campo_color_auto_pensionado.grid(row=2, column=1, padx=5, pady=5)


		seccion_inferior = tk.LabelFrame(self.panel_crud, text='')
		seccion_inferior.grid(row=1, column=0)


		# Crea un botón y lo empaqueta en la seccion_botones_consulta
		boton_modificar_pensionado = tk.Button(seccion_inferior,  text='Activar/Desactivar tarjeta', command = self.activar_desacivar_tarjeta, width=20, font=("Arial", 12), background="red")
		boton_modificar_pensionado.grid(row=0, column=0, padx=5, pady=5)

		
		# Crea un botón y lo empaqueta en la seccion_botones_consulta
		boton_modificar_pensionado = tk.Button(seccion_inferior,  text='Guardar Cambios', command = self.modificar_pensionado, width=20, font=("Arial", 12), background="red")
		boton_modificar_pensionado.grid(row=0, column=1, padx=5, pady=5)

		self.campo_numero_tarjeta.focus()

	def activar_desacivar_tarjeta(self):
		vigencia = self.variable_vigencia.get()
		if vigencia == 'None':vigencia = None

		if vigencia:
			self.variable_vigencia.set(None)
			mb.showinfo("Alerta", "Se ha desactivado la tarjeta, guarde cambios para confirmar cambio")
		else:
			vigencia = self.nueva_vigencia(vigencia)
			self.variable_vigencia.set(vigencia)
			mb.showinfo("Alerta", "Se ha activado la tarjeta, guarde cambios para confirmar cambio")
		



	def modificar_pensionado(self):
		try:
			variable_numero_tarjeta = self.variable_numero_tarjeta.get()
			variable_nombre = self.variable_nombre.get()
			variable_apellido_1 = self.variable_apellido_1.get()
			variable_apellido_2 = self.variable_apellido_2.get()

			variable_telefono_1 = self.variable_telefono_1.get()
			variable_telefono_2 = self.variable_telefono_2.get()
			variable_ciudad = self.variable_ciudad.get()
			variable_colonia = self.variable_colonia.get()
			variable_cp = self.variable_cp.get()
			variable_numero_calle = self.variable_numero_calle.get()

			variable_placas = self.variable_placas.get()
			variable_auto_modelo = self.variable_auto_modelo.get()
			variable_auto_color = self.variable_auto_color.get()

			variable_monto = self.variable_monto.get()
			variable_cortesia = self.variable_cortesia.get()
			variable_tolerancia = 5
			fecha_modificación_pensionado =  datetime.today().strftime("%Y-%m-%d %H:%M:%S")
			vigencia = self.variable_vigencia.get()
			if vigencia == "None":vigencia = None


			if len(variable_numero_tarjeta) == 0 or len(variable_nombre) == 0 or len(variable_apellido_1) == 0 or len(variable_apellido_2) == 0 or len(variable_telefono_1) == 0 or len(variable_telefono_2) == 0 or len(variable_ciudad) == 0 or len(variable_colonia) == 0 or len(variable_cp) == 0 or len(variable_numero_calle) == 0 or len(variable_placas) == 0 or len(variable_auto_modelo) == 0 or len(variable_auto_color) == 0 or len(variable_monto) == 0 or len(variable_cortesia) == 0 or len(str(variable_tolerancia)) == 0:raise IndexError("No dejar campos en blanco")

			if variable_cortesia == "No" and variable_monto == 0:raise IndexError("Ingrese el monto a pagar")
			if variable_cortesia == "Si":variable_monto = 0

			datos_pensionado = (variable_numero_tarjeta, variable_nombre, variable_apellido_1, variable_apellido_2, variable_telefono_1, variable_telefono_2, variable_ciudad, variable_colonia, variable_cp, variable_numero_calle, variable_placas, variable_auto_modelo, variable_auto_color, variable_monto, variable_cortesia, variable_tolerancia, fecha_modificación_pensionado, vigencia)

			self.query.actualizar_pensionado(datos_pensionado=datos_pensionado,Num_tarjeta = variable_numero_tarjeta)
			mb.showinfo("Información", "El pensionado fue modificado correctamente")
			self.desconectar()



		except IndexError as e:
			traceback.print_exc()
			mb.showerror("Error", e)
		except ValueError as e:
			traceback.print_exc()
			mb.showerror("Error", e)
		except Exception as e:
			traceback.print_exc()
			mb.showerror("Error", e)


	def desconectar(self):
		"""
		Cierra la ventana principal y detiene el hilo en el que se ejecuta.

		:param None: 

		:raises None: 

		:return:
			- None
		"""
		#detener el loop principal
		self.panel_crud.quit()
		# Destruye el panel principal
		self.panel_crud.destroy()

	def nueva_vigencia(self, fecha):
		"""
		Obtiene la fecha del último día del mes siguiente a la fecha dada y la devuelve como una cadena de texto en el formato '%Y-%m-%d %H:%M:%S'.

		:param fecha (str or datetime): Fecha a partir de la cual se obtendrá la fecha del último día del mes siguiente.

		:raises: TypeError si la fecha no es una cadena de texto ni un objeto datetime.

		:return:
			- nueva_vigencia (str): Una cadena de texto en el formato '%Y-%m-%d %H:%M:%S' que representa la fecha del último día del mes siguiente a la fecha dada.
		"""
		try:
			if fecha == None:
				# Obtener la fecha y hora actual en formato deseado
				fecha = datetime.today().strftime("%Y-%m-%d 23:59:59")

				# fecha = "2023-04-30 23:59:59"

				# Convertir la cadena de caracteres en un objeto datetime
				fecha = datetime.strptime(fecha, "%Y-%m-%d 23:59:59")

				fecha = fecha - relativedelta(months=1)

			# Verificar que la fecha sea de tipo str o datetime
			elif not isinstance(fecha, (str, datetime)):
				raise TypeError("La fecha debe ser una cadena de texto o un objeto datetime.")
			
			# Convertir la fecha dada en un objeto datetime si es de tipo str
			elif isinstance(fecha, str):
				fecha = datetime.strptime(fecha, '%Y-%m-%d 23:59:59')
			
			# Obtener la fecha del primer día del siguiente mes
			mes_siguiente = fecha + relativedelta(months=1, day=1)
			
			# Obtener la fecha del último día del mes siguiente
			ultimo_dia_mes_siguiente = mes_siguiente + relativedelta(day=31)
			if ultimo_dia_mes_siguiente.month != mes_siguiente.month:
				ultimo_dia_mes_siguiente -= relativedelta(days=1)
			
			# convertir la fecha del último día del mes siguiente en formato de cadena
			nueva_vigencia = ultimo_dia_mes_siguiente.strftime('%Y-%m-%d 23:59:59')

			# Devolver el valor
			return nueva_vigencia
		
		except TypeError as e:
			mb.showwarning("Error", f"{e}")
		except Exception as e:
			mb.showwarning("Error", f"{e}")

#View_modificar_pensionados()