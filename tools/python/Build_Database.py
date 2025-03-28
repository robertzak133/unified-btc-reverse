#
# Build_Database.py
#
# An enumeration of all the supported cameras and whether to build,
#    and where to find their pieces

# Multi-language Strings

g_btc_7e_strings = {'ENGLISH.SST': ["SHORT RANGE",    "EXTENDED SD POWER",   "TIME FORMAT",        "24-HOUR",    "12-HOUR" ,   "DATE FORMAT", \
                                    "MM/DD/YYYY", "DD/MM/YYYY", "YYYYMMDD", "YYYY/MM/DD",  "EXT TRIGGER",    "2 SECS", "ALL DAY/NIGHT",     "DAY THRESHOLD", "STANDARD", "LOW LIGHT", "ALWAYS COLOR", \
				    "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'ESPANOL.sst': ["ALCANCE CORTI",  "POTENCIA SD EXT.",    "FORMATO DE TIEMPO" , "24-HORA",    "12-HORA",    "FORMATO DE FECHA", \
                                    "MM/DD/AAAA", "DD/MM/AAAA", "AAAAMMDD", "AAAA/MM/DD", "EXT TRIGGER", "2 SEGS", "TODO EL DIA/NOCHE", "UMBRAL DE DIA", "ESTANDAR", "LUZ BAJA", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG" , "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'DEUTSCH.sst': ["KURZER BEREICH", "ERWEITERTE SD",       "ZEITFORMAT",         "24-STUDEN",  "12-STUDEN",  "DATUMSFORMAT", \
                                    "MM/TT/JJJJ", "TT/MM/JJJJ", "JJJJMMTT", "JJJJ/MM/TT", "EXT TRIGGER",    "2 SEK",  "GANZEN TAG/NACHT",  "TAGESSCHWELLE", "STANDARD", "GEDIMMTES LICHT", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM",  "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'DUTCH.sst':   ["KORT BEREIK",    "UITGEBREID SD",       "TIJD FORMAAT",       "24-UUR",     "12-UUR",     "DATUMNOTATIE", \
                                    "MM/DD/JJJJ", "DD/MM/JJJJ", "JJJJMMDD", "JJJJ/MM/DD", "EXT TRIGGER",    "2 SEC.", "HELE TAG/NACHT",    "DAGDREMPEL",    "STANDAARD", "WEINIG LICHT", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'FRANCIS.sst': ["COURTE PORTEE",  "SD ETENDUE",          "FORMAT de L'HEURE",  "24-HUERES",  "12-HUERES",  "FORMAT DE DATE", \
                                    "MM/JJ/AAAA", "JJ/MM/AAAA", "AAAAMMJJ", "AAAA/MM/JJ", "EXT TRIGGER","2 SECS", "JOURNEE/NUIT",      "SEUIL DE JOUR", "STANDARD","LUMIERE FAIBLE", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'ITALIANO.sst':["CORTO RAGGIO",   "POTENZA SD ESTESA",   "FORMATO ORARIO",     "24-ORE"   ,  "12-ORE",     "FORMATO DATA", \
                                    "MM/JJ/AAAA", "JJ/MM/AAAA", "AAAAMMJJ", "AAAA/MM/JJ", "EXT TRIGGER",    "2 SEC",  "GIORNO/NOTTE",      "SOGLIA DEL GIORNO", "STANDARD", "LUCE BASSA", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"],
                    'POLISH.sst':  ["KROTKI ZASIEG",  "ROZSZERZONA SD",      "FORMAT CZASU",       "24-GODZINY", "12-GODZINY", "FORMAT DATY", \
                                    "MM/DD/RRRR", "DD/MM/RRRR", "RRRRMMDD", "RRRR/MM/DD", "EXT_TRIGGER",  "2 SEK",  "CALY DZIEN/NOC",    "PROG DNIA",  "STANDARD", "SLABE OSWIETLENIE", "ALWAYS COLOR",
				     "TIMELAPSE FILE", ".TLS", ".JPG", ".MP4", "FACTORY", "CUSTOM", "SAVE CUSTOM", "NATIVE[2M]", "2MP", "DSLR", "FLASH"] }

g_btc_7a_strings = g_btc_7e_strings

g_btc_8e_strings = g_btc_7e_strings 

g_btc_7e_hp4_strings = g_btc_7e_strings

g_btc_8e_hp4_strings = g_btc_7e_hp4_strings 


g_btc_7e_hp5_strings = g_btc_7e_strings

g_btc_8e_hp5_strings = g_btc_7e_hp5_strings 

## YYMMDD{D = Development; A = Alpha; B = Beta; R = Release}
g_btc_major_version = "250321R"

g_wbwl_btc_targets = {}
# BTC-6CDLN
g_wbwl_btc_targets['BTC-6DCLN'] = {}
g_wbwl_btc_targets['BTC-6DCLN'] ['Target Directory'] = 'btc-6dcln'
g_wbwl_btc_targets['BTC-6DCLN'] ['Model'] = 'BTC-6DCLN'
g_wbwl_btc_targets['BTC-6DCLN'] ['LA File'] = '2024-09-07_BTC-6DCLN-boot-to-menu'
g_wbwl_btc_targets['BTC-6DCLN'] ['EEPROM Dir'] = '2024-09-04-factory-baseline'
g_wbwl_btc_targets['BTC-6DCLN'] ['EEPROM Filename'] = 'factory-baseline-BTC6DCLN'
g_wbwl_btc_targets['BTC-6DCLN'] ['EEPROM PCB Locator'] = 'U9'
g_wbwl_btc_targets['BTC-6DCLN'] ['Factory BRN Dir'] = '2024-09-04-Baseline'
g_wbwl_btc_targets['BTC-6DCLN'] ['Factory BRN Filename'] = 'BTC6DCLN.BRN'
g_wbwl_btc_targets['BTC-6DCLN'] ['Carve'] = False
g_wbwl_btc_targets['BTC-6DCLN'] ['Build'] = False

# PATRIOT-FHD
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] = {}
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Target Directory'] = 'btc-patriot-fhd'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Model'] = 'Patriot FHD'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['LA File'] = '2024-01-19-Patriot-EEPROM-Boot'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['EEPROM Dir'] = '2023-12-27-factory-baseline'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['EEPROM Filename'] = 'factory-baseline-BTC6PBM.bin'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['EEPROM PCB Locator'] = 'U9'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Factory BRN Dir'] = '2021-11-04-Baseline'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Factory BRN Filename'] = 'BTC6PBM.BRN'
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Carve'] = True
g_wbwl_btc_targets['BTC-PATRIOT-FHD'] ['Build'] = False

