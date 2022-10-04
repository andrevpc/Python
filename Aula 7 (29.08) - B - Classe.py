# =============================================================================
# # Exercício 1 - Criar classe de casa com Área, Rua, Cor e Nome (opcional)
# class Casa:
#     def __init__(self,area,rua,cor,nome = ""):
#         self._area = area
#         self._rua = rua
#         self._cor = cor
#         self._nome = nome
#     def __del__ (self):
#         pass
#     def descricao(self):
#         print(f"Área: {self._area}, Rua: {self._rua}, Casa: {self._cor}, Dono: {self._nome}")
#     
# casa_do_andre = Casa(295, "Rua Maranhão", "Azul", "André")
# casa_do_andre.descricao()
# # Área: 295, Rua: Rua Maranhão, Casa: Azul, Dono: André
# =============================================================================

# =============================================================================
# # Exercício 2 - Classe carro com um método estático
# class Carro:
#     def __init__(self,modelo,cor,proprietario = ""):
#         self._modelo = modelo
#         Carro._marca = "BMW"
#         self._cor = cor
#         self._proprietario = proprietario
#     def __del__ (self):
#         pass
#     
#     def detalhes(self):
#         print(f"Modelo: {self._modelo} Marca: {self._marca} Cor: {self._cor} Proprietario: {self._proprietario}")
#     
# carro_x5 = Carro("X5", "Preto", "André")
# carro_m4 = Carro("M4", "Vermelha")
# 
# carro_x5.detalhes()
# carro_m4.detalhes()
# 
# print(carro_x5._marca)
# Carro._marca = "Fiat"
# print(carro_x5._marca)
# # Modelo: X5 Marca: BMW Cor: Preto Proprietario: André
# # Modelo: M4 Marca: BMW Cor: Vermelha Proprietario: 
# # BMW
# # Fiat
# =============================================================================

# =============================================================================
# # Exercício 3 - Calculadora cientifica herdando da normal
# class Calculadora:
#     def __init__(self, n1, n2, resultado):
#         self._n1 = n1
#         self._n2 = n2
#         self._resultado = 0
#         
#     def getResult(self):
#         print(self._resultado)
#     
#     def soma(self):
#         self._resultado = self._n1 + self._n2
#         
#     def sub(self):
#         self._resultado = self._n1 - self._n2
#         
#     def mult(self):
#         self._resultado = self._n1 * self._n2
#         
#     def div(self):
#         self._resultado = self._n1 / self._n2
# 
#         
# class CalculadoraCientifica(Calculadora):
#     def __init__(self, n1, n2, n3, resultado):
#         super().__init__(n1, n2, resultado)   
#         self._n3 = n3
#     def formula(self):
#         self._resultado = (self._n1 * self._n1) + (self._n2 * self._n2)
#     def formula2(self):
#         self._resultado = self._n1 * self._n2 * self._n3
# 
# num1=int(input("Selecione o primeiro valor: "))
# num2=int(input("Selecione o segundo valor: "))
# num3=int(input("Selecione o terceiro valor: "))
# 
# calc = CalculadoraCientifica(num1, num2, num3, 0)
# calc.formula()
# calc.getResult()
# calc.soma()
# calc.getResult()
# calc.formula2()
# calc.getResult()
# =============================================================================
