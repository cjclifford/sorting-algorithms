import sys, pygame

class Visualizer:
  black = (0, 0, 0)
  white = (255, 255, 255)
  red = (255, 0, 0)
  dark_gray = (50, 50, 50)
  light_gray = (200, 200, 200)

  history = []

  def __init__(self, width, height, delay):
    self.window_size = self.width, self.height = width, height
    self.delay = delay

  def update(self, lst, item):
    self.history.append({'list': lst, 'item': item})

  def reset(self):
    self.history = []

  def replay(self):
    pygame.init()
    self.screen = pygame.display.set_mode(self.window_size)

    length = len(self.history[0]['list'])
    min_value = min(self.history[0]['list'])
    max_value = max(self.history[0]['list'])

    for event in self.history:
      self.screen.fill(self.white)
      col_width = self.width / length

      for i in range(length):
        height_interval = int(self.height / length)
        col_height = height_interval * event['list'][i]

        rect_col = pygame.Rect(i * col_width, self.height - col_height, col_width, col_height)
        rect_gap = pygame.Rect(i * col_width, self.height - col_height, col_width, col_height)
        rect_top = pygame.Rect(i * col_width, self.height - col_height, col_width, height_interval)

        if i is event['item']:
          pygame.draw.rect(self.screen, self.red, rect_col)
          # play sound
        else:
          pygame.draw.rect(self.screen, self.light_gray, rect_col)
        pygame.draw.rect(self.screen, self.black, rect_top)
        pygame.draw.rect(self.screen, self.white, rect_col, 1)

      pygame.display.flip()
      pygame.time.wait(self.delay)

    while 1:
      for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
          return