# 7A
g_wbwl_btc_targets['BTC-7A'] = {}
g_wbwl_btc_targets['BTC-7A'] ['Target Directory'] = 'btc-7a'
g_wbwl_btc_targets['BTC-7A'] ['Model'] = 'Recon Force Advantage'
g_wbwl_btc_targets['BTC-7A'] ['Strings'] = g_btc_7a_strings
g_wbwl_btc_targets['BTC-7A'] ['EEPROM Dir'] = 'factory-baseline-I04030C'
g_wbwl_btc_targets['BTC-7A'] ['EEPROM Filename'] = 'manufacturer-baseline-BTC-7A_I04030C.bin'
g_wbwl_btc_targets['BTC-7A'] ['EEPROM PCB Locator'] = 'U12'
g_wbwl_btc_targets['BTC-7A'] ['Factory BRN Dir'] = 'BTC7E_2021_10_07'
g_wbwl_btc_targets['BTC-7A'] ['Factory BRN Filename'] = 'brnbtc70.BRN'
g_wbwl_btc_targets['BTC-7A'] ['Version'] = 'WWL7A_' + g_btc_major_version
g_wbwl_btc_targets['BTC-7A'] ['Carve'] = True
g_wbwl_btc_targets['BTC-7A'] ['Build'] = True
# 8A
g_wbwl_btc_targets['BTC-8A'] = {}
g_wbwl_btc_targets['BTC-8A'] ['Target Directory'] = 'btc-8a'
g_wbwl_btc_targets['BTC-8A'] ['Model'] = 'Spec Ops Advantage'
g_wbwl_btc_targets['BTC-8A'] ['EEPROM Dir'] = 'factory-baseline'
g_wbwl_btc_targets['BTC-8A'] ['EEPROM Filename'] = 'Baseline-BTC-8A-EEPROM-Image.bin'
g_wbwl_btc_targets['BTC-8A'] ['EEPROM PCB Locator'] = 'U12'
g_wbwl_btc_targets['BTC-8A'] ['Factory BRN Dir'] = 'BTC-8A-Baseline'
g_wbwl_btc_targets['BTC-8A'] ['Factory BRN Filename'] = 'brnbtc80.BRN'
g_wbwl_btc_targets['BTC-8A'] ['Carve'] = True
g_wbwl_btc_targets['BTC-8A'] ['Build'] = True
# 7E
g_wbwl_btc_targets['BTC-7E'] = {}
g_wbwl_btc_targets['BTC-7E'] ['Target Directory'] = 'btc-7e'
g_wbwl_btc_targets['BTC-7E'] ['Model'] = 'Recon Force Edge'
g_wbwl_btc_targets['BTC-7E'] ['Strings'] = g_btc_7e_strings
g_wbwl_btc_targets['BTC-7E'] ['LA File'] = '2023-08-13-BTC-8E-ref-eeprom'
g_wbwl_btc_targets['BTC-7E'] ['EEPROM Dir'] = '2023-08-13-Synthesized-Baseline'
g_wbwl_btc_targets['BTC-7E'] ['EEPROM Filename'] = '2023-08-13-BTC-7E-EEPROM-Image.bin'
g_wbwl_btc_targets['BTC-7E'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-7E'] ['Factory BRN Dir'] = 'BTC7E_2021_10_07'
g_wbwl_btc_targets['BTC-7E'] ['Factory BRN Filename'] = 'brnbtc70.BRN'
g_wbwl_btc_targets['BTC-7E'] ['Version'] = 'WWL7E_' + g_btc_major_version
g_wbwl_btc_targets['BTC-7E'] ['Carve'] = True
g_wbwl_btc_targets['BTC-7E'] ['Build'] = True
# 8E
g_wbwl_btc_targets['BTC-8E'] = {}
g_wbwl_btc_targets['BTC-8E'] ['Target Directory'] = 'btc-8e'
g_wbwl_btc_targets['BTC-8E'] ['Model'] = 'Spec Ops Edge'
g_wbwl_btc_targets['BTC-8E'] ['Strings'] = g_btc_8e_strings
g_wbwl_btc_targets['BTC-8E'] ['EEPROM Dir'] = '2023-01-03-Factory-Baseline'
g_wbwl_btc_targets['BTC-8E'] ['EEPROM Filename'] = '2021-10-07-Factory-Image-Derived.bin'
g_wbwl_btc_targets['BTC-8E'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-8E'] ['Factory BRN Dir'] = 'BTC8E_2021_10_07'
g_wbwl_btc_targets['BTC-8E'] ['Factory BRN Filename'] = 'brnbtc80.BRN'
g_wbwl_btc_targets['BTC-8E'] ['Version'] = 'WWL8E_' + g_btc_major_version
g_wbwl_btc_targets['BTC-8E'] ['Carve'] = True
g_wbwl_btc_targets['BTC-8E'] ['Build'] = True
# 7E-HP4
g_wbwl_btc_targets['BTC-7E-HP4'] = {}
g_wbwl_btc_targets['BTC-7E-HP4'] ['Target Directory'] = 'btc-7e-hp4'
g_wbwl_btc_targets['BTC-7E-HP4'] ['Model'] = 'Recon Force Elite HP4'
g_wbwl_btc_targets['BTC-7E-HP4'] ['Strings'] = g_btc_7e_hp4_strings
#g_wbwl_btc_targets['BTC-7E-HP4'] ['LA File'] = '2023-03-01-BTC-7E-HP4-200ms'
g_wbwl_btc_targets['BTC-7E-HP4'] ['LA File'] = '2023-03-02-BTC-7E-HP4-180_240ms'
g_wbwl_btc_targets['BTC-7E-HP4'] ['EEPROM Dir'] = '2023-03-01-Synthesized-Factory-Baseline'
g_wbwl_btc_targets['BTC-7E-HP4'] ['EEPROM Filename'] = '2023-03-01-BTC-7E-HP4-EEPROM-Image.bin'
g_wbwl_btc_targets['BTC-7E-HP4'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-7E-HP4'] ['Factory BRN Dir'] = '2023-02-01-ns'
g_wbwl_btc_targets['BTC-7E-HP4'] ['Factory BRN Filename'] = 'brnbtc71.BRN'
g_wbwl_btc_targets['BTC-7E-HP4'] ['Version'] = 'WWL7EH4_' + g_btc_major_version
g_wbwl_btc_targets['BTC-7E-HP4'] ['Carve'] = True
g_wbwl_btc_targets['BTC-7E-HP4'] ['Build'] = True
# 8E-HP4
g_wbwl_btc_targets['BTC-8E-HP4'] = {}
g_wbwl_btc_targets['BTC-8E-HP4'] ['Target Directory'] = 'btc-8e-hp4'
g_wbwl_btc_targets['BTC-8E-HP4'] ['Model'] = 'Spec Ops Elite HP4'
g_wbwl_btc_targets['BTC-8E-HP4'] ['Strings'] = g_btc_8e_hp4_strings
g_wbwl_btc_targets['BTC-8E-HP4'] ['LA File'] = '2023-02-28-BTC-8E-HP4-70ms'
g_wbwl_btc_targets['BTC-8E-HP4'] ['EEPROM Dir'] = '2023-03-01-Synthesized-Factory-Baseline'
g_wbwl_btc_targets['BTC-8E-HP4'] ['EEPROM Filename'] = '2023-03-01-BTC-8E-HP4-EEPROM-Image.bin'
g_wbwl_btc_targets['BTC-8E-HP4'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-8E-HP4'] ['Factory BRN Dir'] = '2023-02-01-ns'
g_wbwl_btc_targets['BTC-8E-HP4'] ['Factory BRN Filename'] = 'brnbtc81.BRN'
g_wbwl_btc_targets['BTC-8E-HP4'] ['Version'] = 'WWL8EH4_' + g_btc_major_version
g_wbwl_btc_targets['BTC-8E-HP4'] ['Carve'] = True
g_wbwl_btc_targets['BTC-8E-HP4'] ['Build'] = True
# 7E-HP5
g_wbwl_btc_targets['BTC-7E-HP5'] = {}
g_wbwl_btc_targets['BTC-7E-HP5'] ['Target Directory'] = 'btc-7e-hp5'
g_wbwl_btc_targets['BTC-7E-HP5'] ['Model'] = 'Recon Force Elite HP5'
g_wbwl_btc_targets['BTC-7E-HP5'] ['Strings'] = g_btc_7e_hp5_strings
g_wbwl_btc_targets['BTC-7E-HP5'] ['EEPROM Dir'] = '2022-10-14-Factory-Firmware-Image'
g_wbwl_btc_targets['BTC-7E-HP5'] ['EEPROM Filename'] = '2022-10-17-BTC-7E-Factory-Firmware.bin'
g_wbwl_btc_targets['BTC-7E-HP5'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-7E-HP5'] ['Factory BRN Dir'] = 'BTC7EH5_M06170F'
g_wbwl_btc_targets['BTC-7E-HP5'] ['Factory BRN Filename'] = 'brnbtc72.BRN'
g_wbwl_btc_targets['BTC-7E-HP5'] ['Version'] = 'WWL7EH5_' + g_btc_major_version
g_wbwl_btc_targets['BTC-7E-HP5'] ['Version'] = 'WWL7EH5_' + g_btc_major_version
g_wbwl_btc_targets['BTC-7E-HP5'] ['Carve'] = True
g_wbwl_btc_targets['BTC-7E-HP5'] ['Build'] = True
# 8E-HP5
g_wbwl_btc_targets['BTC-8E-HP5'] = {}
g_wbwl_btc_targets['BTC-8E-HP5'] ['Target Directory'] = 'btc-8e-hp5'
g_wbwl_btc_targets['BTC-8E-HP5'] ['Model'] = 'Spec Ops Elite HP5'
g_wbwl_btc_targets['BTC-8E-HP5'] ['Strings'] = g_btc_8e_hp5_strings
g_wbwl_btc_targets['BTC-8E-HP5'] ['EEPROM Dir'] = '2022-09-04-Factory-Baseline'
g_wbwl_btc_targets['BTC-8E-HP5'] ['EEPROM Filename'] = '2020-09-04-Post-L10200F.bin'
g_wbwl_btc_targets['BTC-8E-HP5'] ['EEPROM PCB Locator'] = 'U6'
g_wbwl_btc_targets['BTC-8E-HP5'] ['Factory BRN Dir'] = 'BTC8EH5_M06170F'
g_wbwl_btc_targets['BTC-8E-HP5'] ['Factory BRN Filename'] = 'brnbtc82.BRN'
g_wbwl_btc_targets['BTC-8E-HP5'] ['Version'] = 'WWL8EH5_' + g_btc_major_version
g_wbwl_btc_targets['BTC-8E-HP5'] ['Carve'] = True
g_wbwl_btc_targets['BTC-8E-HP5'] ['Build'] = True
