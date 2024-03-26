
# personagens
define p = Character("Pisquinha")
define h = Character("Husky")
define k = Character("Kai")


# o Jogo começa aqui

label start:

    scene noite
    with fade

    play sound "audio_narra1.mp3"

    "Dois irmãos Pisquinha e Husk lutam pela liberdade do clã dos lobos"

    show pisquinha at left
    with dissolve

    p "Não quero brigar com você irmão"

    p "Esta luta não faz sentido pra mim"

    hide pisquinha

    show husky at right
    with dissolve

    h "Deixa de conversa mole Pisquinha"

    h "Isto pra mim tem outro nome"

    h "Covardia!"  

    hide husky

    "Pisquinha deve enfrentar o irmão Husk?"

menu:

    "Sim":
        jump game

    "Não":
        jump book

label game:

    show pisquinha at right
    with dissolve

    p "Se não outra escolha, eu estou pronto irmão"

    hide pisquinha

    show husky at right
    with dissolve

    h "Farei o que deve ser feito"

    hide husky

    jump marry

label book:

    show husky at right
    with dissolve

    h "Você não tem escolha, lembre-se a força vem do seu interior"

    hide husky

    show pisquinha at left
    with dissolve

    p "Eu não queria, mas é o unico jeito"
    
    hide pisquinha

    jump marry

label marry:

    "Os irmão batalham"  

    return