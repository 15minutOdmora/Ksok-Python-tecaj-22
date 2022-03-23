
# Nizi in print

print("Pozdravljeni!")  # Izpišemo niz

ime = input("Vaše ime: ")  # Povprašamo po imenu, vnos shranimo v spremenljivko ime
priimek = input("Vaš priimek: ")  # Povprašamo po priimku

ime_priimek = ime + " " + priimek + "."  # Združimo v en niz, vmes presledek nakoncu "pika"

ime_priimek = f"{ime} {priimek}."  # Enako kot zgornji stavek le da uporabimo formatiranje

print("Lepo vas je spoznati ", ime_priimek)  # Izpišemo dva niza hkrati!

# Števila

# Povprašamo po letnici rojstva
letnica_rojstva = input("Letnica rojstva: ")  # To je niz in ne število!

letnica_rojstva_st = int(letnica_rojstva)  # Pretvorimo v število, shranimo v drugi spremenljivki

starost_v_letih = 2022 - letnica_rojstva_st  # Izračunamo starost (približno, brez upoštevanja mesecev)

print(f"Super stari ste {starost_v_letih} ", end=":)")  # Izpišemo in na konec dodamo smejkota
