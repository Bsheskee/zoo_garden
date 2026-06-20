# explicit namespace marker- jawny znacznik przestrzeni nazw, bez tego nie działałby import z podkatalogów ale istniałoby ryzyko konfliktu nazw z innymi pakietami, 
# np. zewnętrznymi bibliotekami, które też mają katalog zoo, lub employee z lokalnego katalogu vs employee z katalogu zewnętrznego. Python nie wiedziałby, który katalog wybrać. 
# Nowoczesny Python (od wersji 3.3) przełącza się w tryb awaryjny i traktuje folder zoo jako Implicit Namespace Package (niejawną przestrzeń nazw). 
# W tym momencie dla Pythona słowo zoo przestaje być nazwą konkretnej paczki kodu. Staje się tylko luźną, wirtualną etykietą (folderem na dysku), 
# do której każdy z dowolnego miejsca na komputerze może coś wrzucić. 

# Ryzyko "Zatrucia" przestrzeni nazw (Namespace Pollution)
# To jest największe niebezpieczeństwo braku jawnego znacznika w dużych systemach.
# Gdybyś Ty, Stripe, albo jakakolwiek inna biblioteka pobrana z internetu, mieli w swoich strukturach folder o nazwie zoo 
# (co w przypadku systemów zarządzania czy aplikacji demonstracyjnych nie jest rzadkością) i żaden z tych folderów nie miałby pliku __init__.py, 
# Python połączyłby je w pamięci w jedną, gigantyczną, chaotyczną przestrzeń nazw.
# Dla Pythona przestałoby istnieć rozróżnienie na "moje lokalne pliki" i "obce pliki". 

# Gdyby Stripe miał w swojej paczce folder zoo/employees, Python pomyślałby, że pliki Stripe i Twoje pliki to jest dokładnie to samo miejsce.
# Podczas próby importu:
# from zoo.employees import Employee

# Python zacząłby przeszukiwać wszystkie foldery o nazwie zoo na Twoim komputerze i w bibliotekach. 
# Mógłby przypadkowo zaimportować klasę Employee ze Stripe zamiast Twojej, bo ścieżki w pamięci RAM nałożyłyby się na siebie!