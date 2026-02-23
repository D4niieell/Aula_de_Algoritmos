" S E N A C , / "
" 0 1 2 3 4 5 6 "

# CARACTERES
texto1 = "SENAC"
print(texto1[0])
print(texto1[3]) 
print(texto1[-1])

# FUNÇÃO len()
texto2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus semper risus tortor, quis gravida nibh venenatis a. Cras placerat dui id lectus venenatis consequat. Fusce iaculis enim vehicula tellus accumsan commodo at sit amet neque. Morbi facilisis quam eu felis ultrices, ut congue mauris pharetra. Donec cursus augue eros, quis volutpat sem consequat id. Suspendisse ex quam, molestie non enim vitae, vestibulum dapibus felis. Quisque sapien tortor, hendrerit sed neque non, porttitor dapibus erat."
print(len(texto2))

# FUNÇÃO MAIUSCULO E MINUSCULO
texto3 = "olá mundinho"
print(texto3.upper())

texto4 = "OLÁ MUNDÃO"
print(texto4.lower())
print(texto3.capitalize())

texto5 = "Python"
print(texto5[0:3])
print(texto5[0:4])

# REPLACE
texto6 = "Hoje é aula da Heloisa"
novo_texto = texto6.replace("da Heloisa", "do José Milton")
print(novo_texto)

# ESPAÇO EM BRANCO
texto7 = "   Olá mundo   "
print(texto7.strip() + "String") # remove direita e esquerda
print(texto7.lstrip() + "String") # remove esquerda
print(texto7.rstrip() + "String") # remove direita

# METODOS STRING
texto8 = "Pulei carnaval, mas hoje estou estudando."
print("carnaval" in texto8) 
# Case sensitive = Sensível a letras maiusculas e minisculas

print(texto8.find("estudando")) # 31
print(texto8[31]) # E
print(texto8.count("a"))

texto9 = "Eu amo Java"
print(texto9.startswith("Eu"))
print(texto9.endswith("va"))