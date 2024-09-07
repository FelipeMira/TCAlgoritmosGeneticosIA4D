from Produto import Produto


class GeracaoDeProdutos:
    @staticmethod
    def gerar_lista_produtos():
        lista_produto = [
            Produto("Smartphone Samsung", 0.00001, 2500.00),
            Produto("Tablet Apple", 0.00002, 3200.00),
            Produto("Smartwatch Garmin", 0.0005, 1500.00),
            Produto("Cafeteira Nespresso", 0.0002, 800.00),
            Produto("Máquina de Lavar LG", 0.510, 2200.00),
            Produto("Fogão Brastemp", 0.500, 1800.00),
            Produto("Aspirador de Pó Electrolux", 0.300, 600.00),
            Produto("Impressora HP", 0.150, 400.00),
            Produto("Monitor Samsung", 0.250, 1200.00),
            Produto("Geladeira Samsung", 0.700, 1500.00),
            Produto("Microondas Brastemp", 0.040, 300.00),
            Produto("Notebook HP", 0.003, 2500.00),
            Produto("Câmera Canon", 0.002, 1200.00),
            Produto("Fone de Ouvido Bose", 0.0001, 300.00),
            Produto("Teclado Mecânico", 0.001, 150.00),
            Produto("Mouse Logitech", 0.0005, 100.00),
            Produto("Roteador TP-Link", 0.0003, 200.00),
            Produto("Smart TV LG", 0.400, 3500.00),
            Produto("Console PlayStation", 0.300, 2500.00),
            Produto("Drone DJI", 0.002, 4000.00),
            Produto("Bicicleta Caloi", 0.900, 1200.00),
            Produto("Patinete Elétrico", 0.800, 2200.00),
            Produto("Cadeira Gamer", 0.600, 800.00),
            Produto("Projetor Epson", 0.200, 1500.00),
            Produto("Home Theater Sony", 0.100, 1000.00),
            Produto("Ar Condicionado LG", 0.500, 2000.00),
            Produto("Ventilador Arno", 0.050, 150.00),
            Produto("Purificador de Água", 0.100, 500.00)
                         ]
        return lista_produto
