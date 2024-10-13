import matplotlib.pyplot as plt
import numpy as np

# Диапазоны видимого света (в нанометрах)
VISIBLE_RANGE = (380, 750)


# Функция для преобразования длины волны в цвет
def wavelength_to_rgb(wavelength: int) -> tuple[int]:
    """
    Преобразует длину волны света (в нанометрах) в RGB цвет.

    Данная функция принимает длину волны в диапазоне от 380 до 750 нм
    и возвращает кортеж (R, G, B), представляющий соответствующий цвет в модели RGB.

    Аргументы:
    wavelength (float): Длина волны света в нанометрах. Ожидается значение в диапазоне от 380 до 750 нм.

    Возвращает:
    tuple: Кортеж (R, G, B), где R, G и B — целые числа в диапазоне от 0 до 255,
           представляющие интенсивности красного, зелёного и синего каналов соответственно.

    Пример:
    >>> wavelength_to_rgb(500)
    (0, 255, 126)  # Примерное значение для зелёного цвета

    Примечание:
    Значения длины волны вне диапазона от 380 до 750 нм не обрабатываются и могут вернуть некорректные результаты.
    """

    gamma = 0.8
    intensity_max = 255
    factor = 0.0
    R = G = B = 0

    if 380 <= wavelength <= 440:
        R = -(wavelength - 440) / (440 - 380)
        G = 0.0
        B = 1.0
    elif 440 <= wavelength <= 490:
        R = 0.0
        G = (wavelength - 440) / (490 - 440)
        B = 1.0
    elif 490 <= wavelength <= 510:
        R = 0.0
        G = 1.0
        B = -(wavelength - 510) / (510 - 490)
    elif 510 <= wavelength <= 580:
        R = (wavelength - 510) / (580 - 510)
        G = 1.0
        B = 0.0
    elif 580 <= wavelength <= 645:
        R = 1.0
        G = -(wavelength - 645) / (645 - 580)
        B = 0.0
    elif 645 <= wavelength <= 750:
        R = 1.0
        G = 0.0
        B = 0.0

    if 380 <= wavelength <= 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif 420 <= wavelength <= 645:
        factor = 1.0
    elif 645 <= wavelength <= 750:
        factor = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)

    R = round(intensity_max * (R * factor) ** gamma)
    G = round(intensity_max * (G * factor) ** gamma)
    B = round(intensity_max * (B * factor) ** gamma)

    return (R, G, B)


# Функция для генерации спектра
def generate_spectrum(wavelengths, background="white") -> None:
    """
    Генерирует спектр видимого света для заданных длин волн.

    Данная функция создает график с вертикальными линиями, представляющими
    длины волн в видимом спектре (или за его пределами). Цвет линий соответствует
    длинам волн. Фоновый цвет и текст могут быть изменены между белым и черным.

    Аргументы:
    wavelengths (list of floats): Список длин волн (в нанометрах), для которых нужно отобразить линии.
                                  Рекомендуется использовать диапазон от 380 до 750 нм для видимого света.
    background (str, optional): Фоновый цвет графика. Допустимые значения:
                                - "white" (по умолчанию): белый фон с черным текстом.
                                - "black": черный фон с белым текстом.

    Возвращает:
    None: Функция выводит график спектра и не возвращает значений.

    Примечания:
    - Если длина волны находится вне диапазона видимого спектра (380-750 нм), линия будет окрашена в серый цвет.
    - Функция автоматически настраивает отображение осей для удобного визуального восприятия.

    Пример:
    >>> generate_spectrum([400, 500, 600, 700], background="black")
    # Отобразит спектр с указанными длинами волн на черном фоне.

    """

    fig, ax = plt.subplots(figsize=(10, 2))
    if background == "black":
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")
        text_color = "white"
    else:
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")
        text_color = "black"

    for wavelength in wavelengths:
        if VISIBLE_RANGE[0] <= wavelength <= VISIBLE_RANGE[1]:
            color = np.array(wavelength_to_rgb(wavelength)) / 255.0
        else:
            color = "gray"
        ax.axvline(x=wavelength, color=color, linewidth=2)
        ax.text(
            wavelength,
            -0.25,
            f"{wavelength:.1f} nm",
            rotation=0,
            verticalalignment="top",
            horizontalalignment="center",
            color=text_color,
            fontsize=8,
        )

    ax.set_xlim(300, 800)
    ax.set_ylim(-0.2, 1)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    plt.show()


spectral_lines = {
    "Hydrogen": [656.3, 486.1, 434.0, 410.2],
    "Helium": [447.1, 501.6, 587.6, 667.8],
    "Sodium": [589.0, 589.6],
    "Mercury": [404.7, 435.8, 546.1, 576.9],
    "Neon": [585.2, 640.2, 659.9, 703.2],
    "Argon": [696.5, 706.7, 738.4, 763.5, 810.4],
    "Krypton": [427.4, 431.9, 436.3, 557.0, 587.1],
    "Xenon": [823.2, 828.0, 834.7, 881.9, 904.5],
    "Oxygen": [558.0, 630.0, 636.4],
    "Nitrogen": [575.5, 648.2, 742.3],
    "Calcium": [422.7, 443.5, 458.1, 527.0, 558.9],
    "Iron": [438.3, 441.5, 443.1, 445.2, 450.0],
}


generate_spectrum(spectral_lines.get("Oxygen"))

generate_spectrum(spectral_lines.get("Argon"))
