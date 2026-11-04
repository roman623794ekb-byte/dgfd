from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.carousel import Carousel
# ПРАВИЛЬНЫЙ ИМПОРТ: AsyncImage импортируется из kivy.uix.image
from kivy.uix.image import AsyncImage


class AnimalCarouselApp(App):

    def build(self):
        # Главный контейнер (кнопки по бокам, карусель по центру)
        main_layout = BoxLayout(orientation="horizontal")

        # 1. Кнопка "Назад" (слева)
        btn_left = Button(
            text="◀",
            font_size="28sp",
            size_hint_x=0.1,
            background_color=(0.2, 0.2, 0.2, 0.8),
        )
        btn_left.bind(on_press=self.move_left)
        main_layout.add_widget(btn_left)

        # 2. Создаем саму карусель
        self.carousel = Carousel(direction="right", size_hint_x=0.8)

        # Прямые ссылки на изображения домашних животных
        animal_images = [
            "https://unsplash.com",  # Кот
            "https://unsplash.com",  # Пес
            "https://unsplash.com",  # Кролик
            "https://unsplash.com",  # Хомяк
        ]

        # Заполняем карусель картинками животных
        for url in animal_images:
            # Виджет AsyncImage автоматически скачает картинку при запуске
            slide = AsyncImage(source=url, allow_stretch=True, keep_ratio=True)
            self.carousel.add_widget(slide)

        main_layout.add_widget(self.carousel)

        # 3. Кнопка "Вперед" (справа)
        btn_right = Button(
            text="▶",
            font_size="28sp",
            size_hint_x=0.1,
            background_color=(0.2, 0.2, 0.2, 0.8),
        )
        btn_right.bind(on_press=self.move_right)
        main_layout.add_widget(btn_right)

        return main_layout

    def move_left(self, instance):
        """Прокрутка влево"""
        if self.carousel.index > 0:
            self.carousel.load_previous()
        else:
            self.carousel.load_slide(self.carousel.slides[-1])

    def move_right(self, instance):
        """Прокрутка вправо"""
        if self.carousel.index < len(self.carousel.slides) - 1:
            self.carousel.load_next()
        else:
            self.carousel.load_slide(self.carousel.slides[0])


if __name__ == "__main__":
    AnimalCarouselApp().run()
