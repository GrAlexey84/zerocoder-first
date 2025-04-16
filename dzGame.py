import pygame
import random
import time
import json

# Инициализация Pygame
pygame.init()

# Настройки окна
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Гонка с препятствиями")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
ROAD_GRAY = (70, 70, 70)  # Серый цвет дороги
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Настройки дороги
ROAD_WIDTH = 450
LANE_WIDTH = ROAD_WIDTH // 3
ROAD_LEFT = (SCREEN_WIDTH - ROAD_WIDTH) // 2

# Файл для сохранения рекорда
HIGH_SCORE_FILE = "highscore.json"


def load_high_score():
    try:
        with open(HIGH_SCORE_FILE, 'r') as f:
            data = json.load(f)
            return data.get('high_score', 0)
    except:
        return 0


def save_high_score(score):
    with open(HIGH_SCORE_FILE, 'w') as f:
        json.dump({'high_score': score}, f)


class Car:
    def __init__(self):
        self.width = 120
        self.height = 140
        self.x = ROAD_LEFT + LANE_WIDTH + (LANE_WIDTH - self.width) // 2
        self.target_x = self.x
        self.y = SCREEN_HEIGHT - self.height - 20
        self.speed = 8  # Скорость перемещения между полосами
        self.lane = 1  # 0 - левая, 1 - средняя, 2 - правая

        # Простое изображение машины
        self.image = None
        # Можно раскомментировать для загрузки изображения
        try:
            self.image = pygame.image.load("car.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        except:
            self.image = None

    def draw(self):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
            # Рисуем "фары"
            pygame.draw.rect(screen, YELLOW, (self.x + 10, self.y + 15, 15, 20))
            pygame.draw.rect(screen, YELLOW, (self.x + self.width - 25, self.y + 15, 15, 20))

    def move(self, direction):
        if direction == "left" and self.lane > 0:
            self.lane -= 1
            self.target_x = ROAD_LEFT + self.lane * LANE_WIDTH + (LANE_WIDTH - self.width) // 2
        elif direction == "right" and self.lane < 2:
            self.lane += 1
            self.target_x = ROAD_LEFT + self.lane * LANE_WIDTH + (LANE_WIDTH - self.width) // 2

    def update(self):
        # Плавное перемещение к целевой позиции
        if abs(self.x - self.target_x) > 1:
            self.x += (self.target_x - self.x) * 0.1
        else:
            self.x = self.target_x


class Hole:
    def __init__(self, speed):
        self.width = 100
        self.height = 100
        self.lane = random.randint(0, 2)
        self.x = ROAD_LEFT + self.lane * LANE_WIDTH + (LANE_WIDTH - self.width) // 2
        self.y = -self.height
        self.speed = speed

        # Простое изображение ямы
        self.image = None
        # Раскомментируйте для загрузки изображения ямы:
        try:
            self.image = pygame.image.load("hole.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        except:
            self.image = None

    def draw(self):
        if self.image:
            screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.ellipse(screen, BLACK, (self.x, self.y, self.width, self.height))
            # Рисуем трещины для ямы
            pygame.draw.line(screen, WHITE, (self.x + 20, self.y + 20), (self.x + 60, self.y + 60), 2)
            pygame.draw.line(screen, WHITE, (self.x + 60, self.y + 20), (self.x + 20, self.y + 60), 2)

    def update(self):
        self.y += self.speed
        return self.y > SCREEN_HEIGHT


class Game:
    def __init__(self):
        self.car = Car()
        self.holes = []
        self.score = 0
        self.high_score = load_high_score()
        self.last_hole_time = time.time()
        self.hole_interval = 1.5
        self.base_speed = 5
        self.game_over = False
        self.font = pygame.font.SysFont("Arial", 36)
        self.small_font = pygame.font.SysFont("Arial", 24)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.car.move("left")
                elif event.key == pygame.K_RIGHT:
                    self.car.move("right")
                elif event.key == pygame.K_r and self.game_over:
                    # Перезапуск игры
                    self.__init__()
                    self.start_time = time.time()

        return True

    def update(self):
        if self.game_over:
            return

        self.car.update()

        # Увеличиваем счет и сложность
        self.score = int(time.time() - self.start_time)
        current_speed = self.base_speed + self.score // 10  # Увеличиваем скорость каждые 10 секунд

        # Обновляем рекорд
        if self.score > self.high_score:
            self.high_score = self.score
            save_high_score(self.high_score)

        # Создаем новые ямы
        current_time = time.time()
        if current_time - self.last_hole_time > self.hole_interval:
            self.holes.append(Hole(current_speed))
            self.last_hole_time = current_time
            # Уменьшаем интервал между ямами каждые 15 секунд (но не менее 0.7)
            self.hole_interval = max(0.7, 1.5 - self.score // 15 * 0.1)

        # Обновляем ямы
        for hole in self.holes[:]:
            if hole.update():
                self.holes.remove(hole)

        # Проверка столкновений
        for hole in self.holes:
            if (self.car.x + self.car.width * 0.2 < hole.x + hole.width * 0.8 and
                    self.car.x + self.car.width * 0.8 > hole.x + hole.width * 0.2 and
                    self.car.y + self.car.height * 0.2 < hole.y + hole.height * 0.8 and
                    self.car.y + self.car.height * 0.8 > hole.y + hole.height * 0.2):
                self.game_over = True

    def draw(self):
        # Фон с эффектом движения
        screen.fill(GRAY)

        # Дорога (серого цвета)
        pygame.draw.rect(screen, ROAD_GRAY, (ROAD_LEFT, 0, ROAD_WIDTH, SCREEN_HEIGHT))

        # Дорожная разметка (пунктирные линии)
        for i in range(1, 3):
            for j in range(0, SCREEN_HEIGHT, 40):
                offset = (pygame.time.get_ticks() // 30) % 80  # Анимация движения
                pygame.draw.rect(screen, WHITE, (ROAD_LEFT + i * LANE_WIDTH - 5, j + offset, 10, 20))

        # Ямы
        for hole in self.holes:
            hole.draw()

        # Машина
        self.car.draw()

        # Счет и рекорд
        score_text = self.font.render(f"Очки: {self.score}", True, WHITE)
        high_score_text = self.font.render(f"Рекорд: {self.high_score}", True, YELLOW)
        level_text = self.small_font.render(f"Уровень: {self.score // 10 + 1}", True, WHITE)

        screen.blit(score_text, (20, 20))
        screen.blit(high_score_text, (20, 60))
        screen.blit(level_text, (20, 110))

        # Экран Game Over
        if self.game_over:
            overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 180))  # Полупрозрачный черный
            screen.blit(overlay, (0, 0))

            game_over_text = self.font.render(f"Игра окончена! Очки: {self.score}", True, WHITE)
            high_score_text = self.font.render(f"Рекорд: {self.high_score}", True, YELLOW)
            restart_text = self.small_font.render("Нажмите R для перезапуска", True, WHITE)

            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 80))
            screen.blit(high_score_text,
                        (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
            screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

        pygame.display.flip()

    def run(self):
        self.start_time = time.time()
        clock = pygame.time.Clock()
        running = True

        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)


if __name__ == "__main__":
    game = Game()
    game.run()
    pygame.quit()