import os
from datetime import datetime

class BTC_Doc_Maker:
    ''' A class for printing some documentation for firmware images
    '''
    firmware_table_filename = "firmware_table.md"
    eeprom_image_filename = "eeprom_table.md"

    def fprint_eeprom_banner(self, file):
        print(f'| Camera Model | PCB Locator  | EEPROM Image |', file=file)
        print(f'|--------------|--------------|--------------|', file=file)
        return

    def fprint_camera_eeprom_line(self, file, camera_model, pcb_locator, eeprom_image):
        print(f'| {camera_model} | {pcb_locator} | {eeprom_image} |', file=file)
        return

    def fprint_camera_line(self, file, camera_model, factory_baseline, current_wbwl, version, build_date):
        print(f'| {camera_model} | {factory_baseline} | {current_wbwl} | {version} | {build_date} |', file=file)
        return


    def fprint_banner(self, file):
        print(f'| Camera Model | Factory Baseline  | Current WBWL | Version  | Build Date |', file=file)
        print(f'|--------------|-------------------|--------------|----------|------------|', file=file)
        return



    def fprint_version_table(self, file, btc_targets, camera_targets):
        repository_base = "github.com/robertzak133/unified-btc-reverse/blob/main/targets/"
        self.fprint_banner(file)
        for camera_target in btc_targets:
            if camera_targets.count(camera_target) != 0:
                brn_filename = btc_targets[camera_target]['Factory BRN Filename']
                if ('Version' in btc_targets[camera_target]):
                    firmware_version = btc_targets[camera_target]['Version']
                    now = datetime.now() # current date and time
                    current_date = now.strftime("%Y-%m-%d")
                    target_directory =  btc_targets[camera_target]['Target Directory']
                    factory_BRN_directory = btc_targets[camera_target]['Factory BRN Dir']
                    factory_url = "https://" + repository_base + target_directory + "/factory-firmware-images/"+ factory_BRN_directory + "/" + brn_filename
                    wbwl_release_url = "https://" + repository_base + target_directory + "/created-burn-images/RELEASE/" + brn_filename
                    self.fprint_camera_line(file, camera_target, "[" + brn_filename + "](" + factory_url + ")","["+ brn_filename + "](" + wbwl_release_url+ ")", firmware_version, current_date)
        return


    def file_print_version_table(self, dir, filename, build_database, camera_targets):
        extended_filename = os.path.join(dir, filename)
        print(f'Extended Filename = {extended_filename}')
        with open(extended_filename, 'w') as f:
            self.fprint_version_table(f, build_database, camera_targets)
        return

    def file_print_eeprom_table(self, dir, filename, build_database, camera_targets):
        extended_filename = os.path.join(dir, filename)
        print(f'Extended Filename = {extended_filename}')
        with open(extended_filename, 'w') as f:
            self.fprint_eeprom_table(f, build_database, camera_targets)
        return


    def fprint_eeprom_table(self, file, btc_targets, camera_targets):
        repository_base = "github.com/robertzak133/unified-btc-reverse/blob/main/targets/"
        self.fprint_eeprom_banner(file)
        for camera_target in btc_targets:
            if camera_targets.count(camera_target) != 0:
                print(f'camera_target: {camera_target}')
                eeprom_filename = btc_targets[camera_target]['EEPROM Filename']
                eeprom_dir = btc_targets[camera_target]['EEPROM Dir']
                pcb_locator = btc_targets[camera_target]['EEPROM PCB Locator']
                target_directory =  btc_targets[camera_target]['Target Directory']
                eeprom_url = "https://" + repository_base + target_directory + "/eeprom-images/" + eeprom_dir + "/" + eeprom_filename
                self.fprint_camera_eeprom_line(file, camera_target, pcb_locator, "[" + eeprom_filename + "](" + eeprom_url + ")")
        return

	
    
