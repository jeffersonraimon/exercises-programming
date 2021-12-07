
pergunta = input('É mamífero? ')

if pergunta == 'sim':

    pergunta = input('é quadrúpede?: ')

    if pergunta == 'sim':

        pergunta = input('é carnívoro?; ')

        if pergunta == 'sim':

            print(('Leão'))

        else:

            print(('Cavalo'))

    else:
            pergunta = input('é bípede? ')

            if pergunta == 'sim':

                pergunta = input(('é onivoro? '))

                if pergunta == 'sim':

                    print('Homem')

                else:

                     print('macaco')
            else:

                pergunta = input('é voadores? ')

                if pergunta == 'sim':

                    print('Morcego')

                else:

                    print('Aquatico')

if pergunta == 'não':

    pergunta = input('São Aves? ')

    if pergunta == 'sim':

        pergunta = input('Não Voadoras?')

        if pergunta == 'sim':

            pergunta = input('tropical? ')

            if pergunta == 'sim':

                print('avestruz')

            else:

                print('Polar \n pinguim')
        else:

            pergunta = input('são nadadoras? ')

            if pergunta == 'sim':

                print('Pato')

            else:

                print('De rapina \nÁguia')

    else:
        print('São Repteis!')

        pergunta = input('Com casco?')

        if pergunta == 'sim':

            print('tartaruga')

        else:

            pergunta = input('São carnivoros? ')

            if pergunta == 'sim':

                print('Crocodilo')

            else:

                print('Sem pata \nCobra')
