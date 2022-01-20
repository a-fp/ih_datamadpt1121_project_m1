from modules import Analysis as An
from fuzzywuzzy import process
from modules import Wrangling as Wa
monuments_clean = Wa.mercator_1()

#def all_places():
    #df_minimum = pd.DataFrame(columns=["Place of interest","Type of place","Place address","BiciMAD station","Station location"])
    #for place in monuments_clean["Place of interest"]:
        #df_filter2 = df_sumary[df_sumary["Place of interest"] == place]
        #df_places =  df_filter2[df_filter2['Distance'] == df_filter2['Distance'].min()]
        #df_places_clear = df_places[["Place of interest","Type of place","Place address","BiciMAD station","Station location"]]
        #df_minimum = df_minimum.append(df_places_clear)
    #return df_minimum

df_sumary = An.apply_distance_meters()
    
def minimum():
    ok= list(monuments_clean["Place of interest"].unique())
    usuario = input('Pon el lugar de interés: ')
    aprox=process.extractOne(usuario, ok, score_cutoff=80)
    df_filter = df_sumary[df_sumary["Place of interest"] == aprox[0]]
    pre_minimum = df_filter[df_filter['Distance'] == df_filter['Distance'].min()]
    minimum = pre_minimum[["Place of interest","Type of place","Place address","BiciMAD station","Station location","Distance"]]
    return minimum

def all_places():  
    return df_sumary.sort_values(by = "Distance", ascending = True).groupby('Place of interest')['Type of place','Place address','BiciMAD station', 'Station location','Distance'].nth(0).drop(["Distance"], axis = "columns") 
