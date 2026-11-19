#!/usr/bin/env python3
"""Генерация иконок PWA (192/512 px): фиолетовый фон, белый принтер с листом бумаги."""
from pathlib import Path
from PIL import Image, ImageDraw

BG = (124, 58, 237, 255)      # #7c3aed
SHADOW = (46, 16, 101, 90)    # мягкая тень под принтером
SHADOW2 = (46, 16, 101, 50)
WHITE = (255, 255, 255, 255)
GREY = (124, 108, 180, 255)   # строки текста на листе


def draw_icon(size: int) -> Image.Image:
    img = Image.new('RGBA', (size, size), BG)
    d = ImageDraw.Draw(img)
    s = size / 512  # масштаб от базового 512

    def R(x, y, w, h, r, **kw):
        d.rounded_rectangle([x * s, y * s, (x + w) * s, (y + h) * s], radius=r * s, **kw)

    # тень принтера
    R(96, 196, 320, 200, 34, fill=SHADOW)

    # верхняя крышка (задняя часть корпуса)
    R(136, 128, 240, 84, 20, fill=(237, 233, 254, 255))

    # лист бумаги выходит из слота подачи, из-под крышки
    R(172, 186, 168, 210, 10, fill=WHITE)
    for i, w in enumerate((112, 128, 88)):
        y = 216 + i * 42
        d.rounded_rectangle([196 * s, y * s, (196 + w) * s, (y + 18) * s], radius=9 * s, fill=GREY)

    # передний корпус со слотом
    R(96, 232, 320, 148, 34, fill=WHITE)
    # слот подачи
    R(160, 246, 192, 16, 8, fill=(124, 58, 237, 255))
    # кнопка/индикатор
    d.ellipse([344 * s, 266 * s, 376 * s, 298 * s], fill=SHADOW2 if False else (124, 58, 237, 255))
    d.ellipse([352 * s, 274 * s, 368 * s, 290 * s], fill=(196, 181, 253, 255))
    # лоток приёмника внизу корпуса
    R(140, 316, 232, 22, 10, fill=(237, 233, 254, 255))

    return img


def main():
    out = Path(__file__).resolve().parent.parent / 'assets'
    out.mkdir(exist_ok=True)
    for size in (192, 512):
        img = draw_icon(size)
        assert img.size == (size, size) and img.mode == 'RGBA'
        img.save(out / f'icon-{size}.png', optimize=True)
        print(f'assets/icon-{size}.png {size}x{size}')


if __name__ == '__main__':
    main()
