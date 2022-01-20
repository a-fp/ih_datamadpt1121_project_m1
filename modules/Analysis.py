from modules import Wrangling as Wa
from modules import geo_calculations as Ge

df_sumary = Wa.merge()

def apply_distance_meters():
    df_sumary["Distance"] = df_sumary.apply(lambda x: Ge.distance_meters(x['Mercator_start'],x['Mercator_finish']),axis=1)
    return df_sumary
    
df_sumary = apply_distance_meters()