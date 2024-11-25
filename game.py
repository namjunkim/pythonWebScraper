import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Shooting Game")

# 색상 및 속도
white = (255, 255, 255)
black = (0, 0, 0)
player_speed = 5
bullet_speed = 10
enemy_speed = 2

# 플레이어 설정
player = pygame.Rect(screen_width // 2, screen_height - 50, 50, 50)

# 총알 및 적 리스트
bullets = []
enemies = []

#점수
score = 0

#생존여부
alive = True

# 새로운 적 생성 시간
enemy_spawn_time = 2000  # 2초
last_enemy_spawn = pygame.time.get_ticks()

elapsed_time_seconds = 0

# 메인 루프
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0 and alive:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < screen_width and alive:
        player.x += player_speed
    if keys[pygame.K_UP] and player.right > 0 and alive:
        player.y -= player_speed
    if keys[pygame.K_DOWN] and player.right < screen_height and alive:
        player.y += player_speed
    if keys[pygame.K_SPACE] and alive:
        bullet = pygame.Rect(player.centerx - 5, player.top - 10, 3, 3)
        bullets.append(bullet)

    # 적 생성
    if pygame.time.get_ticks() - last_enemy_spawn > enemy_spawn_time:
        enemy_x = random.randint(0, screen_width - 50)
        enemy = pygame.Rect(enemy_x, 0, 50, 50)
        enemies.append(enemy)
        last_enemy_spawn = pygame.time.get_ticks()

    # 총알 이동
    for bullet in bullets[:]:
        bullet.y -= bullet_speed
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # 적 이동
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.top > screen_height:
            enemies.remove(enemy)

    # 충돌 체크
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score =  score + 10
                break

    # 적 충돌
    for enemy in enemies[:]:
        if enemy.colliderect(player):
            alive = False


    # 화면 그리기
    screen.fill(black)

    # 경과 시간 가져오기 (밀리초 단위)
    elapsed_time_ms = pygame.time.get_ticks()

    # 밀리초를 초로 변환

    if alive:
        elapsed_time_seconds = elapsed_time_ms / 1000.0

    font = pygame.font.Font(None, 23)
    text = font.render(f"Elapsed Time: {elapsed_time_seconds:.2f} sec", True, white)
    text_rect = text.get_rect(center=(screen_width - 90, screen_height - 580))
    screen.blit(text, text_rect)

    score_font = pygame.font.Font(None, 40)
    score_text = score_font.render(str(score), True, white)
    score_rect = score_text.get_rect(center=(screen_width - 750, screen_height - 580))
    screen.blit(score_text, score_rect)

    pygame.draw.rect(screen, white, player)
    for bullet in bullets:
        pygame.draw.rect(screen, white, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, white, enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()