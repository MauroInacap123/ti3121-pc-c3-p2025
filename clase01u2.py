class Participante:
    def __intit__(self, rut: str, nombre: str, edad: int):
        self._rut: str = rut 
        self._nombre: str = nombre
        self._edad: int = edad

        def presentarse(self) -> str:
            return f"Hola mi nombre es {self._nombre} y mi edad es {self.edad}"
        
        Participante1 : Participante = Participante("21981220-5", "Mauricio Bustamante", 19)
        print(Participante1)