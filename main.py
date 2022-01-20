from modules import Acquisition as Ac
from modules import Wrangling as Wa
from modules import Analysis as An
from modules import Reporting as Re
import argparse

# Lo almaceno en variables
stations_clean = Ac.stations()
monuments_clean = Ac.monuments()
monuments_clean = Wa.mercator_1()
stations_clean = Wa.mercator_2()    
df_sumary = Wa.merge()
df_sumary = An.apply_distance_meters()


# Argument parser function  
def argument_parser():
    parser = argparse.ArgumentParser(description='Stations')
    parser.add_argument('-f','--function', type=str, help= 'Calculates the closest scaon from a point or several. "minumum" calculates the distance from an indicated monument. "all" calculates the nearest station from all monuments.')
    args=parser.parse_args()
    return args 
    

# Main pipeline function
def main(arguments):
    print('--//--- starting application ---//--')
    print('\n')
    if arguments.function == 'minimum':  
        place = Re.minimum()    
        print(place[['BiciMAD station', 'Station location']])
        print('Tienes que andar:')
        print(place[['Distance']])
        print('Vuelve a escribir para exportarlo')
        print(Re.minimum().to_csv('Near_Stations.csv', sep=';'))
        print('¡Exportado: Near_Stations!')
    elif arguments.function == 'all':
        print(Re.all_places().to_csv('All_Stations.csv', sep=';'))
        print('¡Exportado: All_Stations!')
    print('\n\n')
    print('\n')
    print('--//--- closing application ---//--')
    
# Pipeline execution
if __name__ == '__main__':
    main(argument_parser())




