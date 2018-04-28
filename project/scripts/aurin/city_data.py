# vedant & shashank
# comp90024

import json


class AurinData():

    def __init__(self):
        pass

    def aurin(self):

        # melbourne values
        total_females_melb = 0
        total_males_melb = 0
        total_persons_melb = 0
        north_america_melb = 0
        africa_melb = 0
        europe_melb = 0
        asia_melb = 0
        australia_melb = 0
        new_zealand_melb = 0
        born_elsewhere_melb = 0
        # sydney values
        total_females_syd = 0
        total_males_syd = 0
        total_persons_syd = 0
        north_america_syd = 0
        africa_syd = 0
        europe_syd = 0
        asia_syd = 0
        australia_syd = 0
        new_zealand_syd = 0
        born_elsewhere_syd = 0
        # brisbane values
        total_females_bris = 0
        total_males_bris = 0
        total_persons_bris = 0
        north_america_bris = 0
        africa_bris = 0
        europe_bris = 0
        asia_bris = 0
        australia_bris = 0
        new_zealand_bris = 0
        born_elsewhere_bris = 0
        # hobart values
        total_females_hob = 0
        total_males_hob = 0
        total_persons_hob = 0
        north_america_hob = 0
        africa_hob = 0
        europe_hob = 0
        asia_hob = 0
        australia_hob = 0
        new_zealand_hob = 0
        born_elsewhere_hob = 0
        # perth values
        total_females_per = 0
        total_males_per = 0
        total_persons_per = 0
        north_america_per = 0
        africa_per = 0
        europe_per = 0
        asia_per = 0
        australia_per = 0
        new_zealand_per = 0
        born_elsewhere_per = 0
        # canberra values
        total_females_can = 0
        total_males_can = 0
        total_cansons_can = 0
        north_america_can = 0
        africa_can = 0
        europe_can = 0
        asia_can = 0
        australia_can = 0
        new_zealand_can = 0
        born_elsewhere_can = 0
        # darwin values
        total_females_dar = 0
        total_males_dar = 0
        total_darsons_dar = 0
        north_america_dar = 0
        africa_dar = 0
        europe_dar = 0
        asia_dar = 0
        australia_dar = 0
        new_zealand_dar = 0
        born_elsewhere_dar = 0
        # adelaide values
        total_females_ade = 0
        total_males_ade = 0
        total_adesons_ade = 0
        north_america_ade = 0
        africa_ade = 0
        europe_ade = 0
        asia_ade = 0
        australia_ade = 0
        new_zealand_ade = 0
        born_elsewhere_ade = 0

        try:
            file = open(
                "C:\Users\Dhruv\Desktop\unimelb\Subjects\Sem 2\Cloud Computing\Assignments\Assignment 2\citydata_birthcountries.json",
                "r")

            data = json.load(file)

            city_list = data["features"]
            for city in city_list:
                for key, value in city["properties"].items():
                    if (key == "sa4_name16" and str(value).__contains__("Melbourne")):
                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_melb += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_melb += africa
                        australia_melb = city["properties"]["australia_p"]
                        new_zealand_melb = city["properties"]["new_zealand_p"]
                        born_elsewhere_melb = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_melb += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"]["sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_melb += asia
                        total_females_melb = city["properties"]["tot_f"]
                        total_males_melb = city["properties"]["tot_m"]
                        total_persons_melb = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Sydney")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_syd += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_syd += africa
                        australia_syd = city["properties"]["australia_p"]
                        new_zealand_syd = city["properties"]["new_zealand_p"]
                        born_elsewhere_syd = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_syd += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_syd += asia
                        total_females_syd = city["properties"]["tot_f"]
                        total_males_syd = city["properties"]["tot_m"]
                        total_persons_syd = city["properties"]["tot_p"]
                    elif (key == "sa4_name16" and str(value).__contains__("Hobart")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_hob += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_hob += africa
                        australia_hob = city["properties"]["australia_p"]
                        new_zealand_hob = city["properties"]["new_zealand_p"]
                        born_elsewhere_hob = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_hob += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_hob += asia
                        total_females_hob = city["properties"]["tot_f"]
                        total_males_hob = city["properties"]["tot_m"]
                        total_persons_hob = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Perth")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_per += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_per += africa
                        australia_per = city["properties"]["australia_p"]
                        new_zealand_per = city["properties"]["new_zealand_p"]
                        born_elsewhere_per = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_per += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_per += asia
                        total_females_per = city["properties"]["tot_f"]
                        total_males_per = city["properties"]["tot_m"]
                        total_persons_per = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_dar += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_dar += africa
                        australia_dar = city["properties"]["australia_p"]
                        new_zealand_dar = city["properties"]["new_zealand_p"]
                        born_elsewhere_dar = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_dar += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_dar += asia
                        total_females_dar = city["properties"]["tot_f"]
                        total_males_dar = city["properties"]["tot_m"]
                        total_persons_dar = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Brisbane")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_bris += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_bris += africa
                        australia_bris = city["properties"]["australia_p"]
                        new_zealand_bris = city["properties"]["new_zealand_p"]
                        born_elsewhere_bris = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_bris += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_bris += asia
                        total_females_bris = city["properties"]["tot_f"]
                        total_males_bris = city["properties"]["tot_m"]
                        total_persons_bris = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Darwin")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_dar += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_dar += africa
                        australia_dar = city["properties"]["australia_p"]
                        new_zealand_dar = city["properties"]["new_zealand_p"]
                        born_elsewhere_dar = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_dar += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_dar += asia
                        total_females_dar = city["properties"]["tot_f"]
                        total_males_dar = city["properties"]["tot_m"]
                        total_persons_dar = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_ade += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_ade += africa
                        australia_ade = city["properties"]["australia_p"]
                        new_zealand_ade = city["properties"]["new_zealand_p"]
                        born_elsewhere_ade = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_ade += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"][
                                   "sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + \
                               city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_ade += asia
                        total_females_ade = city["properties"]["tot_f"]
                        total_males_ade = city["properties"]["tot_m"]
                        total_persons_ade = city["properties"]["tot_p"]
                    elif (key == "sa4_name16" and str(value).__contains__("Adelaide")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_ade += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_ade += africa
                        australia_ade = city["properties"]["australia_p"]
                        new_zealand_ade = city["properties"]["new_zealand_p"]
                        born_elsewhere_ade = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_ade += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"]["sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_ade += asia
                        total_females_ade = city["properties"]["tot_f"]
                        total_males_ade = city["properties"]["tot_m"]
                        total_persons_ade = city["properties"]["tot_p"]

                    elif (key == "sa4_name16" and str(value).__contains__("Australian Capital Territory")):

                        north_america = city["properties"]["united_states_america_p"] + city["properties"]["canada_p"]
                        north_america_can += north_america
                        africa = city["properties"]["egypt_p"] + city["properties"]["south_africa_p"] + city["properties"][
                            "zimbabwe_p"]
                        africa_can += africa
                        australia_can = city["properties"]["australia_p"]
                        new_zealand_can = city["properties"]["new_zealand_p"]
                        born_elsewhere_can = city["properties"]["born_elsewhere_p"]
                        europe = city["properties"]["germany_p"] + city["properties"]["croatia_p"] + city["properties"][
                            "united_kingdom_ci_im_p"] + \
                                 city["properties"]["netherlands_p"] + city["properties"]["greece_p"] + city["properties"][
                                     "ireland_p"] + \
                                 city["properties"]["italy_p"] + city["properties"]["turkey_p"] + city["properties"]["poland_p"] + \
                                 city["properties"]["fiji_p"] + city["properties"]["malta_p"]
                        europe_can += europe

                        asia = city["properties"]["china_excl_sars_taiwan_p"] + city["properties"]["vietnam_p"] + \
                               city["properties"]["sri_lanka_p"] + \
                               city["properties"]["japan_p"] + city["properties"]["singapore_p"] + city["properties"][
                                   "malaysia_p"] + \
                               city["properties"]["philippines_p"] + city["properties"]["thailand_p"] + city["properties"][
                                   "hong_kong_sar_china_p"] + \
                               city["properties"]["india_p"] + city["properties"]["indonesia_p"] + city["properties"][
                                   "pakistan_p"] + city["properties"]["iraq_p"] + \
                               city["properties"]["lebanon_p"] + city["properties"]["korea_republic_south_p"]
                        asia_can += asia
                        total_females_can = city["properties"]["tot_f"]
                        total_males_can = city["properties"]["tot_m"]
                        total_persons_can = city["properties"]["tot_p"]

        except:
            print("ERROR: Error in while parsing Aurin data")
