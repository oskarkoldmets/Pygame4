import pygame
import sys

# Funktsioon ruutude joonistamiseks
def joonista_ruudud(ekraan, ruudu_suurus, read, veerud, joone_varv):
    for rida in range(read):
        for veerg in range(veerud):
            ruudu_x = veerg * ruudu_suurus
            ruudu_y = rida * ruudu_suurus
            # Joonista ruut
            pygame.draw.rect(ekraan, joone_varv, (ruudu_x, ruudu_y, ruudu_suurus, ruudu_suurus), 1)

# Mängu initsialiseerimine
pygame.init()

# Ekraani seadistamine
ekraani_laius = 640
ekraani_korgus = 480
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus))
pygame.display.set_caption("Ruutude mäng")

# Värvid
valge = (255, 255, 255)  # Valge värv RGB kujul
heleroheline = (144, 238, 144)  # Heleroheline värv tausta jaoks
punane = (255, 0, 0)  # Punane värv joonte jaoks

# Mängutsükkel
def mangu_tsukkel(ruudu_suurus, read, veerud, joone_varv):
    ekraan.fill(heleroheline)  # Tausta värv
    joonista_ruudud(ekraan, ruudu_suurus, read, veerud, joone_varv)
    pygame.display.flip()  # Värskenda ekraani

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Sulge Pygame
                sys.exit()  # Sulge programm

# Mängu käivitamine
if __name__ == "__main__":
    ruudu_suurus = 20  # Ruudu suurus pikslites
    read = 24  # Ridade arv
    veerud = 32  # Veergude arv
    joone_varv = punane  # Joonte värv
    mangu_tsukkel(ruudu_suurus, read, veerud, joone_varv)  # Käivita mängutsükkel

