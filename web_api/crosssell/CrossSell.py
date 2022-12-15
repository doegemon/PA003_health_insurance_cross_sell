import pickle
import pandas as pd

class CrossSell:
    
    def __init__(self):
        self.home_path = ''
        self.policy_sales_channel_encoder = pickle.load(open(self.home_path + 'parameters/policy_sales_channel_encoder.pkl', 'rb'))
        self.annual_premium_rescaler      = pickle.load(open(self.home_path + 'parameters/annual_premium_rescaler.pkl', 'rb'))
        self.vehicle_damage_encoder       = pickle.load(open(self.home_path + 'parameters/vehicle_damage_encoder.pkl', 'rb'))
        self.vintage_rescaler             = pickle.load(open(self.home_path + 'parameters/vintage_rescaler.pkl', 'rb'))
        self.gender_encoder               = pickle.load(open(self.home_path + 'parameters/gender_encoder.pkl', 'rb'))
        self.region_encoder               = pickle.load(open(self.home_path + 'parameters/region_encoder.pkl', 'rb'))
        self.age_rescaler                 = pickle.load(open(self.home_path + 'parameters/age_rescaler.pkl', 'rb'))
        
    def data_cleaning(self, df1):
        # Alterando os tipos de dados de duas colunas
        df1['region_code'] = df1['region_code'].astype('int64')
        df1['policy_sales_channel'] = df1['policy_sales_channel'].astype('int64')
        
        return df1
    
    def feature_engineering(self, df2):
        # Alterando a redação dos valores da variável
        df2['vehicle_age'] = df2['vehicle_age'].apply(lambda x: 'over_2_years' if x == '> 2 Years' else
                                             ('between_1_and_2_years' if x == '1-2 Year'else 'below_1_year'))
        
        return df2
    
    def data_preparation(self, df4):
        # Rescaling
        df4['annual_premium'] = self.annual_premium_rescaler.transform(df4[['annual_premium']].values)
        df4['vintage']        = self.vintage_rescaler.transform(df4[['vintage']].values)
        df4['age']            = self.age_rescaler.transform(df4[['age']].values)
        
        # Encoding
        df4.loc[:, 'policy_sales_channel'] = df4['policy_sales_channel'].map(self.policy_sales_channel_encoder)
        df4['vehicle_damage']              = self.vehicle_damage_encoder.transform(df4['vehicle_damage'])
        df4.loc[:, 'region_code']          = df4['region_code'].map(self.region_encoder)
        assortment_dict                    = {'below_1_year': 0, 'between_1_and_2_years': 1, 'over_2_years': 2}
        df4['vehicle_age']                 = df4['vehicle_age'].map(assortment_dict)
        df4['gender']                      = self.gender_encoder.transform(df4['gender'])
        
        # Seleção de Variáveis
        cols_selected = ['vintage', 'annual_premium', 'age', 'region_code',
                        'vehicle_damage', 'policy_sales_channel', 'previously_insured']
        
        return df4[cols_selected]
    
    def get_prediction(self, model, original_data, test_data):
        # Previsão do Modelo
        pred = model.predict_proba( test_data )
        
        # Juntar as previsões/scores no conjunto de dados
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )
        