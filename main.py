import random
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class LifeWidget(Widget):
    def __init__(self, **kwargs):
        super(LifeWidget, self).__init__(**kwargs)
        # Размеры сетки игры – число столбцов и строк
        self.cols = 50
        self.rows = 50
        # Инициализируем поле случайными значениями (True – живая клетка, False – мёртвая)
        self.grid = [[random.choice([False, True]) for _ in range(self.cols)] for _ in range(self.rows)]
        self.running = False  # Флаг для режима работы симуляции
        # При изменении размеров или положения виджета запускаем перерисовку
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        """Перерисовка всех клеток на экране."""
        self.canvas.clear()
        cell_width = self.width / self.cols
        cell_height = self.height / self.rows
        with self.canvas:
            for i in range(self.rows):
                for j in range(self.cols):
                    # Живая клетка – зелёная, мёртвая – чёрная
                    if self.grid[i][j]:
                        Color(0, 1, 0)
                    else:
                        Color(0, 0, 0)
                    Rectangle(
                        pos=(self.x + j * cell_width, self.y + i * cell_height),
                        size=(cell_width, cell_height)
                    )

    def count_neighbors(self, i, j):
        """Подсчёт количества живых соседей для клетки (i, j)
        с обработкой краёв через wrap-around."""
        count = 0
        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue
                ni = (i + di) % self.rows
                nj = (j + dj) % self.cols
                if self.grid[ni][nj]:
                    count += 1
        return count

    def next_generation(self, dt):
        """Расчёт следующего поколения клеток по правилам Конвея."""
        if not self.running:
            return
        new_grid = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                neighbors = self.count_neighbors(i, j)
                if self.grid[i][j]:
                    # Живая клетка живёт при 2 или 3 соседях
                    new_grid[i][j] = neighbors in [2, 3]
                else:
                    # Мёртвая клетка оживает при ровно 3 соседях
                    new_grid[i][j] = (neighbors == 3)
        self.grid = new_grid
        self.update_canvas()

    def toggle_running(self):
        """Переключает режим симуляции – запуск/остановка."""
        self.running = not self.running
        if self.running:
            Clock.schedule_interval(self.next_generation, 0.2)
        else:
            Clock.unschedule(self.next_generation)

    def reset_game(self):
        """Сброс игры: остановка симуляции и создание нового случайного поля."""
        self.running = False
        Clock.unschedule(self.next_generation)
        self.grid = [[random.choice([False, True]) for _ in range(self.cols)] for _ in range(self.rows)]
        self.update_canvas()

class LifeGameApp(App):
    def build(self):
        # Основной layout с игровой областью и панелью кнопок
        layout = BoxLayout(orientation='vertical')
        self.life_widget = LifeWidget()
        button_layout = BoxLayout(size_hint=(1, 0.1))
        
        self.start_stop_btn = Button(text="Старт")
        self.start_stop_btn.bind(on_press=self.start_stop)
        
        reset_btn = Button(text="Начать сначала")
        reset_btn.bind(on_press=self.reset_game)
        
        button_layout.add_widget(self.start_stop_btn)
        button_layout.add_widget(reset_btn)
        
        layout.add_widget(self.life_widget)
        layout.add_widget(button_layout)
        
        return layout

    def start_stop(self, instance):
        """Обработчик кнопки Старт/Стоп."""
        self.life_widget.toggle_running()
        if self.life_widget.running:
            self.start_stop_btn.text = "Стоп"
        else:
            self.start_stop_btn.text = "Старт"

    def reset_game(self, instance):
        """Обработчик кнопки сброса игры."""
        self.start_stop_btn.text = "Старт"
        self.life_widget.reset_game()

if __name__ == '__main__':
    LifeGameApp().run()
