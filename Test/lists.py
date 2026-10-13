namn = "Lelle är bäst"

# for idx in namn:
    # print(idx)

def maskera_ord(ord):
    maskat_ord = ""
    for bokstav in namn:
        # print(bokstav, end="")
        if bokstav ==" ":
            maskat_ord = maskat_ord + " "
            # print(" ", end="")
        elif bokstav=="ä":
            maskat_ord = maskat_ord + bokstav
            # print(f"{bokstav} ", end="")
        else:
            maskat_ord = maskat_ord + "_"
            # print("_ ", end="")
    return maskat_ord

print(namn)
hemliga_ordet = maskera_ord(namn)
print(hemliga_ordet)