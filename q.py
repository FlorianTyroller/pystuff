def gibtWahrZurueckWennDieErsteZahlKleinerWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl):
    if (ErsteZahl < ZweiteZahl):
        return True
    if (ErsteZahl == ZweiteZahl):
        return False
    if (ErsteZahl > ZweiteZahl):
        return False

def gibtWahrZurueckWennDieErsteZahlGroesserWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl):
    if (gibtWahrZurueckWennDieErsteZahlKleinerWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return False
    if (ErsteZahl == ZweiteZahl):
        return False
    if (ErsteZahl > ZweiteZahl):
        return True
        
def gibtWahrZurueckWennDieErsteZahlGleichGrossWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl):
    if (gibtWahrZurueckWennDieErsteZahlKleinerWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return False
    if (ErsteZahl == ZweiteZahl):
        return True
    if (gibtWahrZurueckWennDieErsteZahlGroesserWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return False

def gibtWahrZurueckWennDieErsteZahlKleineroderGleichGrossWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl):
    if (gibtWahrZurueckWennDieErsteZahlKleinerWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return True
    if (gibtWahrZurueckWennDieErsteZahlGleichGrossWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return True
    if (gibtWahrZurueckWennDieErsteZahlGroesserWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return False
def gibtWahrZurueckWennDieErsteZahlGroesserroderGleichGrossWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl):
    if (gibtWahrZurueckWennDieErsteZahlKleinerWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return False
    if (gibtWahrZurueckWennDieErsteZahlGleichGrossWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return True
    if (gibtWahrZurueckWennDieErsteZahlGroesserWieDieZweiteZahlIst(ErsteZahl, ZweiteZahl)):
        return True

def derRestDerEntstehtKommaWennManZweiGanzzahlenDividiert(GanzzahlEins, GanzzahlZwei):
    while(gibtWahrZurueckWennDieErsteZahlGroesserroderGleichGrossWieDieZweiteZahlIst(GanzzahlEins, GanzzahlZwei)):
        GanzzahlEins = GanzzahlEins - GanzzahlZwei
    return int(GanzzahlEins)

def dieSummeDieEntstehtKommaWennManZweiZahlenAddiert(ZahlEins, ZahlZwei):
    for IndexOderAuchZaehlerGenannt in range(ZahlZwei):
        ZahlEins = ZahlEins + KONSTANTEMITDERSUMMEEINS
    return int(ZahlEins)

KONSTANTEMITDERSUMMEZWEI = int('00000010', 2)
KONSTANTEMITDERSUMMEEINS = int('00000001', KONSTANTEMITDERSUMMEZWEI)
KONSTANTEMITDERSUMMENEUN = int('00001001', KONSTANTEMITDERSUMMEZWEI)
KONSTANTEMITDERSUMMEZEHN = int('00001010', KONSTANTEMITDERSUMMEZWEI)

def quersummeEinerZahlRekursivBilden(ZahlvondermandieQUERSUMMEwissENWILL):
    if(gibtWahrZurueckWennDieErsteZahlKleineroderGleichGrossWieDieZweiteZahlIst(ZahlvondermandieQUERSUMMEwissENWILL, KONSTANTEMITDERSUMMENEUN)):
        return int(ZahlvondermandieQUERSUMMEwissENWILL)
    return dieSummeDieEntstehtKommaWennManZweiZahlenAddiert(derRestDerEntstehtKommaWennManZweiGanzzahlenDividiert(ZahlvondermandieQUERSUMMEwissENWILL, KONSTANTEMITDERSUMMEZEHN), quersummeEinerZahlRekursivBilden(int(ZahlvondermandieQUERSUMMEwissENWILL//KONSTANTEMITDERSUMMEZEHN)))

print(quersummeEinerZahlRekursivBilden(9999))