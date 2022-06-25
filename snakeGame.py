from definitions import *

limparTela()
print(
    'Bem vindo ao Snake Game \nDigite seus dados a seguir: \n')

nome = input(
    'Digite seu nome: ')
email = input(
    'Digite seu e-mail: ')

pygame.init()
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption(
    'Snake da CC')

snake = [(200, 200), (210, 200), (220, 200)]
snakeSkin = pygame.Surface((10, 10))
snakeSkin.fill((255, 255, 255))

posicaoMaca = inicioAleatorio()
maca = pygame.Surface((10, 10))
maca.fill((255, 0, 0))

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direcao = UP
            elif event.key == pygame.K_RIGHT:
                direcao = RIGHT
            elif event.key == pygame.K_DOWN:
                direcao = DOWN
            elif event.key == pygame.K_LEFT:
                direcao = LEFT

    if colisao(snake[0], posicaoMaca):
        posicaoMaca = inicioAleatorio()
        snake.append((0, 0))
        pontos = pontos + 1

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if direcao == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    screen.fill((0, 0, 0))
    screen.blit(maca, posicaoMaca)

    fonte = pygame.font.Font(
        "freesansbold.ttf", 20)
    texto = fonte.render(
        f'Pontos: {pontos}', True, (255, 255, 255))
    screen.blit(texto, (30, 5))

    for posicao in snake:
        screen.blit(snakeSkin, posicao)

    pygame.display.update()

    dadosJogador = open('dados.txt', 'w')
    dadosJogador.write(
        f'Jogador: {nome} \nE-mail: {email} \nPontuação: {pontos}')
    dadosJogador.close()
