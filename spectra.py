import matplotlib.pyplot as plt
import numpy as np

# Диапазоны видимого света (в нанометрах)
VISIBLE_RANGE = (380, 750)


# Функция для преобразования длины волны в цвет
def wavelength_to_rgb(wavelength):
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
def generate_spectrum(wavelengths, background="black"):
    fig, ax = plt.subplots(figsize=(10, 2))
    if background == "black":
        fig.patch.set_facecolor("black")
        ax.set_facecolor("black")
    else:
        fig.patch.set_facecolor("white")
        ax.set_facecolor("white")

    for wavelength in wavelengths:
        if VISIBLE_RANGE[0] <= wavelength <= VISIBLE_RANGE[1]:
            color = np.array(wavelength_to_rgb(wavelength)) / 255.0
        else:
            color = "gray"
        ax.axvline(x=wavelength, color=color, linewidth=2)

    ax.set_xlim(300, 800)
    ax.set_ylim(0, 1)
    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)

    plt.show()


# Пример использования
wavelengths = [370, 400, 450, 500, 550, 600, 650, 700, 750]
generate_spectrum(wavelengths)
