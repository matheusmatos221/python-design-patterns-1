from impostos import calcula_ISS, calcula_ICMS


class CalculadorDeImpostos(object):
    def realiza_calculo(self, orcamento, imposto):

        if imposto == 'ISS':
            imposto_calculado = calcula_ISS(orcamento)
        elif imposto == 'ICMS':
            imposto_calculado = calcula_ICMS(orcamento)

        print(imposto_calculado)



if __name__ == '__main__':
    print('\n' * 2)
    print('************************************')
    print('Executando calculador_de_impostos.py')
    print('************************************')
    print('\n')

    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, 'ISS')
    calculador.realiza_calculo(orcamento, 'ICMS')
