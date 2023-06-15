class Carrera:
    __codigo = 0
    __nombreC = ''
    __fechaInicio = ''
    __duracion = 0
    __titulo = ''

    def __init__(self, codigo, nombreC, fechaInicio, duracion, titulo):
        self.__codigo = codigo
        self.__nombreC = nombreC
        self.__fechaInicio = fechaInicio
        self.__duracion = duracion
        self.__titulo

    def __str__(self):
        return "%s %s %s %s %s %s" %(self.__codigo, self.__nombreC, self.__fechaInicio, self.__duracion, self.__titulo)
