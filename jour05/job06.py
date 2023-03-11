def arrondir_notes(notes):
    notes_arrondies = []
    for note in notes:
        if note >= 40:
            multiple_de_5_sup = (note // 5 + 1) * 5
            if multiple_de_5_sup - note < 3:
                note_arrondie = multiple_de_5_sup
            else:
                note_arrondie = note
        else:
            note_arrondie = note
        notes_arrondies.append(note_arrondie)
    return notes_arrondies
notes = [65, 72, 83, 57, 39, 91]
notes_arrondies = arrondir_notes(notes)
print(notes_arrondies)
